"""Exact vector figures shared by the textbook and the web readings."""
import math, random

def coords(points):
    return ' '.join('(%g,%g)'%(x,y) for x,y in points)
def normalized(p,w):
    z=sum(a*b for a,b in zip(p,w)); return [a*b/z for a,b in zip(p,w)]
def expstep(p,s,eta):
    m=max(s); return normalized(p,[math.exp(eta*(a-m)) for a in s])
def xy(p): return p[1]+p[2]/2, math.sqrt(3)*p[2]/2
def triangle():
    return r'\draw[ink,thick] (0,0)--(6,0)--(3,5.196)--cycle;\node[below left] at (0,0){$A$};\node[below right] at (6,0){$B$};\node[above] at (3,5.196){$C$};'
def tri_path(ps,color,style=''):
    return r'\draw[%s,line width=1pt,%s] plot coordinates {%s};'%(color,style,coords([(6*xy(p)[0],6*xy(p)[1]) for p in ps]))
def distance(p,r): return 2*math.acos(max(0,min(1,sum(math.sqrt(a*b) for a,b in zip(p,r)))))
def geo(p,r,t):
    a=distance(p,r)/2
    if a<1e-12:return p[:]
    s=[(math.sin((1-t)*a)*math.sqrt(x)+math.sin(t*a)*math.sqrt(y))/math.sin(a) for x,y in zip(p,r)]
    z=sum(v*v for v in s);return [v*v/z for v in s]

FIGURES={}
FIGURES['growth']=(r'''
\begin{tikzpicture}
\begin{axis}[width=6.7cm,height=5.3cm,xlabel={Step $t$},ylabel={Count},xmin=0,xmax=6,ymin=0,legend pos=north west]
\addplot[teal,mark=*] coordinates {'''+coords([(t,20*2**t)for t in range(7)])+r'''};\addlegendentry{$A$}
\addplot[copper,mark=square*] coordinates {'''+coords([(t,80)for t in range(7)])+r'''};\addlegendentry{$B$}
\end{axis}
\begin{axis}[at={(6.5cm,0)},anchor=south west,width=6.7cm,height=5.3cm,xlabel={Step $t$},ylabel={$A$ proportion},xmin=0,xmax=6,ymin=0,ymax=1]
\addplot[teal,mark=*] coordinates {'''+coords([(t,2**t/(4+2**t))for t in range(7)])+r'''};
\end{axis}\end{tikzpicture}''',
'Counts and proportions for initial counts (20,80) and multipliers (2,1). The total population changes at every step.')

lin=[.25];exp=[.25]
for _ in range(12):
    x=lin[-1];f=[4-2*x,1+2*x];lin.append(normalized([x,1-x],[1+2*s for s in f])[0])
    x=exp[-1];exp.append(expstep([x,1-x],[4-2*x,1+2*x],2)[0])
FIGURES['payoff']=(r'''\begin{tikzpicture}
\begin{axis}[width=6.7cm,height=5.4cm,xlabel={$A$ proportion $x$},ylabel={Score},xmin=0,xmax=1,ymin=0,ymax=4.5,legend pos=south east]
\addplot[teal,domain=0:1]{4-2*x};\addlegendentry{$f_A$}
\addplot[copper,domain=0:1]{1+2*x};\addlegendentry{$f_B$}
\draw[dashed] (axis cs:.75,0)--(axis cs:.75,4.3);
\end{axis}
\begin{axis}[at={(6.5cm,0)},anchor=south west,width=6.7cm,height=5.4cm,xlabel={Step $t$},ylabel={$A$ proportion},xmin=0,xmax=12,ymin=0,ymax=1,legend pos=south east]
\addplot[teal,mark=*] coordinates {'''+coords(enumerate(lin))+r'''};\addlegendentry{Linear}
\addplot[copper,mark=square*] coordinates {'''+coords(enumerate(exp))+r'''};\addlegendentry{Exponential}
\addplot[ink,dashed,domain=0:12]{.75};
\end{axis}\end{tikzpicture}''','Coexistence scores and two finite trajectories at intensity 2. The linear rule approaches the equilibrium from one side; the exponential rule crosses it.')

lat=triangle()
for a in range(5):
    for b in range(5-a):
        c=4-a-b;x,y=xy([a/4,b/4,c/4]);lat+=r'\fill[teal] (%g,%g) circle (2pt);'%(6*x,6*y)
lat+=r'\node[anchor=west,align=left] at (6.8,3.7){$N=4$: fifteen states\\One token changes two counts.};'
x,y=xy([.5,.25,.25]);lat+=r'\draw[copper,thick] (%g,%g) circle (5pt);\node[below=6pt] at (%g,%g){$(2,1,1)$};'%(6*x,6*y,6*x,6*y)
for p in [[.25,.5,.25],[.25,.25,.5],[.75,0,.25],[.5,0,.5],[.75,.25,0],[.5,.5,0]]:
    u,v=xy(p);lat+=r'\draw[copper,->] (%g,%g)--(%g,%g);'%(6*x,6*y,6*u,6*v)
FIGURES['lattice']=(r'\begin{tikzpicture}'+lat+r'\end{tikzpicture}','The denominator-four token lattice. Arrows show the six one-token moves from counts (2,1,1).')

p=[.5,1/3,1/6];ps=[p];products=[math.prod(p)]
for _ in range(160):
    p=expstep(p,[p[1]-p[2],p[2]-p[0],p[0]-p[1]],.35);ps.append(p);products.append(math.prod(p))
FIGURES['cyclic']=(r'\begin{tikzpicture}'+triangle()+tri_path(ps,'teal')+r'''
\begin{axis}[at={(7cm,0.2cm)},anchor=south west,width=6.2cm,height=5.2cm,xlabel={Step $t$},ylabel={$p_Ap_Bp_C$},xmin=0,xmax=160,ymin=0]
\addplot[teal] coordinates {'''+coords(enumerate(products))+r'''};
\end{axis}\end{tikzpicture}''','Balanced cyclic exponential updates at intensity 0.35. The triangle trajectory circulates while the coordinate product decreases.')

n=10;p=.3;theory=[math.comb(n,k)*p**k*(1-p)**(n-k)for k in range(n+1)]
rng=random.Random(1729);hist=[0]*(n+1)
for _ in range(200):hist[sum(rng.random()<p for _ in range(n))]+=1
FIGURES['sampling']=(r'''\begin{tikzpicture}\begin{axis}[width=12.5cm,height=5.8cm,xlabel={Success count $k$},ylabel={Probability or frequency},xmin=-.5,xmax=10.5,ymin=0,ymax=.35,xtick={0,1,...,10},legend pos=north east,ybar,bar width=5pt]
\addplot[teal,fill=teal!55] coordinates {'''+coords(enumerate(theory))+r'''};\addlegendentry{Exact binomial}
\addplot[copper,fill=copper!55] coordinates {'''+coords((k,v/200)for k,v in enumerate(hist))+r'''};\addlegendentry{200 samples}
\end{axis}\end{tikzpicture}''','Exact probabilities for ten independent trials with success probability 0.3, compared with frequencies from 200 reproducible simulated samples.')

FIGURES['code']=(r'''\begin{tikzpicture}[level distance=1.5cm,sibling distance=4cm,every node/.style={font=\small},edge from parent/.style={draw,ink,thick},label distance=2pt]
\node[circle,draw=ink,inner sep=3pt]{}
child{node[align=center]{$A:0$\\$p_A=1/2$} edge from parent node[above left]{$0$}}
child{node[circle,draw=ink,inner sep=3pt]{}
child[sibling distance=3cm]{node[align=center]{$B:10$\\$p_B=1/4$} edge from parent node[above left]{$0$}}
child[sibling distance=3cm]{node[align=center]{$C:11$\\$p_C=1/4$} edge from parent node[above right]{$1$}}
edge from parent node[above right]{$1$}};
\node[align=left,anchor=west] at (5,-1.5){Expected length: $3/2$ bits\\Entropy: $3/2$ bits\\Kraft sum: $1$};
\end{tikzpicture}''','A binary prefix tree with code lengths 1, 2, and 2, matched to probabilities (1/2,1/4,1/4).')

q=.5;x=.9;ds=[];bound=[];d0=q*math.log(q/x)+(1-q)*math.log((1-q)/(1-x))
for t in range(13):
    ds.append((t,q*math.log(q/x)+(1-q)*math.log((1-q)/(1-x))));bound.append((t,d0*.75**t));x=.75*x+.25*q
FIGURES['contraction']=(r'''\begin{tikzpicture}\begin{axis}[width=12.5cm,height=5.8cm,xlabel={Step $t$},ylabel={Relative entropy (nats)},xmin=0,xmax=12,ymin=0,legend pos=north east]
\addplot[teal,mark=*] coordinates {'''+coords(ds)+r'''};\addlegendentry{$D(q\Vert p_t)$}
\addplot[copper,dashed,mark=square*] coordinates {'''+coords(bound)+r'''};\addlegendentry{$(1-\lambda)^tD(q\Vert p_0)$}
\end{axis}\end{tikzpicture}''','Mixture contraction toward binary target (0.5,0.5) from (0.9,0.1), with mixture fraction 0.25. The proven bound lies above the actual divergence.')

FIGURES['sphere']=(r'''\begin{tikzpicture}
\draw[->,ink] (0,0)--(4.7,0) node[right]{$2\sqrt{x}$};\draw[->,ink] (0,0)--(0,4.7) node[above]{$2\sqrt{1-x}$};
\draw[teal,line width=1.5pt] (4,0) arc[start angle=0,end angle=90,radius=4];
\draw[ink!40] (0,0)--(2,3.464);\draw[ink!40] (0,0)--(2.828,2.828);
\fill[copper] (2,3.464) circle(2.5pt) node[above right]{$x=1/4$};
\fill[teal] (2.828,2.828) circle(2.5pt) node[above right]{$x=1/2$};
\node[below] at (4,0){$x=1$};\node[left] at (0,4){$x=0$};
\node[align=left] at (2,-1){Radius $2$\\Arc coordinate $2\arcsin\sqrt{x}$};
\begin{axis}[at={(6.7cm,0)},anchor=south west,width=6.1cm,height=5.8cm,xlabel={Probability $x$},ylabel={Arc coordinate},xmin=0,xmax=1,ymin=0,ymax=3.2,ytick={0,1.570796,3.141593},yticklabels={$0$,$\pi/2$,$\pi$}]
\addplot[teal,domain=0:1,samples=101]{2*asin(sqrt(x))*pi/180};
\end{axis}\end{tikzpicture}''','Binary distributions form a quarter circle on the radius-two sphere. Equal probability increments generally cover unequal arc lengths.')

p=[.8,.1,.1];r=[.1,.7,.2]
FIGURES['paths']=(r'\begin{tikzpicture}'+triangle()+tri_path([p,r],'copper','dashed')+tri_path([geo(p,r,t/40)for t in range(41)],'teal')+r'''
\node[anchor=west,align=left,text=teal] at (6.6,3.8){Spherical interpolation};
\node[anchor=west,align=left,text=copper] at (6.6,3.1){Ordinary mixture};
\node[anchor=west,align=left] at (6.6,1.9){$p=(0.8,0.1,0.1)$\\$r=(0.1,0.7,0.2)$};
\end{tikzpicture}''','A spherical geodesic mapped back to the probability triangle, compared with the ordinary mixture segment between the same endpoints.')

p=[.5,1/3,1/6];r=expstep(p,[0,1,2],math.log(2))
FIGURES['learning']=(r'''\begin{tikzpicture}\begin{axis}[width=12.5cm,height=5.6cm,ybar,bar width=14pt,xlabel={Choice},ylabel={Probability},xmin=.5,xmax=3.5,ymin=0,ymax=.65,xtick={1,2,3},legend pos=north east]
\addplot[ink,fill=ink!40] coordinates {'''+coords(enumerate(p,1))+r'''};\addlegendentry{Current table}
\addplot[teal,fill=teal!60] coordinates {'''+coords(enumerate(r,1))+r'''};\addlegendentry{Exponential update}
\end{axis}\end{tikzpicture}''','An exponential update of (1/2,1/3,1/6) with scores (0,1,2) and intensity ln 2 gives (3/11,4/11,4/11).')

FIGURES['network']=(r'''\begin{tikzpicture}[every node/.style={font=\small},>=Stealth]
\node[anchor=west] at (0,4.5){Input label};\node[anchor=west] at (2,4.5){$q_i$};\node[anchor=west] at (3.1,4.5){$p_i$};
\node[anchor=west] at (7,4.5){Recorded group};
\foreach \i/\y/\q/\p in {1/3.5/.4/.1,2/2.5/.1/.4,3/1.5/.4/.1,4/.5/.1/.4}{
\node at (.5,\y){\i};\node at (2.3,\y){\q};\node at (3.4,\y){\p};}
\draw[->,teal,thick] (4,3.5)--(7,3);\draw[->,teal,thick] (4,2.5)--(7,3);
\draw[->,copper,thick] (4,1.5)--(7,1);\draw[->,copper,thick] (4,.5)--(7,1);
\node[anchor=west,align=left] at (7.2,3){Group $\{1,2\}$\\Both models: $1/2$};
\node[anchor=west,align=left] at (7.2,1){Group $\{3,4\}$\\Both models: $1/2$};
\node[anchor=west] at (0,-.5){$D(q\Vert p)=0.6\ln4\quad\longrightarrow\quad D(Kq\Vert Kp)=0$};
\end{tikzpicture}''','Grouping can erase a distinction carried entirely by the probabilities inside each group. Both recorded output tables are identical.')
