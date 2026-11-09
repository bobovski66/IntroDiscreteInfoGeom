#!/usr/bin/env python3
"""Rebuild the static course, self-contained LaTeX files, and compiled PDFs."""
from pathlib import Path
import sys, subprocess, json, html, re, shutil, concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from course import WEEKS,TITLE,SUBTITLE
from figures import FIGURES
from extensions import EXTENSIONS
E=html.escape
def run(args,**kw):
    p=subprocess.run(args,cwd=ROOT,capture_output=True,text=True,**kw)
    if p.returncode: raise RuntimeError(' '.join(map(str,args))+'\n'+p.stdout[-2500:]+'\n'+p.stderr[-2500:])
    return p.stdout
def write(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
def md(text,fmt):
    args=['pandoc','-f','markdown+fenced_divs','-t',fmt,'--lua-filter=scripts/blocks.lua']
    args+=['--mathjax'] if fmt=='html5' else ['--wrap=none','--shift-heading-level-by=-1']
    return run(args,input=text)
def guided(q):
    parts=re.split(r'\s+\(([a-e])\)\s*',q)
    if len(parts)<3:
        return md(q,'html5')
    result=md(parts[0],'html5')+'<ol type="a">'
    for i in range(1,len(parts),2):
        result+='<li>'+md(parts[i+1],'html5')+'</li>'
    return result+'</ol>'
def head(title,pre=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)} · {TITLE}</title><meta name="description" content="A ten-week course in finite information geometry through probability, counting, difference equations, and graphs."><link rel="stylesheet" href="{pre}assets/style.css"><script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]}},svg:{{fontCache:'none'}}}};</script><script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js"></script><script defer src="{pre}assets/site.js"></script></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><a class="wordmark" href="{pre}index.html">Discrete Information Geometry</a><nav aria-label="Main"><a href="{pre}index.html#weeks">Ten weeks</a><a href="{pre}textbook/pdf/discrete_information_geometry.pdf">Textbook</a><a href="{pre}guide.html">Course guide</a></nav></header>'''
def foot(pre=''):
    return f'''<footer><p>{TITLE}<br><span>{SUBTITLE}</span></p><p><a href="{pre}index.html#weeks">Weekly materials</a> · <a href="https://github.com/bobovski66/IntroDiscreteInfoGeom">Source and downloads</a><br>Related course: <a href="https://bobovski66.github.io/IntroInfoGeom/">Introduction to Information Geometry</a></p></footer></body></html>'''
def weekly(w,kind,body):
    n=w['week'];s=f'{n:02}'
    nav=''.join(f'<a {"aria-current=page" if k==kind else ""} href="../{folder}/week{s}.html">{label}</a>'for k,folder,label in [('reading','readings','Reading'),('demo','demos','Demonstration'),('lab','labs','Lab'),('quiz','quizzes','Quiz')])
    prev=f'<a href="../readings/week{n-1:02}.html">← Week {n-1}</a>' if n>1 else '<span></span>'
    nxt=f'<a href="../readings/week{n+1:02}.html">Week {n+1} →</a>' if n<10 else '<a href="../guide.html#capstone">Capstone guidance →</a>'
    return head(f'Week {n}: {w["title"]}','../')+f'<main id="main" class="weekly {kind}" data-week="{n}"><p class="eyebrow">Week {n} · {kind.title()}</p><h1>{E(w["title"])}</h1><nav class="week-nav" aria-label="Week {n} resources">{nav}</nav>'+body+f'<nav class="prev-next" aria-label="Adjacent weeks">{prev}{nxt}</nav></main>'+foot('../')
def make_figures():
    common=r'''\documentclass[border=6pt]{standalone}
\usepackage[T1]{fontenc}\usepackage[sc]{mathpazo}\usepackage{amsmath,amssymb,tikz,pgfplots}
\usetikzlibrary{arrows.meta,calc}\pgfplotsset{compat=1.18}
\definecolor{ink}{HTML}{17334B}\definecolor{teal}{HTML}{137C83}\definecolor{copper}{HTML}{AE5932}
\pgfplotsset{every axis/.append style={axis line style={black!55},tick label style={font=\small},label style={font=\small},legend style={font=\small,draw=none,fill=white},grid style={black!10}},every axis plot/.append style={line width=1.1pt}}
\begin{document}'''
    work=ROOT/'tmp/figures';work.mkdir(parents=True,exist_ok=True)
    for key,(tikz,cap) in FIGURES.items():
        write(f'src/figure-data/{key}.tex',tikz)
        write(f'src/figure-data/{key}.txt',cap)
        f=work/f'{key}.tex';f.write_text(common+tikz+r'\end{document}')
        run(['pdflatex','-halt-on-error','-interaction=nonstopmode',f'-output-directory={work}',str(f)])
        run(['pdftocairo','-svg',str(work/f'{key}.pdf'),str(ROOT/f'assets/fig-{key}.svg')])

PREFACE=r'''
\chapter*{Preface}\addcontentsline{toc}{chapter}{Preface}
This book develops a discrete calculus of information. Finite differences measure changes of sequences and probability distributions, summation reconstructs accumulated changes, and discrete vector calculus describes flows across the edges of probability lattices. Its prerequisites are algebra, fractions, powers, and an interest in mathematical models. Logarithms, matrix notation, probability, and the needed trigonometry are introduced where they are used.

The central objects are sequences and probability distributions on finitely many labels. The first chapters develop finite differences, discrete integration, and difference equations, before using token transfers to define directional derivatives on a probability simplex. A list of population counts becomes a distribution by division by its total. A growth rule becomes a difference equation after normalization. Counting ordered samples leads to multinomial coefficients; logarithmic surprise leads to entropy and relative entropy. Taking square roots places distributions on a sphere, where angles provide statistical distances. Graphs impose finite constraints on possible movements, and stochastic matrices model noisy observations and information networks.

Every recurrence has a stated meaning for one step. Its conclusions are established for that finite rule. In particular, properties of a continuous-time model need not survive repeated finite updates. Exact identities, inequalities, and small examples allow us to examine this issue directly.

The ten chapters are arranged for ten weeks of study. Each chapter contains worked examples, exercises, selected solutions, and a laboratory investigation. The accompanying course site supplies interactive demonstrations and short quizzes. A suggested weekly rhythm is to read the first half of a chapter, work through examples, explore the demonstration, and then complete the remaining reading and laboratory. Four to six hours of preparation and independent work per week is a reasonable starting estimate; discussion time can be adapted to the class.

Calculations use natural logarithms unless bits are specified. A distribution is a column of nonnegative entries adding to one. A positive distribution has no zero entries. For relative entropy, terms with zero first argument contribute zero, while a positive first entry over a zero reference entry gives infinity. Square-root distances remain finite at the boundary. These conventions are explained at their first use and used consistently thereafter.

This course is a companion to \emph{Introduction to Information Geometry}, available at \url{https://bobovski66.github.io/IntroInfoGeom/}. It follows a related progression from population models to information and geometry. Its finite proofs and combinatorial investigations provide a separate entry into the subject.
'''
REFS=r'''
\chapter*{Further reading}\addcontentsline{toc}{chapter}{Further reading}
The following sources provide broader context and more advanced developments. Their prerequisites vary; the present chapters supply the definitions needed for the accompanying course.
\begin{description}[style=nextline,leftmargin=0pt]
\item[Arora, S., Hazan, E., and Kale, S. (2012).] The multiplicative weights update method: a meta-algorithm and applications. \emph{Theory of Computing} 8, 121--164. \url{https://theoryofcomputing.org/articles/v008a006/}. An extensive account of finite learning updates and their applications.
\item[Levin, D. A., and Peres, Y. (2017).] \emph{Markov Chains and Mixing Times}, second edition, with contributions by E. L. Wilmer. American Mathematical Society. Author resources: \url{https://pages.uoregon.edu/dlevin/MARKOV/}. Develops finite Markov chains, stationarity, and convergence.
\item[Nielsen, F. (2020).] An elementary introduction to information geometry. \emph{Entropy} 22(10), 1100. \url{https://doi.org/10.3390/e22101100}. A survey connecting statistical divergences with geometric structures.
\item[Shannon, C. E. (1948).] A mathematical theory of communication. \emph{Bell System Technical Journal} 27, 379--423 and 623--656. The foundational paper on entropy and communication.
\end{description}
'''
def titlepage(individual=None):
    extra=(r'\vspace{1cm}{\Large Chapter '+str(individual)+r'\par}') if individual else ''
    return r'''\begin{titlepage}\color{ink}\centering\vspace*{1.0in}{\small\sffamily PROBABILITY AND MATHEMATICAL MODELLING\par}\vspace{.45in}{\Huge\bfseries Discrete Information\\[.12in]Geometry\par}\vspace{.35in}{\Large Finite Differences, Probability,\\and Information Flows\par}'''+extra+r'''\vfill\begin{tikzpicture}[scale=1.05]\draw[teal,line width=1pt](0,0)--(4,0)--(2,3.464)--cycle;\foreach \a in {0,...,6}{\foreach \b in {0,...,6}{\pgfmathtruncatemacro{\c}{6-\a-\b}\ifnum\c>-1\fill[teal] ({(\b+\c/2)*4/6},{\c*3.464/6}) circle(1.5pt);\fi}}\end{tikzpicture}\vfill{\large A course in ten chapters\par}\vspace{.3in}{\small\url{https://bobovski66.github.io/IntroDiscreteInfoGeom/}\par}\end{titlepage}'''

def build():
    make_figures()
    p=(ROOT/'src/preamble.tex').read_text()
    p=p.replace('The Calculus of Probability Distributions','Discrete Information Geometry').replace('An undergraduate introduction to information geometry','Finite differences, probability, and information flows')
    # These macros support Pandoc output; the complete files require no external figures.
    p+=r'''\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}
\newcommand{\labheading}{\FloatBarrier\section*{Laboratory investigation}\addcontentsline{toc}{section}{Laboratory investigation}}
'''
    chapters=[]
    for w in WEEKS:
        n=w['week'];s=f'{n:02}';source=(ROOT/f'src/ch{s}.md').read_text()
        source=source.replace('## Exercises',EXTENSIONS[n]+'\n## Exercises')
        core=md(source,'latex').replace('\\label{','\\label{ch'+s+'-').replace('\\hypertarget{','\\hypertarget{ch'+s+'-')
        labmd='\n'.join(f'{i}. {q}'for i,q in enumerate(w['lab'],1))
        labtex=r'\labheading'+md(labmd,'latex')
        ch='\n\\chapter{'+w['title']+'}\n'+core+labtex+'\n\\FloatBarrier\n'
        chapters.append(ch)
        single=p+'\n\\begin{document}\n'+titlepage(n)+f'\n\\setcounter{{chapter}}{{{n-1}}}\n'+ch+'\n\\end{document}\n'
        write(f'textbook/latex/chapter{s}.tex',single)
        read=md(source,'html5')
        # Put solutions in an accessible expandable element on the web.
        read=re.sub(r'<h2 id="selected-solutions">Selected solutions</h2>(.*)$',r'<details class="solutions"><summary>Selected exercise solutions</summary>\1</details>',read,flags=re.S)
        objective='<aside class="objectives"><h2>Learning goals</h2><ul>'+''.join('<li>'+E(x)+'</li>'for x in w['objectives'])+'</ul></aside>'
        body=f'<p class="chapter-download"><a href="../textbook/pdf/chapter{s}.pdf">Chapter {n} PDF</a> · <a href="../textbook/latex/chapter{s}.tex">LaTeX source</a></p>'+objective+'<article class="reading-text">'+read+'</article>'
        write(f'readings/week{s}.html',weekly(w,'reading',body))
        body='<p class="lede">'+E(w['demo'])+'</p><p class="operator-link"><a href="../demos/operator-explorer.html">Open the discrete calculus operator explorer</a></p><div id="demo-root" data-demo="'+str(n)+'"></div><noscript><p>Enable JavaScript to use the controls. The reading and PDF contain the formulas and worked examples.</p></noscript><script src="../assets/math.js"></script><script src="../assets/demos.js"></script>'
        write(f'demos/week{s}.html',weekly(w,'demo',body))
        body='<p class="lede">Record calculations, predictions, and observations. Answers are saved in this browser when storage is available; use the download button to keep a separate copy.</p><div class="lab-actions"><button id="export-lab" type="button">Download answers</button><button id="clear-lab" type="button" class="secondary">Clear saved answers</button><span id="save-status" role="status"></span></div><form class="lab-form">'
        for i,q in enumerate(w['lab'],1):
            body+=f'<section class="lab-question"><h2>Investigation {n}.{i}</h2>'+guided(q)+f'<label for="answer-{i}">Your calculations and explanation</label><textarea id="answer-{i}" name="answer-{i}" rows="7" spellcheck="true"></textarea></section>'
        body+='</form>'
        write(f'labs/week{s}.html',weekly(w,'lab',body))
        body='<p class="lede">Choose one answer per question, then check your work. Feedback explains each answer. You can revise and check again.</p><form id="quiz-form">'
        for i,q in enumerate(w['quiz']):
            body+=f'<fieldset><legend>{i+1}. {E(q["prompt"])}</legend>'
            for j,a in enumerate(q['choices']):body+=f'<label><input type="radio" name="q{i}" value="{j}"> <span>{E(a)}</span></label>'
            body+=f'<p class="feedback" id="feedback-{i}" aria-live="polite"></p></fieldset>'
        body+='</form><div class="quiz-actions"><button type="button" id="check-quiz">Check answers</button><button type="button" id="reset-quiz" class="secondary">Reset quiz</button><p id="quiz-score" role="status"></p></div><script type="application/json" id="quiz-data">'+json.dumps(w['quiz']).replace('<','\\u003c')+'</script>'
        write(f'quizzes/week{s}.html',weekly(w,'quiz',body))
    full=p+'\n\\begin{document}\n\\frontmatter\n'+titlepage()+PREFACE+'\n\\tableofcontents\n\\mainmatter\n'+''.join(chapters)+'\n\\backmatter\n'+REFS+'\n\\end{document}\n'
    write('textbook/latex/discrete_information_geometry.tex',full)
    make_index();make_guide()
    write('assets/course.json',json.dumps(WEEKS,indent=2,ensure_ascii=False))
    compile_pdfs()

def make_index():
    rows=''
    for w in WEEKS:
        n=w['week'];s=f'{n:02}'
        links=''.join(f'<a href="{f}/week{s}.html">{l}</a>'for f,l in [('readings','Read'),('demos','Explore'),('labs','Investigate'),('quizzes','Check')])
        rows+=f'<tr><th scope="row"><span class="week-number">{n:02}</span></th><td><h3><a href="readings/week{s}.html">{E(w["title"])}</a></h3><p>{E(w["summary"])}</p><div class="resource-links">{links}</div></td><td class="completion"><label><input type="checkbox" data-complete="{n}"> <span>Complete</span></label></td></tr>'
    body=f'''<main id="main"><section class="hero"><div><p class="eyebrow">A course in ten weeks</p><h1>Discrete<br>Information Geometry</h1><p class="hero-subtitle">Finite Differences, Probability, and Information Flows</p><p>How do probability distributions change? Can we differentiate entropy on a finite lattice? How does information flow through a network?</p><p>Study these questions through finite differences, summation, probability lattices, information gradients, and flows through graphs. The mathematics begins with algebra; logarithms, probability, and angles are developed along the way.</p><p class="hero-links"><a class="primary-link" href="readings/week01.html">Begin with Week 1 →</a><a href="textbook/pdf/discrete_information_geometry.pdf">Read the textbook</a></p></div><figure><img src="assets/fig-lattice.svg" alt="A triangular lattice of fifteen possible compositions of four tokens."><figcaption>Finite states, geometric questions.</figcaption></figure></section><section class="overview"><div><h2>Preparation</h2><p>Fractions, powers, simple equations, and coordinate graphs. The course introduces its probability, matrix notation, logarithms, and trigonometry. Calculus is not a prerequisite.</p></div><div><h2>A weekly rhythm</h2><p>Work through the reading and examples, explore the demonstration, complete the five-part lab, and use the eight-question quiz to check understanding. Allow roughly four to six hours of independent work each week.</p></div></section><section id="weeks"><div class="section-intro"><h2>The ten weeks</h2><p>Each row contains the full set of weekly materials. Completion marks are optional and stored on this device.</p></div><table class="week-table"><thead><tr><th scope="col">Week</th><th scope="col">Topic and materials</th><th scope="col">Progress</th></tr></thead><tbody>{rows}</tbody></table></section><section class="textbook-section"><div><p class="eyebrow">Companion text</p><h2>Ten chapters, one connected argument</h2><p>Worked examples, exact finite proofs, 120 chapter exercises, 50 guided investigations, and 80 check-in questions connect discrete calculus, information, and geometry.</p><p><a href="textbook/pdf/discrete_information_geometry.pdf">Complete textbook PDF</a> · <a href="textbook/latex/discrete_information_geometry.tex">Complete LaTeX source</a> · <a href="textbook/course_materials.zip">Download all chapters and sources</a></p><p>Individual chapter PDFs and LaTeX files are linked from each reading.</p></div></section></main>'''
    body=body.replace('Finite states, geometric questions.','Four tokens shared among three categories.')
    body=body.replace('href="textbook/course_materials.zip"','href="https://github.com/bobovski66/IntroDiscreteInfoGeom/archive/refs/heads/main.zip"')
    write('index.html',head('Ten-week course')+body+foot())

def make_guide():
    body=(ROOT/'src/guide_body.html').read_text(encoding='utf-8')
    write('guide.html',head('Course guide')+body+foot())

def compile_one(f):
    out=ROOT/'tmp/latex';out.mkdir(parents=True,exist_ok=True)
    for _ in range(2):run(['pdflatex','-halt-on-error','-interaction=nonstopmode',f'-output-directory={out}',str(f)])
    shutil.copy2(out/(f.stem+'.pdf'),ROOT/'textbook/pdf'/f'{f.stem}.pdf')
    return f.stem
def compile_pdfs():
    files=list((ROOT/'textbook/latex').glob('*.tex'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for n in pool.map(compile_one,files):print('Compiled',n,flush=True)

if __name__=='__main__':build()
