#!/usr/bin/env python3
"""Check links, course inventories, compiled text, and self-contained sources."""
from pathlib import Path
from html.parser import HTMLParser
import sys,re,json,subprocess
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from course import WEEKS
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.text=[]
 def handle_data(self,text):self.text.append(text)
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.add(d['id'])
  for a in ['href','src']:
   if a in d:self.links.append(d[a])
errors=[];pages=[]
for folder in ['readings','demos','labs','quizzes']:
 files=sorted((ROOT/folder).glob('week*.html'));assert len(files)==10;pages+=files
pages+=[ROOT/'index.html',ROOT/'guide.html']
for p in pages:
 parser=Links();text=p.read_text();parser.feed(text)
 for x in parser.links:
  if x.startswith('#') and x[1:] not in parser.ids:
   errors.append(f'{p.relative_to(ROOT)}: missing anchor {x}')
  if x.startswith(('http:','https:','#','data:','mailto:')):continue
  target=(p.parent/x.split('#')[0]).resolve()
  if not target.exists():errors.append(f'{p.relative_to(ROOT)}: missing {x}')
 if len(re.findall(r'<h1(?:\s|>)',text))!=1:errors.append(f'{p}: expected one h1')
for w in WEEKS:
 assert len(w['lab'])==5 and len(w['quiz'])==8
 assert all(0<=q['answer']<len(q['choices'])==4 for q in w['quiz'])
def normalized(text):
 text=re.sub(r'-\s*\n\s*','',text)
 return ' '.join(re.findall(r'[a-z0-9]+',text.lower()))
def pdf_text(path):
 return subprocess.run(['pdftotext',str(path),'-'],capture_output=True,text=True,check=True).stdout
book=normalized(pdf_text(ROOT/'textbook/pdf/discrete_information_geometry.pdf'))
for n in range(1,11):
 s=f'{n:02}';source=(ROOT/f'src/ch{s}.md').read_text()
 opening=' '.join(normalized(source.split('\n\n')[0]).split()[:8])
 chapter=normalized(pdf_text(ROOT/f'textbook/pdf/chapter{s}.pdf'))
 reading_source=(ROOT/f'readings/week{s}.html').read_text()
 reading_parser=Links();reading_parser.feed(reading_source)
 reading=normalized(' '.join(reading_parser.text))
 contents=re.search(r'<nav aria-label="Reading contents"><ol>(.*?)</ol>',reading_source,re.S)
 section_count=len(re.findall(r'^## ',source,re.M))-1
 if not contents or contents[1].count('<li>')!=section_count:
  errors.append(f'Chapter {n}: contents do not cover every reading section')
 for kind,content in [('book',book),('chapter PDF',chapter),('web reading',reading)]:
  if opening not in content:errors.append(f'Chapter {n}: {kind} does not match the current source opening')
 exercises=source.split('## Exercises')[1].split('## Selected solutions')[0]
 if re.findall(r'^(\d+)\. ',exercises,re.M)!=[str(i) for i in range(1,13)]:
  errors.append(f'Chapter {n}: expected twelve numbered exercises')
 if len(re.findall(r'^\*\*\d+\.\*\*',source,re.M))!=6:
  errors.append(f'Chapter {n}: expected six selected solutions')
for p in (ROOT/'textbook/latex').glob('*.tex'):
 s=p.read_text();assert '\\begin{document}'in s and '\\end{document}'in s
 assert not re.search(r'\\(?:input|includegraphics)\{',s),f'External dependency in {p}'
for p in (ROOT/'tmp/latex').glob('*.log'):
 s=p.read_text(errors='replace')
 for pattern in ['Overfull','multiply defined','undefined references','! LaTeX Error']:
  if pattern in s:errors.append(f'{p.name}: {pattern}')
if errors:
 print('\n'.join(errors));sys.exit(1)
print(f'{len(pages)} pages: links, contents anchors, exercise counts, synchronized PDF openings, standalone LaTeX, and compilation logs passed.')
