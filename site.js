const menu=document.querySelector('#menu');
const nav=document.querySelector('nav');
menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open))});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}));
if(document.body.classList.contains('home-page')){
 const onScroll=()=>{document.body.classList.toggle('scrolled',window.scrollY>window.innerHeight*.75);if(window.scrollY<=window.innerHeight*.75){nav.classList.remove('open');menu.setAttribute('aria-expanded','false')}};
 window.addEventListener('scroll',onScroll,{passive:true});onScroll();
 const hero=document.querySelector('#hero-video');
 const mobileHero=window.matchMedia('(max-width: 600px)');
 const hevcSource=hero?.querySelector('source[data-quality="hevc"]')?.getAttribute('src');
 const h264Source=hero?.querySelector('source[data-quality="h264"]')?.getAttribute('src');
 const mobileSource=hero?.dataset.mobileSrc;
 const hevcSupported=!!hero?.canPlayType('video/mp4; codecs="hvc1"');
 const useHeroSource=src=>{
  if(!hero||!src||hero.dataset.activeSrc===src)return;
  hero.dataset.activeSrc=src;
  hero.src=src;
  hero.load();
  hero.play().catch(()=>{});
 };
 const applyHeroSource=()=>{
  if(!hero)return;
  useHeroSource(mobileHero.matches?mobileSource:(hevcSupported?hevcSource:h264Source));
 };
 hero?.addEventListener('error',()=>{
  if(hero.dataset.activeSrc===hevcSource)useHeroSource(h264Source);
  else if(hero.dataset.activeSrc===mobileSource)useHeroSource(h264Source);
 });
 applyHeroSource();
 mobileHero.addEventListener('change',applyHeroSource);
 const storyScenes=[...document.querySelectorAll('.story-scene')];
 if(storyScenes.length && 'IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){
  document.body.classList.add('story-enhanced');
  const storyObserver=new IntersectionObserver(entries=>{
   entries.forEach(({target,isIntersecting})=>{
    const video=target.querySelector('video');
    if(isIntersecting){
     target.classList.add('is-visible');
     video.play().catch(()=>{});
    }else video.pause();
   });
  },{threshold:.12,rootMargin:'0px 0px -5% 0px'});
  storyScenes.forEach(scene=>storyObserver.observe(scene));
 }
}
document.addEventListener('click',event=>{
 const button=event.target.closest('.sound-toggle');
 if(!button||button.disabled)return;
 const video=button.parentElement.querySelector('video');
 if(!video)return;
 const turnOn=video.muted;
 document.querySelectorAll('.sound-toggle:not(:disabled)').forEach(other=>{
  const otherVideo=other.parentElement.querySelector('video');
  if(!otherVideo)return;
  otherVideo.muted=true;
  other.setAttribute('aria-pressed','false');
  other.textContent='Sound on';
  other.setAttribute('aria-label','Turn sound on for '+otherVideo.getAttribute('aria-label'));
 });
 if(turnOn){
  video.volume=.8;
  video.muted=false;
  video.play().catch(()=>{});
  button.setAttribute('aria-pressed','true');
  button.textContent='Sound off';
  button.setAttribute('aria-label','Turn sound off for '+video.getAttribute('aria-label'));
 }
});
if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
 document.querySelectorAll('video[autoplay]').forEach(video=>video.pause());
}
const projectDialog=document.querySelector('.project-story-dialog');
if(projectDialog){
 const dialogMedia=projectDialog.querySelector('.project-dialog-media');
 const dialogCopy=projectDialog.querySelector('.project-dialog-copy');
 const dialogGallery=projectDialog.querySelector('.project-dialog-gallery>div');
 let lastProjectTrigger=null;
 const clearProjectDialog=()=>{
  dialogMedia.querySelectorAll('video').forEach(video=>video.pause());
  dialogMedia.replaceChildren();
  dialogGallery.replaceChildren();
  document.body.classList.remove('project-dialog-open');
  if(lastProjectTrigger?.isConnected)lastProjectTrigger.focus();
 };
 projectDialog.querySelector('.project-dialog-close').addEventListener('click',()=>projectDialog.close());
 projectDialog.addEventListener('close',clearProjectDialog);
 projectDialog.addEventListener('click',event=>{if(event.target===projectDialog)projectDialog.close()});
 document.querySelectorAll('.project-open-story').forEach(button=>button.addEventListener('click',()=>{
  const card=button.closest('.project-entry,.project-footage-card,.project-poster');
  if(!card)return;
  const copy=card.querySelector('.project-copy')||card;
  const title=copy.querySelector('h2,h3');
  const label=copy.querySelector('small');
  const paragraphs=[...copy.querySelectorAll('p')].filter(p=>!p.classList.contains('project-credit'));
  const credit=copy.querySelector('.project-credit');
  dialogCopy.querySelector('small').textContent=label?.textContent||'THE DREAMER / PROJECT';
  dialogCopy.querySelector('h2').textContent=title?.textContent||'Project story';
  dialogCopy.querySelector('p').textContent=paragraphs.map(p=>p.textContent.trim()).filter(Boolean).join(' ');
  dialogCopy.querySelector('.project-dialog-credit').textContent=credit?.textContent||'';
  const media=card.querySelector('.project-media,.project-footage-player,.project-poster-media');
  if(media){
   const clone=media.cloneNode(true);
   clone.querySelectorAll('video').forEach(video=>{video.preload='metadata';video.controls=true;video.autoplay=false});
   clone.querySelectorAll('iframe').forEach(frame=>{frame.loading='eager';frame.src=frame.src.replace('?rel=0','?rel=0&playsinline=1')});
   dialogMedia.append(clone);
  }
  let stills=[...(card.querySelector('.project-related-gallery')?.querySelectorAll('figure')||[])];
  if(!stills.length){
   const image=card.querySelector('.project-poster-media img,.project-footage-player video[poster],.project-media img');
   if(image){
    const src=image.tagName==='VIDEO'?image.poster:image.currentSrc||image.src;
    const alt=image.tagName==='VIDEO'?image.getAttribute('aria-label')+' still':image.alt;
    stills=[{dataset:{},querySelector:()=>null,_src:src,_alt:alt}];
   }else{
    const frame=card.querySelector('.project-media iframe');
    const match=frame?.src.match(/embed\/([^?]+)/);
    if(match)stills=[{dataset:{},querySelector:()=>null,_src:'https://i.ytimg.com/vi/'+match[1]+'/hqdefault.jpg',_alt:(title?.textContent||'Project')+' film still'}];
   }
  }
  stills.forEach(still=>{
   const original=still.querySelector('img');
   const figure=document.createElement('figure');
   const image=document.createElement('img');
   image.src=still._src||original?.currentSrc||original?.src||'';
   image.alt=still._alt||original?.alt||'';
   image.loading='eager';
   figure.append(image);
   const caption=still.querySelector('figcaption');
   const text=caption?.textContent.trim();
   if(text){const figcaption=document.createElement('figcaption');figcaption.textContent=text;figure.append(figcaption)}
   dialogGallery.append(figure);
  });
  lastProjectTrigger=button;
  document.querySelectorAll('.project-entry video,.project-footage-card video').forEach(video=>video.pause());
  document.body.classList.add('project-dialog-open');
  projectDialog.showModal();
  projectDialog.querySelector('.project-dialog-close').focus();
 }));
}

document.querySelectorAll('.background-sound-toggle').forEach(button=>{
 const media=document.querySelector(button.dataset.backgroundSound||'');
 if(!media)return;
 let soundOn=false;
 const update=()=>{
  button.textContent=soundOn?'Sound on · mute':'Enable sound';
  button.setAttribute('aria-pressed',String(soundOn));
 };
 button.addEventListener('click',()=>{
  soundOn=!soundOn;
  if(media.tagName==='IFRAME'){
   const command=func=>media.contentWindow.postMessage(JSON.stringify({event:'command',func,args:[]}),'*');
   command('playVideo');
   command(soundOn?'unMute':'mute');
   update();
   return;
  }
  media.muted=!soundOn;
  update();
  if(soundOn)media.play().catch(()=>{
   soundOn=false;media.muted=true;update();
  });
 });
 update();
});

const inquiryForm=document.querySelector('.contact-form');
if(inquiryForm){
 inquiryForm.addEventListener('submit',event=>{
  event.preventDefault();
  if(!inquiryForm.reportValidity())return;
  const recipient=inquiryForm.dataset.recipient;
  if(!recipient)return;
  const fields=new FormData(inquiryForm);
  const subject='The Dreamer inquiry — '+fields.get('topic');
  const body=`Name: ${fields.get('name')}\nEmail: ${fields.get('email')}\nTopic: ${fields.get('topic')}\n\n${fields.get('message')}`;
  window.location.href=`mailto:${recipient}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  inquiryForm.querySelector('.contact-form-status').textContent='Your email app should open with the message ready to send.';
 });
}

const printDialog=document.querySelector('.print-shop-dialog');
if(printDialog){
 const cards=[...document.querySelectorAll('.print-shop-card')];
 let printTrigger;
 document.querySelectorAll('[data-print-filter]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-print-filter]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const category=button.dataset.printFilter;
  cards.forEach(card=>{card.hidden=category!=='All'&&card.dataset.printCategory!==category});
 }));
 document.querySelectorAll('.print-shop-open').forEach(button=>button.addEventListener('click',()=>{
  const card=button.closest('.print-shop-card');
  const image=card.querySelector('img');
  const dialogImage=printDialog.querySelector('.print-shop-dialog-image img');
  dialogImage.src=image.src;
  dialogImage.alt=image.alt;
  printDialog.querySelector('h2').textContent=card.querySelector('strong').textContent;
  printDialog.querySelector('.print-shop-dialog-category').textContent=card.dataset.printCategory.toUpperCase()+' / PHOTOGRAPHY';
  printDialog.querySelector('.print-shop-dialog-description').textContent=card.querySelector('p').textContent;
  printDialog.querySelector('.print-shop-dialog-price').textContent=card.dataset.printPrice+' · test price';
  printTrigger=button;
  printDialog.showModal();
  printDialog.querySelector('.print-shop-close').focus();
 }));
 printDialog.querySelector('.print-shop-close').addEventListener('click',()=>printDialog.close());
 printDialog.addEventListener('click',event=>{if(event.target===printDialog)printDialog.close()});
 printDialog.addEventListener('close',()=>printTrigger?.focus());
}
