(function(){'use strict';
 const $=s=>document.querySelector(s);
 const read=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback;}catch{return fallback;}};
 const save=(key,value)=>{try{localStorage.setItem(key,JSON.stringify(value));return true;}catch{return false;}};
 document.querySelectorAll('[data-complete]').forEach(box=>{const key='dig-complete-'+box.dataset.complete;box.checked=read(key,false);box.addEventListener('change',()=>save(key,box.checked));});
 const week=$('[data-week]')?.dataset.week;
 if($('.lab-form')){
   const key='dig-lab-'+week,answers=read(key,{}),fields=[...document.querySelectorAll('textarea')],status=$('#save-status');
   fields.forEach(t=>{t.value=answers[t.name]||'';t.addEventListener('input',()=>{answers[t.name]=t.value;status.textContent=save(key,answers)?'Answers saved on this device.':'Storage is unavailable; download your answers to keep them.';});});
   if(Object.values(answers).some(Boolean))status.textContent='Saved answers restored.';
   $('#clear-lab').addEventListener('click',()=>{if(!confirm('Clear the answers saved for this week on this device?'))return;fields.forEach(t=>{t.value='';delete answers[t.name];});save(key,answers);status.textContent='Answers cleared.';});
   $('#export-lab').addEventListener('click',async()=>{
     if(window.MathJax?.startup?.promise){try{await window.MathJax.startup.promise;}catch{}}
     const main=$('main').cloneNode(true);main.querySelectorAll('.week-nav,.prev-next,.lab-actions').forEach(n=>n.remove());
     const originals=[...document.querySelectorAll('textarea')];
     main.querySelectorAll('textarea').forEach((t,i)=>{const div=document.createElement('div');div.className='answer';div.textContent=originals[i].value||'(No answer recorded.)';t.replaceWith(div);});
     main.querySelectorAll('script').forEach(n=>n.remove());
     const stamp=document.createElement('p');stamp.textContent='Saved '+new Date().toLocaleString();main.insertBefore(stamp,main.firstChild);
     const mathStyle=$('#MJX-SVG-styles')?.textContent||'';
     const style='body{max-width:850px;margin:3rem auto;padding:0 1.3rem;font:18px/1.65 Georgia,serif;color:#17334b}h1{line-height:1.2}h2{font-size:1.4rem}.answer{white-space:pre-wrap;border:1px solid #ccd8da;padding:1rem;margin:1rem 0 2rem;font:16px/1.6 system-ui,sans-serif;color:#263944}.lab-question{border-top:1px solid #ccd8da;padding-top:1rem}label{font-size:14px}mjx-container{max-width:100%;overflow:auto}'+mathStyle;
     const content='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Week '+week+' laboratory answers</title><style>'+style+'</style></head><body>'+main.innerHTML+'</body></html>';
     const blob=new Blob([content],{type:'text/html;charset=utf-8'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='week'+String(week).padStart(2,'0')+'-lab-answers.html';a.click();setTimeout(()=>URL.revokeObjectURL(url),2000);status.textContent='Answer copy downloaded.';
   });
 }
 if($('#quiz-form')){
   const qs=JSON.parse($('#quiz-data').textContent),key='dig-quiz-'+week,state=read(key,{choices:{},checked:false});
   if(!state.choices)state.choices={};
   const grade=()=>{let count=0,attempted=0;qs.forEach((q,i)=>{const v=state.choices[i],p=$('#feedback-'+i);if(v===undefined){p.className='feedback';p.textContent='Choose an answer to receive feedback.';return;}attempted++;const right=Number(v)===q.answer;if(right)count++;p.className='feedback '+(right?'correct':'incorrect');p.textContent=(right?'Correct. ':'Review. The correct answer is '+q.choices[q.answer]+'. ')+q.explanation;});$('#quiz-score').textContent=count+' of '+qs.length+' correct; '+attempted+' answered.';};
   document.querySelectorAll('#quiz-form input').forEach(r=>{const i=Number(r.name.slice(1));if(String(state.choices[i])===r.value)r.checked=true;r.addEventListener('change',()=>{state.choices[i]=Number(r.value);state.checked=false;save(key,state);$('#feedback-'+i).textContent='';$('#quiz-score').textContent='Selection saved. Check answers when ready.';});});
   $('#check-quiz').addEventListener('click',()=>{state.checked=true;save(key,state);grade();});
   $('#reset-quiz').addEventListener('click',()=>{state.choices={};state.checked=false;save(key,state);$('#quiz-form').reset();document.querySelectorAll('.feedback').forEach(p=>p.textContent='');$('#quiz-score').textContent='Quiz reset.';});
   if(state.checked)grade();
 }
})();
