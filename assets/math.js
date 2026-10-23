/* Finite probability operations. Shared by demonstrations and numerical tests. */
(function(root){'use strict';
 const sum=a=>a.reduce((s,v)=>s+v,0);
 function probability(p){if(!Array.isArray(p)||!p.length||p.some(v=>!Number.isFinite(v)||v<0)||Math.abs(sum(p)-1)>1e-9)throw Error('Expected nonnegative probabilities with total one.');return p;}
 function normalize(a){if(!a.length||a.some(v=>!Number.isFinite(v)||v<0)||!(sum(a)>0))throw Error('Weights must be nonnegative with positive finite total.');const z=sum(a);return a.map(v=>v/z);}
 function growth(p,w){probability(p);if(w.length!==p.length||w.some(v=>!Number.isFinite(v)||v<=0))throw Error('Multipliers must be positive.');return normalize(p.map((v,i)=>v*w[i]));}
 function scores(M,p){return M.map(row=>sum(row.map((v,i)=>v*p[i])));}
 function exponential(p,s,eta){probability(p);if(s.length!==p.length||s.some(v=>!Number.isFinite(v))||!Number.isFinite(eta)||eta<0)throw Error('Invalid scores or intensity.');const m=Math.max(...s.filter((_,i)=>p[i]>0));return normalize(p.map((v,i)=>v===0?0:v*Math.exp(eta*(s[i]-m))));}
 function selection(p,M,eta,rule='exponential'){const s=scores(M,p);return rule==='linear'?growth(p,s.map(v=>1+eta*v)):exponential(p,s,eta);}
 function entropy(p,base=Math.E){probability(p);return -sum(p.map(v=>v===0?0:v*Math.log(v)))/Math.log(base);}
 function kl(q,p){probability(q);probability(p);if(q.length!==p.length)throw Error('Tables must have equal length.');if(q.some((v,i)=>v>0&&p[i]===0))return Infinity;return Math.max(0,sum(q.map((v,i)=>v===0?0:v*Math.log(v/p[i]))));}
 function overlap(p,r){probability(p);probability(r);if(p.length!==r.length)throw Error('Tables must have equal length.');return Math.min(1,Math.max(0,sum(p.map((v,i)=>Math.sqrt(v*r[i])))));}
 function distance(p,r){const b=overlap(p,r);return b>1-1e-15?0:2*Math.acos(b);}
 function mixture(p,r,t){if(t<0||t>1)throw Error('Mixture fraction must lie in [0,1].');return p.map((v,i)=>(1-t)*v+t*r[i]);}
 function geodesic(p,r,t){if(t<0||t>1)throw Error('Path fraction must lie in [0,1].');const a=distance(p,r)/2;if(a<1e-10)return mixture(p,r,t);return normalize(p.map((v,i)=>((Math.sin((1-t)*a)*Math.sqrt(v)+Math.sin(t*a)*Math.sqrt(r[i]))/Math.sin(a))**2));}
 function logFactorial(n){let v=0;for(let k=2;k<=n;k++)v+=Math.log(k);return v;}
 function multinomial(counts){const n=sum(counts);return Math.exp(logFactorial(n)-sum(counts.map(logFactorial)));}
 function binomial(n,p){if(!Number.isInteger(n)||n<1||p<0||p>1)throw Error('Invalid binomial parameters.');if(p===0)return [1,...Array(n).fill(0)];if(p===1)return [...Array(n).fill(0),1];return normalize(Array.from({length:n+1},(_,k)=>Math.exp(logFactorial(n)-logFactorial(k)-logFactorial(n-k)+k*Math.log(p)+(n-k)*Math.log1p(-p))));}
 function seeded(seed){let a=seed>>>0;return ()=>{a=(1664525*a+1013904223)>>>0;return a/4294967296;};}
 function channel(K,p){probability(p);if(!K.length||K.some(row=>row.length!==p.length||row.some(v=>!Number.isFinite(v)||v<0)))throw Error('Invalid channel.');for(let i=0;i<p.length;i++)if(Math.abs(sum(K.map(row=>row[i]))-1)>1e-9)throw Error('Channel columns must sum to one.');return K.map(row=>sum(row.map((v,i)=>v*p[i])));}
 function lattice(N){if(!Number.isInteger(N)||N<1)throw Error('Token denominator must be a positive integer.');const vertices=[],index=new Map();for(let a=0;a<=N;a++)for(let b=0;b<=N-a;b++){const c=N-a-b;index.set([a,b,c].join(','),vertices.length);vertices.push([a,b,c]);}const edges=vertices.map(c=>{const out=[];for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(i!==j&&c[i]>0){const v=c.slice();v[i]--;v[j]++;const k=index.get(v.join(','));out.push([k,distance(c.map(x=>x/N),v.map(x=>x/N))]);}return out;});return {N,vertices,edges,index};}
 function shortest(graph,start,end){const n=graph.vertices.length,d=Array(n).fill(Infinity),prev=Array(n).fill(-1),done=Array(n).fill(false);d[start]=0;for(let z=0;z<n;z++){let u=-1;for(let i=0;i<n;i++)if(!done[i]&&(u<0||d[i]<d[u]))u=i;if(u<0||!Number.isFinite(d[u]))break;done[u]=true;if(u===end)break;for(const [v,w]of graph.edges[u])if(!done[v]&&d[u]+w<d[v]-1e-13){d[v]=d[u]+w;prev[v]=u;}}const path=[];if(Number.isFinite(d[end])){let v=end;while(v!==-1){path.push(v);v=prev[v];}path.reverse();}return {length:d[end],path,distances:d};}
 const api={sum,probability,normalize,growth,scores,exponential,selection,entropy,kl,overlap,distance,mixture,geodesic,logFactorial,multinomial,binomial,seeded,channel,lattice,shortest};
 root.DIG=api;if(typeof module!=='undefined')module.exports=api;
})(typeof globalThis!=='undefined'?globalThis:this);
