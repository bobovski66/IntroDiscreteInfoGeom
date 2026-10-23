#!/usr/bin/env python3
"""Check links, course inventories, compiled text, and self-contained sources."""
from pathlib import Path
from html.parser import HTMLParser
import sys,re,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from course import WEEKS
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  for a in ['href','src']:
   if a in d:self.links.append(d[a])
errors=[];pages=[]
for folder in ['readings','demos','labs','quizzes']:
 files=sorted((ROOT/folder).glob('week*.html'));assert len(files)==10;pages+=files
pages+=[ROOT/'index.html',ROOT/'guide.html']
for p in pages:
 parser=Links();text=p.read_text();parser.feed(text)
 for x in parser.links:
  if x.startswith(('http:','https:','#','data:','mailto:')):continue
  target=(p.parent/x.split('#')[0]).resolve()
  if not target.exists():errors.append(f'{p.relative_to(ROOT)}: missing {x}')
 if len(re.findall(r'<h1(?:\s|>)',text))!=1:errors.append(f'{p}: expected one h1')
for w in WEEKS:
 assert len(w['lab'])==5 and len(w['quiz'])==8
 assert all(0<=q['answer']<len(q['choices'])==4 for q in w['quiz'])
for p in (ROOT/'textbook/latex').glob('*.tex'):
 s=p.read_text();assert '\\begin{document}'in s and '\\end{document}'in s
 assert not re.search(r'\\(?:input|includegraphics)\{',s),f'External dependency in {p}'
for p in (ROOT/'tmp/latex').glob('*.log'):
 s=p.read_text(errors='replace')
 for pattern in ['Overfull','multiply defined','undefined references','! LaTeX Error']:
  if pattern in s:errors.append(f'{p.name}: {pattern}')
if errors:
 print('\n'.join(errors));sys.exit(1)
print(f'{len(pages)} pages: local links, resource counts, standalone LaTeX, and compilation logs passed.')
