'use strict';
const header=document.querySelector('.publication-header');
const setHeader=()=>header?.classList.toggle('scrolled',scrollY>35);
addEventListener('scroll',setHeader,{passive:true});setHeader();
const menu=document.querySelector('#publication-menu'),toggle=document.querySelector('#menu-toggle');
toggle?.addEventListener('click',()=>{menu.showModal();toggle.setAttribute('aria-expanded','true')});
menu?.addEventListener('close',()=>{toggle.setAttribute('aria-expanded','false');toggle.focus()});
menu?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>menu.close()));
document.querySelectorAll('[data-close]').forEach(b=>b.addEventListener('click',()=>b.closest('dialog').close()));
document.querySelectorAll('dialog').forEach(d=>d.addEventListener('click',ev=>{if(ev.target===d){const r=d.getBoundingClientRect();if(ev.clientX<r.left||ev.clientX>r.right||ev.clientY<r.top||ev.clientY>r.bottom)d.close()}}));
// No automatic video requests for reduced motion or data-saving connections.
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const saveData=Boolean(navigator.connection?.saveData);
const backgrounds=[...document.querySelectorAll('[data-ambient]')];
function pauseLabel(v){const b=v.parentElement.querySelector('[data-pause]');if(b){b.textContent=v.paused?'Play film':'Pause film';b.setAttribute('aria-label',v.paused?'Play background film':'Pause background film')}}
function loadBackground(v){if(!v.getAttribute('src')){v.src=matchMedia('(max-width:760px)').matches&&v.dataset.mobile?v.dataset.mobile:v.dataset.src;v.load()}}
backgrounds.forEach(v=>{v.addEventListener('play',()=>pauseLabel(v));v.addEventListener('pause',()=>pauseLabel(v));v.addEventListener('error',()=>{v.parentElement.querySelector('[data-pause]')?.setAttribute('disabled','');v.poster=v.poster||'/assets/hero-new/poster.webp'})});
const ambientObserver='IntersectionObserver'in window?new IntersectionObserver(entries=>entries.forEach(({target:v,isIntersecting})=>{v.dataset.visible=String(isIntersecting);if(isIntersecting&&!reduced.matches&&!saveData&&v.dataset.userPaused!=='true'){loadBackground(v);v.play().catch(()=>pauseLabel(v))}else v.pause()}),{threshold:.1}):null;
backgrounds.forEach(v=>ambientObserver?.observe(v));
document.querySelectorAll('[data-pause]').forEach(b=>b.addEventListener('click',()=>{const v=b.parentElement.querySelector('video')||document.querySelector('#opening-film');if(!v)return;if(v.paused){v.dataset.userPaused='false';loadBackground(v);v.play().catch(()=>pauseLabel(v))}else{v.dataset.userPaused='true';v.pause()}}));
reduced.addEventListener('change',()=>{if(reduced.matches)backgrounds.forEach(v=>v.pause())});
document.addEventListener('visibilitychange',()=>{if(document.hidden)backgrounds.forEach(v=>v.pause());else backgrounds.filter(v=>v.dataset.visible==='true'&&v.dataset.userPaused!=='true'&&!reduced.matches&&!saveData).forEach(v=>v.play().catch(()=>{}))});
// Embeds are requested only after a user chooses a film.
const viewer=document.querySelector('#media-viewer'),content=document.querySelector('#viewer-content'),caption=document.querySelector('#viewer-caption');
let lastTrigger=null,photoIndex=0;
const photos=[...document.querySelectorAll('[data-photo]')];
function embed(id,title){const frame=document.createElement('iframe');frame.src='https://www.youtube-nocookie.com/embed/'+encodeURIComponent(id)+'?autoplay=1&playsinline=1&rel=0';frame.title=title;frame.allow='autoplay; encrypted-media; picture-in-picture';frame.allowFullscreen=true;return frame}
function showViewer(trigger,film){lastTrigger=trigger;document.querySelectorAll('video').forEach(v=>v.pause());viewer.classList.toggle('is-film',film);viewer.showModal();viewer.querySelector('[data-close]').focus()}
function showPhoto(i){photoIndex=(i+photos.length)%photos.length;const a=photos[photoIndex];const original=a.querySelector('img'),image=document.createElement('img');image.src=a.href;image.alt=original?.alt||'';content.replaceChildren(image);caption.textContent=a.dataset.caption;viewer.setAttribute('aria-label','Photograph: '+caption.textContent)}
photos.forEach((a,i)=>a.addEventListener('click',ev=>{if(ev.ctrlKey||ev.metaKey||ev.shiftKey||ev.altKey)return;ev.preventDefault();showPhoto(i);showViewer(a,false)}));
document.querySelectorAll('[data-film]').forEach(a=>a.addEventListener('click',ev=>{if(ev.ctrlKey||ev.metaKey||ev.shiftKey||ev.altKey)return;ev.preventDefault();content.replaceChildren(embed(a.dataset.film,a.dataset.title));caption.textContent=a.dataset.title;viewer.setAttribute('aria-label','Film: '+a.dataset.title);showViewer(a,true)}));
document.querySelectorAll('[data-inline-film]').forEach(b=>b.addEventListener('click',()=>{b.replaceWith(embed(b.dataset.inlineFilm,b.dataset.title))}));
document.querySelector('#photo-prev')?.addEventListener('click',()=>showPhoto(photoIndex-1));
document.querySelector('#photo-next')?.addEventListener('click',()=>showPhoto(photoIndex+1));
viewer?.addEventListener('keydown',ev=>{if(viewer.classList.contains('is-film'))return;if(ev.key==='ArrowRight'){ev.preventDefault();showPhoto(photoIndex+1)}if(ev.key==='ArrowLeft'){ev.preventDefault();showPhoto(photoIndex-1)}});
viewer?.addEventListener('close',()=>{content.replaceChildren();lastTrigger?.focus();backgrounds.filter(v=>v.dataset.visible==='true'&&v.dataset.userPaused!=='true'&&!reduced.matches&&!saveData).forEach(v=>v.play().catch(()=>{}))});
