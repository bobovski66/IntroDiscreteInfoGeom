'use strict';
const assert=require('node:assert/strict'),M=require('../assets/math.js');
let checks=0;function near(a,b,e=2e-10){checks++;assert.ok(Math.abs(a-b)<e,`${a} != ${b}`);}function vector(a,b,e=2e-10){a.forEach((v,i)=>near(v,b[i],e));}
function distribution(p){near(M.sum(p),1);assert.ok(p.every(v=>v>=0&&Number.isFinite(v)));checks++;}
vector(M.growth([.5,1/3,1/6],[1,2,3]),[.3,.4,.3]);
let p=[.2,.8];for(let t=1;t<=10;t++){p=M.growth(p,[2,1]);near(p[0],2**t/(4+2**t));}
assert.throws(()=>M.growth([.5,.5],[-1,2]));checks++;
const rng=M.seeded(271828),randp=k=>M.normalize(Array.from({length:k},()=>.02+rng()));
for(let z=0;z<300;z++){
 let p=randp(4),q=randp(4),eta=.01+3*rng(),s=Array.from({length:4},()=>4*rng()-2),r=M.exponential(p,s,eta),Z=M.sum(p.map((v,i)=>v*Math.exp(eta*s[i])));
 distribution(r);vector(M.exponential(p,s.map(v=>v+1000),eta),r,1e-10);
 near(eta*M.sum(q.map((v,i)=>v*s[i]))-M.kl(q,p),Math.log(Z)-M.kl(q,r));
 near(eta*M.sum(r.map((v,i)=>(v-p[i])*s[i])),M.kl(r,p)+M.kl(p,r));
 const lam=.01+.98*rng(),mix=M.mixture(p,q,lam);distribution(mix);assert.ok(M.kl(q,mix)<=(1-lam)*M.kl(q,p)+1e-12);checks++;
 near(M.entropy(mix)-(1-lam)*M.entropy(p)-lam*M.entropy(q),(1-lam)*M.kl(p,mix)+lam*M.kl(q,mix));
 const mid=M.geodesic(p,q,.5);distribution(mid);near(M.distance(p,mid),M.distance(p,q)/2);near(M.distance(mid,q),M.distance(p,q)/2);
 near(M.distance(p,q),M.distance(q,p));near(M.distance(p,p),0);
 const K=Array.from({length:3},()=>Array(4));for(let i=0;i<4;i++){const col=randp(3);col.forEach((v,j)=>K[j][i]=v);}const a=M.channel(K,p),b=M.channel(K,q);distribution(a);distribution(b);assert.ok(M.kl(a,b)<=M.kl(p,q)+1e-12);assert.ok(M.distance(a,b)<=M.distance(p,q)+1e-12);checks+=2;
 let c=randp(3),scores=[c[1]-c[2],c[2]-c[0],c[0]-c[1]],updated=M.exponential(c,scores,.5),oldProduct=c.reduce((a,b)=>a*b,1),newProduct=updated.reduce((a,b)=>a*b,1),norm=M.sum(c.map((v,i)=>v*Math.exp(.5*scores[i])));near(newProduct,oldProduct/norm**3);assert.ok(newProduct<=oldProduct+1e-12);checks++;
 const x=.001+.998*rng(),A=[[2,4],[3,1]],y=M.selection([x,1-x],A,eta,'linear')[0];assert.ok((x-.75)*(y-.75)>=0);assert.ok(Math.abs(y-.75)<=Math.abs(x-.75));checks+=2;
}
for(let N=2;N<=50;N+=3){const p=.03+.94*rng(),b=M.binomial(N,p);distribution(b);near(M.sum(b.map((v,k)=>k*v)),N*p,1e-8);near(M.sum(b.map((v,k)=>(k-N*p)**2*v)),N*p*(1-p),1e-8);}
for(let N=3;N<=10;N++){
 const g=M.lattice(N);assert.equal(g.vertices.length,(N+1)*(N+2)/2);checks++;
 for(const [a,b]of [[0,g.vertices.length-1],[2,Math.floor(g.vertices.length/2)],[1,1]]){
  const r=M.shortest(g,a,b);let total=0;for(let k=1;k<r.path.length;k++){const u=g.vertices[r.path[k-1]],v=g.vertices[r.path[k]];assert.equal(M.sum(u.map((x,i)=>Math.abs(x-v[i]))),2);total+=M.distance(u.map(x=>x/N),v.map(x=>x/N));checks++;}near(total,r.length);assert.ok(total>=M.distance(g.vertices[a].map(x=>x/N),g.vertices[b].map(x=>x/N))-1e-10);checks++;
 }
}
assert.equal(M.kl([.5,.5],[1,0]),Infinity);near(M.distance([1,0],[0,1]),Math.PI);vector(M.geodesic([1,0],[.25,.75],.5),[.75,.25]);
console.log(`${checks} numerical and structural checks passed.`);
