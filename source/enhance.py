from html import escape as e

YT='https://www.youtube.com/@thedreamerwildandfree'
POD='https://youtu.be/AcNYeD8vvbw'
ARAB='https://www.arabnews.fr/node/194521/culture'
TUNIS='https://www.youtube.com/watch?v=OtJVufo3IrA'
def a(url,label):
 return f'<a class="text-link" href="{e(url,quote=True)}" {"target=_blank rel=noopener" if url.startswith("http") else ""}>{e(label)} <span aria-hidden="true">↗</span></a>'
def still(n,title,description='',shape=''):
 return f'<figure class="film-still {shape}"><img src="/assets/frames/tunisia-{n:02}.jpg" loading="lazy" alt="{e(description or title)}"><figcaption><small>THE DREAMER / TUNISIA FILM</small><strong>{e(title)}</strong><span>{e(description or "Film frame, Tunisia")}</span></figcaption></figure>'
def player(id,title):
 return f'<div class="cinema-player"><iframe title="{e(title)}" loading="lazy" src="https://www.youtube-nocookie.com/embed/{id}?autoplay=1&amp;mute=1&amp;playsinline=1&amp;loop=1&amp;playlist={id}&amp;rel=0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
def home_video(id,title,category):
 return f'<article class="home-film"><div class="home-film-frame"><iframe title="{e(title)}" loading="lazy" src="https://www.youtube-nocookie.com/embed/{id}?playsinline=1&amp;rel=0&amp;modestbranding=1&amp;vq=hd1080" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div><small>{e(category)}</small><h3>{e(title)}</h3></article>'
def head(n,title,desc=''):
 backgrounds={
  '01':'/assets/frames/tunisia-03.jpg',
  '04':'/assets/about/09.jpg',
  '06':'/assets/about/07.jpg',
  '07':'/assets/photography/469728961.jpg',
  '08':'/assets/about/01.jpg',
 }
 image=backgrounds.get(n[:2],'/assets/frames/tunisia-02.jpg')
 media=f'<img class="cinema-head-image" src="{image}" alt="" aria-hidden="true" fetchpriority="high">'
 if n.startswith('01 / DOCUMENTARIES'):
  media='<img class="cinema-head-image" src="/assets/documentaries-poster.jpg" alt="" aria-hidden="true" fetchpriority="high"><video class="cinema-head-video" autoplay muted loop playsinline preload="metadata" poster="/assets/documentaries-poster.jpg" aria-hidden="true" tabindex="-1"><source src="/assets/documentaries-hero.mp4" type="video/mp4"></video>'
 if n.startswith('04 / PROJECTS'):
  media='<img class="cinema-head-image" src="/assets/projects/community-field.jpg" alt="" aria-hidden="true" fetchpriority="high"><video class="cinema-head-video project-head-video" autoplay muted loop playsinline preload="metadata" poster="/assets/projects/community-field.jpg" aria-label="Land Rover driving across a Tunisian landscape" aria-hidden="true" tabindex="-1" data-background-audio><source src="/assets/projects/community-field.mp4" type="video/mp4"></video>'
 if n.startswith('06 / SPEAKING'):
  media='<iframe class="speaking-head-iframe speaking-head-bg-iframe" title="Rabii Ben Brahim speaking on Radio Cap FM" loading="eager" src="https://www.youtube-nocookie.com/embed/5ZJtvU-VOjw?autoplay=1&amp;mute=1&amp;controls=0&amp;playsinline=1&amp;loop=1&amp;playlist=5ZJtvU-VOjw&amp;rel=0&amp;modestbranding=1&amp;enablejsapi=1&amp;origin=https%3A%2F%2Fthe-dreamer-cinematic-preview.dhiamahouachi115.chatgpt.site" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen aria-hidden="true" tabindex="-1"></iframe>'
 head_class='cinema-head project-head' if n.startswith('04 / PROJECTS') else ('cinema-head speaking-head' if n.startswith('06 / SPEAKING') else 'cinema-head')
 sound_button='<button class="background-sound-toggle" type="button" data-background-sound=".project-head-video" aria-pressed="false">Enable sound</button>' if n.startswith('04 / PROJECTS') else ('<button class="background-sound-toggle speaking-background-sound" type="button" data-background-sound=".speaking-head-bg-iframe" aria-pressed="false">Enable sound</button>' if n.startswith('06 / SPEAKING') else '')
 return f'<section class="{head_class}">{media}<div class="cinema-head-shade"></div>{sound_button}<div class="cinema-head-copy"><small>{e(n)}</small><h1>{e(title)}</h1>{f"<p>{e(desc)}</p>" if desc else ""}</div></section>'
def editorial(n,title,body):
 return f'<section class="cinema-section"><small>{e(n)}</small><div><h2>{e(title)}</h2>{body}</div></section>'
def spread(items,extra=''):
 return '<div class="frame-spread '+extra+'">'+''.join(still(*it) for it in items)+'</div>'
def filmcase(label,title,copy,video_id,source):
 return f'<article class="film-case"><div class="case-media">{player(video_id,title)}</div><div class="case-text"><small>{e(label)}</small><h2>{e(title)}</h2><p>{e(copy)}</p>{a(source,"Film and credits")}</div></article>'
def note():
 return '<p class="asset-note">Tunisia images on this page are frames from The Dreamer film supplied for this preview. They are not standalone photographs, partner campaign images or prints. Original photography and rights-specific captions will be added from the approved archive.</p>'
def write(slug,title,body):
 (p/slug/'index.html').write_text(doc(title,body)) if slug else (p/'index.html').write_text(doc(title,body))

home = f'''<section class="cinema-hero"><video id="hero-video" autoplay muted loop playsinline preload="metadata" poster="/assets/hero-new/poster.webp" aria-label="The Dreamer’s cinematic film of Tunisia" data-mobile-src="/assets/hero-new/landing-bg-mobile.mp4"><source src="/assets/hero-new/landing-bg-hevc.mp4" data-quality="hevc" type='video/mp4; codecs="hvc1"'><source src="/assets/hero-new/landing-bg.mp4" data-quality="h264" type="video/mp4"></video><div class="hero-tint"></div><a class="scroll-hint" href="#home-title">SCROLL TO EXPLORE ↓</a></section><section class="home-title" id="home-title"><div><small>THE DREAMER / RABII BEN BRAHIM</small><h1>Wild.<br>And free.</h1></div><a href="https://www.youtube.com/watch?v=OtJVufo3IrA" target="_blank" rel="noopener">WATCH THE FILM <span aria-hidden="true">↗</span></a></section>'''
def story_scene(number, label, headline, body, clip, still, still_alt, still_label):
 return f'''<article class="story-scene"><figure class="story-media story-primary"><video muted loop playsinline preload="none" poster="/assets/story/{clip}.jpg" aria-hidden="true"><source src="/assets/story/{clip}.mp4" type="video/mp4"></video><figcaption>{e(number)} / MOVING IMAGE</figcaption></figure><div class="story-scene-copy"><small>{e(number)} / {e(label)}</small><h2>{e(headline)}</h2><p>{e(body)}</p></div><figure class="story-media story-secondary"><img src="{still}" alt="{e(still_alt)}" loading="lazy"><figcaption>{e(still_label)}</figcaption></figure></article>'''

home += '<section class="story-sequence" aria-label="A journey through The Dreamer’s work"><div class="story-sequence-intro"><span>THE DREAMER / A STORY IN THREE SCENES</span><span>SCROLL TO FOLLOW THE JOURNEY ↓</span></div>'
home += story_scene('01','THE ROAD','Go where the story begins.','Across open ground, the camera follows a journey shaped by curiosity and the freedom to keep moving.','desert-road','/assets/about/09.jpg','Rabii seated beside a vehicle, looking across a landscape','THE JOURNEY')
home += story_scene('02','THE LIVING WORLD','Then look closer.','The smallest lives reveal a world of movement, colour and detail worth seeing.','field-life','/assets/photography/556922215.jpg','Small owl looking out from a rocky hollow','THE WILD')
home += story_scene('03','THE SEA','Follow what connects us.','From the land to the water, the journey turns toward the places and lives held together by the coast.','sea-journey','/assets/photography/526506341.jpg','Rocky coastline and clear turquoise water seen from above','THE COAST')
home += '<div class="story-sequence-outro"><span>THREE GLIMPSES. MANY STORIES STILL TO TELL.</span>'+a('/about/','Meet the Dreamer')+'</div></section>'
home += '<section class="home-panorama" id="home-panorama"><aside class="home-story-copy"><small>A LIFE IN THE FIELD / TUNISIA</small><h2>Look closer.<br>Go further.</h2><p>Follow Rabii through wild places, open landscapes and the stories that connect them.</p>'+a('/about/','Meet the Dreamer')+a('/conservation/','Explore Impact')+'</aside><div class="home-panorama-grid"><figure><video autoplay muted loop playsinline preload="metadata" poster="/assets/frames/tunisia-02.jpg" aria-label="Wide view across Tunisia"><source src="/assets/hero-full/part-02.mp4" type="video/mp4"></video><figcaption><small>01 / THE LAND</small></figcaption></figure><figure><video autoplay muted loop playsinline preload="metadata" poster="/assets/frames/tunisia-06.jpg" aria-label="Historic place among the Tunisian landscape"><source src="/assets/hero-full/part-04.mp4" type="video/mp4"></video><figcaption><small>02 / PEOPLE &amp; PLACE</small></figcaption></figure><figure><video autoplay muted loop playsinline preload="metadata" poster="/assets/frames/tunisia-09.jpg" aria-label="Coastline in Tunisia"><source src="/assets/hero-full/part-05.mp4" type="video/mp4"></video><figcaption><small>03 / THE COAST</small></figcaption></figure></div></section>'
home += '<section class="home-gallery" id="home-gallery"><div class="home-gallery-layout"><aside class="home-gallery-copy"><small>THE DREAMER / FIELD ARCHIVE</small><h2>Twenty moments.<br>One wild world.</h2><p>Move over a frame to pause on a small story from the field.</p>'+a('/photography/','Explore all photography')+'</aside><div class="home-cube-grid">'

films=head('01 / DOCUMENTARIES','Stories in motion.','Films about nature, Tunisia and the people whose lives are tied to place.')
films+=filmcase('DOCUMENTARY / TUNISIA','Wildlife Wonders','Rabii describes working with ecologist Zakher Bouragaoui within the Tunisian Wonders initiative.','oBRHiGLC0S4',S['wildlife'])
films+='''<section class="documentary-sequence" aria-labelledby="documentary-sequence-title"><div class="documentary-sequence-heading"><small>THE DREAMER / FIELD NOTES</small><div><h2 id="documentary-sequence-title">The story keeps moving.</h2><p>Two glimpses from Rabii’s Tunisia film: the restless coastline and a path through the trees. The landscape becomes part of the story when the camera stays with it.</p></div></div><div class="documentary-sequence-grid"><figure class="documentary-sequence-frame"><video autoplay muted loop playsinline preload="metadata" poster="/assets/frames/tunisia-09.jpg" aria-label="Moving aerial footage of Tunisia’s coastline from The Dreamer’s Tunisia film"><source src="/assets/hero-full/part-06.mp4" type="video/mp4"></video><figcaption><small>01 / AT THE WATER’S EDGE</small><strong>Where land meets water.</strong></figcaption><span class="documentary-sequence-progress" aria-hidden="true"></span></figure><figure class="documentary-sequence-frame"><video autoplay muted loop playsinline preload="metadata" poster="/assets/frames/tunisia-01.jpg" aria-label="Moving aerial footage of a wooded path from The Dreamer’s Tunisia film"><source src="/assets/hero-full/part-07.mp4" type="video/mp4"></video><figcaption><small>02 / INTO THE GREEN</small><strong>Follow the quiet path.</strong></figcaption><span class="documentary-sequence-progress" aria-hidden="true"></span></figure></div><div class="documentary-sequence-footer"><span>EXCERPTS / THE DREAMER’S TUNISIA FILM</span>'''+a(TUNIS,'Watch the full film')+'</div></section>'
films+=filmcase('DOCUMENTARY / WWF','Blue Future','A collective documentary about Mediterranean livelihoods. WWF credits Rabii Ben Brahim alongside Ante Gugić, Emanuele Quartarone and Beatrice Surano.','OyaSu8oF-D8',S['blue'])
travel=[('Tunisia','OtJVufo3IrA','A cinematic journey across Tunisia.',TUNIS),('Bizerte','uyeXpLjqgxw','A visual exploration of Bizerte.','https://www.youtube.com/watch?v=uyeXpLjqgxw'),('El Kef','xKpNfEQQrWE','A film connected to place and sustainable tourism.','https://www.youtube.com/watch?v=xKpNfEQQrWE'),('Torda','7ftfKXuN38o','A field film connected to biodiversity.','https://www.youtube.com/watch?v=7ftfKXuN38o')]
films+=editorial('FIELD FILMS','Tunisia, seen differently.','<div class="film-grid">'+''.join(f'<article>{player(v,t)}<h3>{t}</h3><p>{d}</p>{a(u,"Watch original")}</article>' for t,v,d,u in travel)+'</div>')+note()
write('films','Documentaries',films)

photos={
 'open_plain':[
  ('645836414','Last light over the herd','The last light of day settles behind the elephants, turning the open plain gold.','wide','Elephants silhouetted at sunset'),
  ('650871801','A closer look','One elephant stands forward while the rest of the herd moves through the green.','tall','Elephant standing in front of its herd'),
  ('649232440','The sun between them','A quiet pause in the warm light as the herd crosses the horizon.','wide','Elephants crossing a sunset'),
  ('650643519','Under a changing sky','A family group moves across the plain beneath a wide, clouded sky.','square','Elephant family on open grassland'),
  ('653507443','The long walk','A young elephant follows the path across open ground.','tall','Young elephant walking across grassland'),
 ],
 'faces':[
  ('469728961','A face in the grass','A close portrait catches the strength and stillness in a wild face.','wide','Close portrait of a large wild cat'),
  ('469683747','A breath in the open air','A yawn becomes a moment of expression, framed against the soft green behind it.','tall','Wild cat with its mouth open'),
  ('469825933','Together','Two animals rest close, a small gesture of care in a quiet moment.','square','Two wild cats close together'),
  ('469728510','In monochrome','Without colour, attention shifts to the gaze, texture and shape of the animal.','tall','Black and white portrait of a wild cat'),
 ],
 'small_worlds':[
  ('555630946','On the warm stone','A small reptile pauses on sunlit rock, almost disappearing into the earth tones.','wide','Small reptile resting on a sunlit rock'),
  ('555826408','A flash of green','Bright scales stand out against rough stone and dry ground.','tall','Green lizard on a rocky surface'),
  ('684847033','At the edge of a leaf','A tiny subject rests along the clean curve of a vivid green leaf.','square','Small creature on a green leaf'),
  ('686509758','A world in miniature','A close study of a tiny animal against the soft green of its habitat.','tall','Macro photograph of a small animal on a leaf'),
  ('689096947','Climbing into view','A delicate subject climbs along a leaf, framed against deep shadow.','square','Small animal climbing a leaf'),
 ],
 'wings_watchers':[
  ('556626056','Eyes above the rocks','An owl watches from its sheltered perch, almost blending into the stone.','tall','Owl perched among rocks'),
  ('556922215','A sheltered pair','Two young owls sit close together in the shade of a rocky hollow.','wide','Two owls inside a rocky shelter'),
  ('557438021','Through the branches','A bird holds still among fine branches while the background falls away.','square','Bird perched among branches'),
  ('700708021','Into the blue','A flash of colour crosses the green as a bird flies past.','wide','Blue and orange bird in flight'),
  ('654066053','A call in the wild','A powerful open-mouth portrait catches a moment of sound and movement.','tall','Wildlife portrait with mouth open'),
  ('556799051','Moments from the field','A composite frame gathers several encounters from the wider wildlife archive.','square','Collage of wildlife field moments'),
 ],
 'coast_and_water':[
  ('526215548','Where the rock meets the sea','Clear blue water wraps around a layered headland, revealing the shoreline below the surface.','wide','Layered rocky coastline above clear turquoise water'),
  ('526763980','A boat between worlds','An aerial view holds a small boat between the dark depths and the bright shallows.','tall','Small boat on the boundary between dark and shallow water'),
  ('526594784','One quiet crossing','A single kayak leaves a fine line across a wide field of deep blue water.','wide','Kayak seen from above in dark blue water'),
  ('525755603','The coast opens out','Cliffs and clear water stretch toward the horizon in a quiet sweep of blue.','tall','High coastal cliffs above the Mediterranean Sea'),
  ('526506341','A hidden cove','The aerial view reveals a small cove tucked between pale rock and open water.','wide','Aerial view of a Mediterranean cove'),
  ('526744379','Coastline in three frames','A small sequence of views follows the coast from the clear shallows to the rocky headland.','wide','Three views of the Mediterranean coastline'),
  ('526294068','A line along the shore','From above, the shoreline brings together pale rock, sea and a small beach.','square','Aerial view of a rocky coast and beach'),
  ('527055566','Alone on the water','A lone kayak sits against the vast dark blue sea, seen from high above.','tall','Single kayak on deep blue water seen from above'),
 ],
 'field_observers':[
  ('526285315','Behind the lens','A photographer pauses in silhouette, looking out across the landscape.','tall','Silhouette of a photographer holding a camera'),
  ('573830916','A field day in focus','A sequence of moments shows the patience and equipment behind a day spent watching wildlife.','wide','Wildlife photographer using binoculars and camera in the field'),
 ],
 'wild_encounters':[
  ('525861371','Drifting in blue','Jellyfish move through clear water, light passing softly through their bells.','wide','Two jellyfish drifting underwater'),
  ('526130764','A patient perch','A small raptor rests on a weathered post, alert above the green.','tall','Small bird of prey perched on a stone post'),
  ('527337330','At the water’s edge','A black-winged stilt steps carefully through the shallows.','wide','Black-winged stilt standing in shallow water'),
  ('573570378','A quiet rest','A leopard rests with eyes half closed, its patterned coat echoing the dappled light.','tall','Leopard resting on a tree branch'),
  ('573551598','A flash of blue','A blue bird pauses above the water while a crocodile rests below.','square','Blue bird perched above a crocodile'),
  ('575191913','Small details, bright colours','Close portraits catch the bold patterns and bright colours of birds in the field.','wide','Close-up portraits of colourful birds'),
 ],
 'flight_and_wetlands':[
  ('573688673','Resting in the canopy','A leopard settles among branches, sheltered by the leaves.','wide','Leopard resting in a leafy tree'),
  ('821441541','Across the open sky','A bird cuts across a pale sky with its wings extended.','tall','Bird in flight across a clear sky'),
  ('817329413','Wings over water','A dark waterbird glides above the wetland, reflected in the open blue.','wide','Waterbird flying over a wetland'),
  ('810813870','A nest among the reeds','A bird settles among the reeds beside its nest.','tall','Dark waterbird beside a nest in reeds'),
 ],
 'people_and_place':[
  ('655487978','At the blue doorway','Rabii pauses in the shade of a bright blue doorway.','tall','Rabii wearing a straw hat beside a blue doorway'),
  ('652760438','Under the palms','A quiet moment beneath the palms, with woven fronds filtering the light.','wide','Man seated beneath palm trees in a woven shade shelter'),
  ('655081329','A face in the sun','A close portrait in the open air, framed by blue sky and sea.','tall','Portrait of Rabii wearing a straw hat beside the sea'),
  ('651921257','A catch from the water','A fisherman holds up a crab beside the open sea.','wide','Fisherman holding a crab on a boat beside the sea'),
  ('650345189','The morning catch','A market display gathers the day’s fish, fresh from the water.','tall','Fresh fish arranged at a local market'),
  ('651876653','From sea to table','A cooked fish is served simply with lemon.','tall','Cooked fish with lemon on a plate'),
  ('645712006','A meal in the shade','A shared meal beneath the broad shade of an old tree.','wide','Man eating beneath a large tree'),
  ('651451626','A conversation by the blue doors','Two people talk in the cool shade of a whitewashed island house.','tall','Two people seated beside bright blue doors'),
  ('651912908','Out on the water','A fisherman works from a small boat along the coast.','tall','Fisherman seated on a blue boat at sea'),
  ('653587851','The working coast','A fisherman tends his nets beneath the old branches.','tall','Fisherman beside fishing nets under a tree'),
 ],
 'wings_in_flight':[
  ('731067983','Against the open sky','A bird glides across a pale, open sky.','wide','Bird in flight across a pale blue sky'),
  ('731158290','A flash of colour','Bright feathers catch the light as a bird passes overhead.','wide','Colourful bird in flight against a blue sky'),
 ]
}
def photo_card(item,index):
 name,title,story,shape,alt=item
 return f'<figure class="photo-card {shape}" tabindex="0"><img src="/assets/photography/{name}.jpg" loading="lazy" alt="{e(alt)}"><figcaption><small>PHOTO STORY / {index:02}</small><h3>{e(title)}</h3><p>{e(story)}</p><a href="{IG}" target="_blank" rel="noopener">Find the original story on Instagram ↗</a></figcaption></figure>'
old_home_photos=[item for chapter_items in list(photos.values())[:4] for item in chapter_items]
new_home_photos=[item for chapter_items in list(photos.values())[4:] for item in chapter_items]
home_photos=[item for pair in zip(old_home_photos[:10],new_home_photos[:10]) for item in pair]
home_photo_index=1
for item in home_photos:
  name,title,story,shape,alt=item
  home+=f'<figure class="home-cube-card" tabindex="0"><img src="/assets/photography/{name}.jpg" alt="{e(alt)}" loading="lazy"><figcaption><small>FIELD FRAME / {home_photo_index:02}</small><h3>{e(title)}</h3><p>{e(story)}</p></figcaption></figure>'
  home_photo_index+=1
home+='</div></div></section>'
home+='<section class="home-films"><div class="home-films-heading"><small>FILMS / WATCH ON YOUTUBE</small><h2>Stories in motion.</h2></div><div class="home-film-grid">'+home_video('oBRHiGLC0S4','Wildlife Wonders','TUNISIA / CONSERVATION')+home_video('OyaSu8oF-D8','Blue Future','MEDITERRANEAN / SUSTAINABLE FUTURES')+'</div></section>'
collaborators=[
 ('Land Rover Tunisia','https://www.linkedin.com/posts/rabii-ben-brahim-007309141_the-new-land-rover-defender-activity-6783114169421045760-o5vA'),
 ('Alpha International','https://www.linkedin.com/posts/rabii-ben-brahim-007309141_the-new-land-rover-defender-activity-6783114169421045760-o5vA'),
 ('YKONE Tunis','https://ykone.com/portfolio/landrover-defender/'),
 ('WWF × COGITO','https://www.wwf.it/area-stampa/blue-future-il-documentario-wwf-sui-lavori-blu/'),
 ('National Geographic','https://www.linkedin.com/posts/rabii-ben-brahim-007309141_wildlife-wonders-activity-7311423928600596482-iWgy'),
 ('Tunisian Wonders','https://www.linkedin.com/posts/rabii-ben-brahim-007309141_wildlife-wonders-activity-7311423928600596482-iWgy'),
 ('Tunisie Telecom','https://www.linkedin.com/in/rabii-ben-brahim-007309141'),
 ('Zakher Bouragaoui','https://www.linkedin.com/posts/rabii-ben-brahim-007309141_wildlife-wonders-activity-7311423928600596482-iWgy'),
]
home+='<section class="home-collaborators"><div class="collaborator-heading"><small>SELECTED COLLABORATIONS</small>'+a('/collaborations/','See the projects')+'</div><div class="collaborator-list">'+''.join(f'<a href="{e(url,quote=True)}" target="_blank" rel="noopener">{e(name)} <span aria-hidden="true">↗</span></a>' for name,url in collaborators)+'</div></section>'
home+='<section class="home-end"><small>KEEP LOOKING CLOSER</small><h2>There’s always another story.</h2><div>'+a('/collaborations/','Explore projects')+a('/contact/','Start a conversation')+'</div></section>'
write('', 'Home', home)
photo='<section class="photography-opening"><img class="photography-opening-backdrop" src="/assets/photography/526215548.jpg" alt="" aria-hidden="true"><img class="photography-opening-image" src="/assets/photography/526215548.jpg" alt="Rocky Tunisian coastline meeting turquoise water" fetchpriority="high"><div class="photography-opening-shade"></div><div class="photography-opening-copy"><small>THE DREAMER / PHOTOGRAPHY</small><h1>Look closer.</h1><p>Wildlife, people and places held in a single frame.</p></div><a class="photo-scroll" href="#photo-stories">SCROLL TO EXPLORE ↓</a></section>'
photo+='<section class="photography-intro" id="photo-stories"><small>FIFTY TWO FRAMES / TEN CHAPTERS</small><p>Each photograph is a moment to pause, notice the detail and imagine what happened just beyond the frame.</p><span>Hover or focus a photograph to read its story.</span></section>'
photo_index=1
for chapter,title,dek in [
 ('open_plain','01 / THE OPEN PLAIN','Movement, distance and the last light of day.'),
 ('faces','02 / FACES IN THE WILD','Expression, closeness and the quiet between movements.'),
 ('small_worlds','03 / SMALL WORLDS','The details that reward a slower look.'),
 ('wings_watchers','04 / WINGS & WATCHERS','A flash of flight, a patient gaze, a sheltered moment.'),
 ('coast_and_water','05 / COAST & WATER','Wide horizons, hidden coves and the quiet patterns of the sea.'),
 ('field_observers','06 / BEHIND THE LENS','The patience and perspective that go into a day in the field.'),
 ('wild_encounters','07 / WILD ENCOUNTERS','Close encounters with wildlife, from the shoreline to the canopy.'),
 ('flight_and_wetlands','08 / FLIGHT & WETLANDS','Birdlife in motion and the sheltered places that sustain it.'),
 ('people_and_place','09 / PEOPLE & PLACE','Portraits and everyday moments along Tunisia’s coast.'),
 ('wings_in_flight','10 / WINGS IN FLIGHT','A pair of passing birds, framed against open sky.'),
]:
 photo+='<section class="photo-chapter"><header><small>'+e(title)+'</small><p>'+e(dek)+'</p></header><div class="photo-grid '+('photo-grid-'+chapter)+'">'+''.join(photo_card(item,i) for i,item in enumerate(photos[chapter],photo_index))+'</div></section>'
 photo_index+=len(photos[chapter])
photo+='<section class="photo-source"><div><small>MORE FROM THE DREAMER</small><h2>Follow the stories back to their source.</h2><p>The hover notes here are short visual stories. Open Instagram to read Rabii’s original post captions and see more from the archive.</p>'+a(IG,'Open The Dreamer on Instagram')+'</div></section>'
write('photography','Photography',photo)

PODCAST_EP='https://podcasts.apple.com/us/podcast/rabii-ben-brahim-%D8%A7%D9%84%D8%B7%D9%81%D9%84-%D8%A7%D9%84%D8%AF%D8%A7%D8%AE%D9%84%D9%8A-%D8%A7%D9%84%D8%B7%D8%A8%D9%8A%D8%B9%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D9%8A%D8%B4-%D8%A8%D8%A5%D9%85%D8%AA%D9%86%D8%A7%D9%86/id1553496708?i=1000642255921&l=ar'
GOOD_TUNISIA='https://www.youtube.com/watch?v=aBjmrxRNm0g'
WILDLIFE='https://www.youtube.com/watch?v=8dy7puUV0dg'
BLUE_CREDITS='https://www.wwf.it/area-stampa/blue-future-il-documentario-wwf-sui-lavori-blu/'
CINEMAJET='https://www.eumedbridge.eu/news/jet-cinema-2026-in-zaghouan-and-jendouba-cinema-comes-to-meet-territories-generations-and-imaginations/'
def impact_player(video_id,title):
 return f'<div class="cinema-player"><iframe title="{e(title)}" loading="lazy" src="https://www.youtube-nocookie.com/embed/{video_id}?rel=0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>'
def impact_feature(number,theme,title,copy,media,links):
 return f'<article class="impact-feature"><div class="impact-media">{media}</div><div class="impact-copy"><small>{e(number)} / {e(theme)}</small><h2>{e(title)}</h2>{copy}{links}</div></article>'
impact='<section class="impact-opening impact-video-opening"><img class="impact-opening-backdrop" src="/assets/impact/impact-opening.jpg" alt="" aria-hidden="true"><video class="impact-opening-video" autoplay muted loop playsinline preload="metadata" poster="/assets/impact/impact-opening.jpg" aria-label="Aerial view over Tunisia’s green landscape and communities" data-background-audio><source src="/assets/impact/impact-opening.mp4" type="video/mp4"></video><div class="impact-opening-shade"></div><div class="impact-opening-copy"><small>THE DREAMER / IMPACT</small><h1>See. Feel.<br>Protect.</h1><p>Field films and youth photography bring people closer to Tunisia’s landscapes, wildlife and communities.</p></div><button class="background-sound-toggle impact-background-sound" type="button" data-background-sound=".impact-opening-video" aria-pressed="false">Enable sound</button><span class="about-opening-index">TUNISIA / PEOPLE / NATURE</span></section>'
impact+='<section class="impact-manifesto"><small>LOOKING CLOSER</small><p>Conservation stories begin with attention: to living landscapes, to wildlife, and to the people who call a place home.</p></section>'
impact+='<article class="impact-feature impact-field-feature"><div class="impact-media impact-portrait-player"><video class="impact-stories-video" autoplay muted loop playsinline preload="metadata" poster="/assets/impact/field-mentoring.webp" aria-label="Wildlife, landscape and conversation clips supplied for The Dreamer"><source src="/assets/impact/field-stories.mp4" type="video/mp4"></video><button class="sound-toggle sound-unavailable" type="button" disabled aria-label="This supplied video has no audio track">No audio track</button></div><div class="impact-copy"><small>01 / FIELD &amp; COMMUNITY</small><h2>Stories bring us closer.</h2><p>Birdlife, coast and open landscapes sit alongside Rabii in conversation and young people looking through a camera. Together, the supplied clips show how visual storytelling can draw attention to both the natural world and the communities around it.</p></div></article>'
impact+='<section class="impact-field-context"><small>PEOPLE / PLACE / PERSPECTIVE</small><p>These photographs show a community film and photography activity, the young participants, and the process of making images in the field. They keep the story close to the people and places at its centre.</p></section><div class="impact-photo-ribbon impact-field-ribbon"><figure><img src="/assets/impact/cinemajet-program.webp" loading="lazy" alt="A collage of CinémaJet event artwork and a group taking part in an outdoor activity"><figcaption>Community activity / CinémaJet</figcaption></figure><figure><img src="/assets/impact/field-mentoring.webp" loading="lazy" alt="A collage of portraits of young participants"><figcaption>Young perspectives</figcaption></figure><figure><img src="/assets/impact/photography-workshop.webp" loading="lazy" alt="A collage of field photography moments with Rabii and young participants"><figcaption>Learning through the lens</figcaption></figure></div>'
def impact_supplied_clip(number,title,description,filename,poster,has_audio=True):
 audio_button=f'<button class="sound-toggle" type="button" aria-label="Turn sound on for {e(title)}" aria-pressed="false">Sound on</button>' if has_audio else '<button class="sound-toggle sound-unavailable" type="button" disabled aria-label="This supplied video has no audio track">No audio track</button>'
 return f'<article class="impact-supplied-card"><div class="impact-supplied-player"><video autoplay muted loop playsinline preload="metadata" poster="/assets/impact/{poster}" aria-label="{e(title)}"><source src="/assets/impact/{filename}" type="video/mp4"></video>{audio_button}</div><div><small>{e(number)} / FIELD STORY</small><h3>{e(title)}</h3><p>{e(description)}</p></div></article>'
impact+='<section class="impact-supplied-section"><div class="impact-supplied-grid">'
impact+=impact_supplied_clip('02','Life along the coast','A coastal scene invites a closer look at the pressures and life gathered at the water’s edge.','community-coast.mp4','community-coast-poster.webp',True)
impact+=impact_supplied_clip('03','The value of nature','A voice reflects on nature’s worth beyond monetary terms. This supplied clip has no embedded audio track.','nature-value.mp4','nature-value-poster.webp',False)
impact+='</div></section>'
impact+='<section class="impact-heritage"><div><small>THE WORK IN CONTEXT</small><h2>Nature. People. Place.</h2></div><div><p>The Dreamer’s environmental storytelling brings landscapes and wildlife into view while making room for the people who experience and care for them.</p>'+a('/photography/','Explore photography')+a('/collaborations/','Explore projects')+'</div></section>'
impact+='<section class="impact-closing"><small>KEEP LOOKING CLOSER</small><h2>Every place has a story worth protecting.</h2>'+a('/speaking/','Hear Rabii speak')+a('/contact/','Start a conversation')+'</section>'
write('conservation','Impact',impact)

def project_player(video_id,title):
 return f'<div class="cinema-player"><iframe title="{e(title)} film" loading="lazy" src="https://www.youtube-nocookie.com/embed/{video_id}?rel=0" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>'
def project_entry(number,kicker,title,description,credit,video_id,link,link_label='Watch the film'):
 return f'<article class="project-entry"><div class="project-media">{project_player(video_id,title)}</div><div class="project-copy"><small>{e(number)} / {e(kicker)}</small><h2>{e(title)}</h2><p>{e(description)}</p><p class="project-credit">{e(credit)}</p>{a(link,link_label)}<button class="project-open-story" type="button">Explore this project <span aria-hidden="true">↗</span></button></div></article>'
def poster_entry(kicker,title,description,credit,img,alt,link,label):
 return f'<article class="project-poster"><div class="project-poster-media"><img src="/assets/projects/{img}" alt="{e(alt)}" loading="lazy"></div><div class="project-copy"><small>{e(kicker)}</small><h2>{e(title)}</h2><p>{e(description)}</p><p class="project-credit">{e(credit)}</p>{a(link,label)}<button class="project-open-story" type="button">Explore this project <span aria-hidden="true">↗</span></button></div></article>'

projects=head('04 / PROJECTS','Stories made in the field.','Campaigns, documentaries, independent films and the collaborations that bring them to life.')
projects+='<div class="project-intro"><span>SELECTED WORK / 2021—2026</span><p>From the road to the sea, each film starts with a place and the people connected to it.</p></div>'
djerba_story='<article class="project-footage-card project-djerba-story" data-project-gallery><div class="project-footage-player project-djerba-player"><video controls playsinline preload="metadata" poster="/assets/projects/djerba/06-land-rover.webp" aria-label="Djerba — between sea and stone"><source src="/assets/projects/djerba/coastline.mp4" type="video/mp4"></video><button class="sound-toggle sound-unavailable" type="button" disabled aria-label="This supplied video has no audio track">No audio track</button></div><div class="project-copy"><small>NEW FIELD STORY / TUNISIA</small><h2>Djerba: between sea &amp; stone.</h2><p>A quiet look at the island’s coastline, whitewashed architecture and the people behind a filming day. Open the story to see Rabii on location, the crew at work and a short coastal film.</p><p class="project-credit">Field film and photographs supplied by The Dreamer</p><button class="project-open-story" type="button">Explore this project <span aria-hidden="true">↗</span></button></div><div class="project-related-gallery" hidden>'+''.join(f'<figure><img src="/assets/projects/djerba/{name}" alt="{e(alt)}" loading="lazy"><figcaption>{e(caption)}</figcaption></figure>' for name,alt,caption in [('01-seaside-portrait.webp','Rabii and a companion beside the blue sea','Along the coast'),('02-blue-door.webp','An old blue doorway in a pale stone arch','An old blue doorway'),('03-coastal-courtyard.webp','Whitewashed buildings and a dome under clear sky','Light on whitewashed walls'),('04-rabii-filming.webp','A camera operator films Rabii speaking outdoors','Behind the camera'),('05-interview.webp','A camera crew records an interview in a courtyard','Listening closely'),('06-land-rover.webp','A classic yellow Land Rover beside a white island house','The road vehicle'),('07-team.webp','The group rests together beside a whitewashed building','The people behind the frame'),('08-camera-and-guest.webp','A filmmaker takes a portrait beside a pale stone wall','A portrait in progress')])+'</div></article>'
def project_supplied_clip(number,title,description,name):
 return f'''<article class="project-footage-card"><div class="project-footage-player"><video autoplay muted loop controls playsinline preload="metadata" poster="/assets/projects/{name}.jpg" aria-label="{e(title)} video"><source src="/assets/projects/{name}.mp4" type="video/mp4">Your browser does not support this video.</video><button class="sound-toggle" type="button" aria-label="Turn sound on for {e(title)}" aria-pressed="false">Sound on</button></div><div><small>{e(number)} / FIELD FOOTAGE</small><h3>{e(title)}</h3><p>{e(description)}</p><button class="project-open-story" type="button">Explore this project <span aria-hidden="true">↗</span></button></div></article>'''
projects+='<section class="project-new-media" aria-label="More work in motion"><div class="project-new-heading"><small>FROM THE FIELD / NEW FOOTAGE</small><h2>More stories in motion.</h2><p>Coastlines, conversations, journeys and time spent in the field.</p></div><div class="project-footage-grid">'
projects+=project_supplied_clip('02','The Defender journey','A drive between the shore, the dunes and the open road.','defender-field')
projects+=djerba_story
projects+=project_supplied_clip('03','On the road','A moving view of coasts, landscapes and the places between them.','road-expedition')
projects+=project_supplied_clip('04','Coastal lives','Fishing scenes and local voices beside the water.','coastal-voices')
projects+='</div></section>'
projects+='<div class="project-field-heading project-community-heading"><small>BEYOND THE CAMERA</small><h2>On screen. In the community.</h2></div><div class="project-community-grid">'
def community_card(kicker,title,description,credit,image,alt,link,label,video_id=None):
 media=(f'<div class="project-poster-media"><iframe title="{e(title)}" loading="lazy" src="https://www.youtube-nocookie.com/embed/{video_id}?rel=0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>' if video_id else f'<div class="project-poster-media"><img src="/assets/projects/{image}" alt="{e(alt)}" loading="lazy"></div>')
 return f'<article class="project-poster project-community-card">{media}<div class="project-copy"><small>{e(kicker)}</small><h2>{e(title)}</h2><p>{e(description)}</p><p class="project-credit">{e(credit)}</p>{a(link,label)}<button class="project-open-story" type="button">Explore this project <span aria-hidden="true">↗</span></button></div></article>'
projects+=community_card('FILM APPEARANCE / 2024','Where Is Diana?','Rabii appears in this short film directed by Sami Chaffai. This is an acting credit, presented separately from the films he made.','Directed by Sami Chaffai · Featuring Rabii Ben Brahim','where-is-diana.jpg','Where Is Diana? film poster featuring the cast','https://www.imdb.com/title/tt35113069/','View film details')
projects+=community_card('COMMUNITY / 2026','CinémaJet','Rabii joined the festival’s photography program in Zaghouan, inviting participants to see the city through its residents.','CinémaJet · Zaghouan, Tunisia · Photography activity','cinemajet.jpg','CinémaJet festival graphic','https://www.facebook.com/cinematdour/posts/-cin%C3%A9-balade-avec-the-dreamer-cin%C3%A9majet-2%E1%B5%89-%C3%A9ditionce-jeudi-on-troque-la-salle-ob/122273262584089082/','View organizer update')
projects+=community_card('TELEVISION APPEARANCE','Sadeem','Rabii Ben Brahim appears on Sadeem, the Arab world’s digital creator competition.','Television appearance · Video provided by The Dreamer','','','https://youtu.be/dT68BX8jonk','Watch the Sadeem appearance','dT68BX8jonk')
projects+='</div>'
projects+=project_entry('01','CAMPAIGN / YKONE TUNIS','Land Rover Defender','A road trip across Tunisia for the launch of the Defender, with Rabii Ben Brahim as The Dreamer at the heart of the story.','Partner: YKONE Tunis · Land Rover Defender campaign','YkmgKAZFtXs',S['defender'],'View the campaign and credits')
projects+=project_entry('02','WILDLIFE FILM / TUNISIAN WONDERS','Wildlife Wonders','A film bringing Tunisia’s natural heritage into view. Rabii worked with wildlife ecologist Zakher Bouragaoui on the story.','The Dreamer × Zakher Bouragaoui · Film and field collaboration','oBRHiGLC0S4',S['wildlife'],'View the project post')
projects+=project_entry('03','DOCUMENTARY / WWF MEDITERRANEAN','Blue Future','Three Mediterranean stories about sustainable work tied to the sea, from tourism to fishing and renewable energy.','WWF and COGITO · Filmmakers: Ante Gugić, Rabii Ben Brahim, Emanuele Quartarone and Beatrice Surano','OyaSu8oF-D8',S['blue'],'Read the WWF credits')
projects+='<dialog class="project-story-dialog" aria-labelledby="project-story-title"><div class="project-story-shell"><button class="project-dialog-close" type="button" aria-label="Close project story">Close <span aria-hidden="true">×</span></button><div class="project-dialog-main"><div class="project-dialog-media"></div><div class="project-dialog-copy"><small></small><h2 id="project-story-title"></h2><p></p><p class="project-dialog-credit"></p></div></div><section class="project-dialog-gallery"><small>STILLS FROM THE STORY</small><div></div></section></div></dialog>'
write('collaborations','Projects',projects)

def about_photo(n,alt,caption='',shape=''):
 return f'<figure class="about-photo {shape}"><img src="/assets/about/{n:02}.jpg" loading="lazy" alt="{e(alt)}"><figcaption>{e(caption)}</figcaption></figure>'
def about_video(name,label):
 return f'<div class="about-motion"><video autoplay muted loop playsinline preload="metadata" aria-label="{e(label)}"><source src="/assets/about/{name}.mp4" type="video/mp4"></video><span>{e(label)}</span><button class="sound-toggle" type="button" aria-label="Turn sound on for {e(label)}" aria-pressed="false">Sound on</button></div>'

about = '''<section class="about-opening"><img class="about-opening-backdrop" src="/assets/about/01.jpg" alt="" aria-hidden="true"><img class="about-opening-image" src="/assets/about/01.jpg" alt="Photographer beside a vehicle in the Tunisian landscape" fetchpriority="high"><div class="about-opening-shade"></div><div class="about-opening-copy"><small>THE DREAMER / RABII BEN BRAHIM</small><h1>Wild and free.</h1><p>A life spent moving closer to the places, people and living world of Tunisia.</p></div><span class="about-opening-index">01 / THE PERSON BEHIND THE CAMERA</span></section>'''
about += '<section class="cinema-section about-beginning"><small>01 / THE BEGINNING</small><div><h2>A way of seeing.</h2><p class="large-copy">Curiosity became a camera. The camera became a way to bring Tunisia closer.</p><p>Rabii has spoken about watching documentaries with his father and spending time near the forest with his uncle. Those early experiences shaped the stories he would choose to tell.</p>'+a(ARAB,'Read his interview')+'</div></section>'
about += '<section class="about-chapter"><div class="about-chapter-copy"><small>02 / THE JOURNEY</small><h2>Always moving.</h2><p>From the coast to the forest, the road keeps opening onto another story. The Dreamer follows the light, the land and the life within it.</p>'+a(S['tourism'],'Discover Tunisia profile')+'</div><div class="about-motion-grid">'+about_video('tunisia','THIS IS TUNISIA / MOVING IMAGES')+about_photo(3,'Traveler beneath palms and old architecture','Between places','about-tile-short')+about_photo(5,'Person standing at the rocky coast at sunset','At the edge of the sea','about-tile-short')+'</div></section>'
about += '<div class="about-gallery about-gallery-first">'+about_photo(2,'Person resting beside a forest stream','Closer to the wild','about-portrait')+about_photo(4,'Person facing a waterfall in a red jacket','Into the water','about-portrait')+about_photo(6,'Person looking toward the sunset from a tent','The quiet in between','about-portrait')+about_photo(7,'Silhouette on a ridge at sunset','Follow the light','about-portrait')+'</div>'
about += editorial('03 / THE VISION','Look closer. Care more.','<p class="large-copy">A place becomes harder to ignore when its story is seen.</p><p>Rabii describes his work as a way to draw attention to Tunisia’s natural and cultural heritage. Film and photography let that purpose travel further.</p>'+a(ARAB,'Read his words'))
about += '<section class="about-chapter about-chapter-reverse"><div class="about-chapter-copy"><small>04 / THE LIVING WORLD</small><h2>Patient eyes.<br>Open horizons.</h2><p>Wildlife stories ask for time, attention and the willingness to wait. These frames sit alongside the landscapes and people that make up the larger journey.</p>'+a('/conservation/','Explore the impact')+'</div><div class="about-motion-grid">'+about_video('wildlife','IN THE FIELD / WILDLIFE')+about_photo(10,'Swimmer underwater above a coral reef','Below the surface','about-tile-short')+about_photo(8,'Person beneath a historic stone arch','The places we carry','about-tile-short')+'</div></section>'
about += '<div class="about-gallery about-gallery-last">'+about_photo(9,'View over a wide landscape beside a vehicle','Beyond the road','about-portrait')+about_photo(11,'Sunset seen through the rear of a vehicle','The long way home','about-portrait')+about_photo(12,'Man in conversation with a woman on a street','Human stories','about-portrait')+about_photo(13,'Person resting above a blue cove','A moment to stay','about-portrait')+'</div>'
about += editorial('IN CONVERSATION','The story continues.','<p>Hear Rabii speak about the path behind The Dreamer, or explore the films that grew from it.</p>'+a(POD,'Watch the conversation')+'<br>'+a('/films/','Explore the films'))
write('about','About',about)

speaking=head('06 / SPEAKING','Stories worth sharing.','Rabii Ben Brahim speaks about the moments, people and places behind The Dreamer.')
speaking+='<section class="speaking-intro speaking-intro-story"><div><small>THE VOICE BEHIND THE IMAGES</small><h2>From the field<br>to the conversation.</h2></div><p>Interviews and conversations give Rabii space to tell the stories behind his films and photography. These clips bring his voice into the frame.</p></section>'
local_clips=[('01','A moment from the conversation','/assets/speaking/clip-01.mp4'),('02','Behind the microphone','/assets/speaking/rabii-speaking-background.mp4'),('03','The Dreamer speaks','/assets/speaking/clip-03.mp4')]
speaking+='<section class="speaking-clips"><div class="speaking-section-heading"><small>FROM THE SUPPLIED FOOTAGE</small><h2>Listen to the story.</h2></div><div class="speaking-clip-grid">'+''.join(f'<article class="speaking-clip"><video autoplay muted loop playsinline controls preload="metadata" aria-label="{e(title)}"><source src="{src}" type="video/mp4"></video><div><small>{n} / SPEAKING</small><h3>{e(title)}</h3></div></article>' for n,title,src in local_clips)+'</div></section>'
def speaking_embed(video_id,title):
 return f'<div class="speaking-youtube"><iframe title="{e(title)}" loading="lazy" src="https://www.youtube-nocookie.com/embed/{video_id}?autoplay=0&amp;mute=0&amp;controls=1&amp;playsinline=1&amp;rel=0&amp;enablejsapi=1" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
speaking+='<section class="speaking-youtube-section"><div class="speaking-section-heading"><small>INTERVIEWS / CONVERSATIONS</small><h2>More of the voice behind the work.</h2><p>Play the conversations and interviews selected for this page.</p></div><div class="speaking-youtube-grid">'+speaking_embed('7cYfRkddQOE','The Dreamer — speaking video 01')+speaking_embed('poFk6c6C25Y','The Dreamer — speaking video 02')+speaking_embed('5ZJtvU-VOjw','Radio Cap FM — The Dreamer')+'</div></section>'
speaking+='<section class="speaking-cta"><small>FOR EVENTS</small><h2>Invite The Dreamer.</h2><p>For interviews, panels, podcasts, screenings, universities and creative events.</p>'+a('/contact/','Invite Rabii to Speak')+'</section>'
write('speaking','Speaking',speaking)

print_products=[
 ('The blue edge','Coast','526215548','Rocky Tunisian coastline meeting turquoise water','A meeting of stone and clear water, seen from above.','280 TND'),
 ('Along the shoreline','Coast','526506341','Rocky coastline and clear turquoise water seen from above','A line of rock traces the quiet edge of the sea.','280 TND'),
 ('A face in the grass','Wildlife','469728961','Close portrait of a large wild cat','An unhurried portrait from the wildlife archive.','320 TND'),
 ('The watcher','Wildlife','556922215','Small owl looking out from a rocky hollow','A small gaze emerging from the shelter of stone.','240 TND'),
 ('A breath in the open air','Wildlife','469683747','Wild cat with its mouth open against soft green','A fleeting expression held in a single frame.','320 TND'),
 ('A flash of green','Details','555826408','Green lizard on a rocky surface','Colour and texture meet on sun-warmed rock.','220 TND'),
]
prints='''<section class="print-shop-hero"><img src="/assets/photography/526215548.jpg" alt="Rocky coast and turquoise water" fetchpriority="high"><div class="print-shop-veil"></div><div class="print-shop-hero-copy"><small>THE DREAMER / FINE ART</small><h1>Bring the wild<br>closer.</h1><p>A preview collection of photographs from the field, imagined for the walls we live with.</p><a href="#collection" class="print-shop-action">Explore the collection <span aria-hidden="true">↓</span></a></div><span class="print-shop-hero-foot">PHOTOGRAPHY BY RABII BEN BRAHIM / COLLECTION PREVIEW</span></section>'''
prints+='''<section class="print-shop-intro"><small>THE COLLECTION / A FIRST LOOK</small><div><h2>Nature, held still.</h2><p>From the open coast to the smallest encounters in the wild, each frame offers another way to stay with a place.</p></div><span>Six studies / three chapters</span></section>'''
prints+='<section class="print-shop-catalog" id="collection"><div class="print-shop-toolbar"><div><small>THE DREAMER / PHOTO ARCHIVE</small><h2>Explore the works.</h2></div><div class="print-shop-filters" aria-label="Filter photographs"><button type="button" data-print-filter="All" aria-pressed="true">All works</button><button type="button" data-print-filter="Coast" aria-pressed="false">Coast</button><button type="button" data-print-filter="Wildlife" aria-pressed="false">Wildlife</button><button type="button" data-print-filter="Details" aria-pressed="false">Details</button></div></div><div class="print-shop-grid">'
for i,(title,category,filename,alt,description,price) in enumerate(print_products,1):
 image=f'/assets/photography/{filename}.jpg'
 prints+=f'''<article class="print-shop-card" data-print-category="{e(category)}" data-print-price="{e(price)}"><button type="button" class="print-shop-open" data-print-id="{i}" aria-label="View {e(title,quote=True)}"><span class="print-shop-image"><img src="{image}" alt="{e(alt,quote=True)}" loading="lazy"><span>VIEW THE WORK <span aria-hidden="true">↗</span></span></span><span class="print-shop-meta"><span><small>{i:02} / {e(category.upper())}</small><strong>{e(title)}</strong></span><span aria-hidden="true">↗</span></span></button><p>{e(description)}</p><div class="print-shop-price"><strong>{e(price)}</strong><span>Sample price</span></div><span class="print-shop-preview">SAMPLE LISTING · DETAILS TO BE CONFIRMED</span></article>'''
prints+='</div><p class="print-shop-disclaimer">Collection preview: all displayed prices are test prices in Tunisian dinars, not active offers. Print sizes, editions, paper, final prices and ordering are still to be confirmed with the artist.</p></section>'
prints+=f'''<dialog class="print-shop-dialog" aria-label="Photograph details"><button type="button" class="print-shop-close" aria-label="Close photograph details">Close ✕</button><div class="print-shop-dialog-layout"><div class="print-shop-dialog-image"><img alt=""></div><div class="print-shop-dialog-copy"><small>THE DREAMER / COLLECTION PREVIEW</small><h2></h2><p class="print-shop-dialog-category"></p><p class="print-shop-dialog-description"></p><div class="print-shop-spec"><span>FORMAT</span><strong>Fine art print concept</strong><span>SAMPLE PRICE</span><strong class="print-shop-dialog-price"></strong><span>EDITION</span><strong>To be confirmed</strong></div><p class="print-shop-dialog-note">This is a sample listing with a test price. Ask Rabii about the photograph and future print availability.</p>{a(IG,'Enquire on Instagram')}</div></div></dialog>'''
prints+=f'<section class="print-shop-ending"><small>FROM THE FIELD TO YOUR WALL</small><h2>Find a frame that stays with you.</h2><p>Discover more of Rabii’s photography, or ask him about a particular image.</p><div>{a("/photography/","Explore photography")}{a(IG,"Ask about prints")}</div></section>'
write('prints','Fine Art Prints',prints)

CONTACT_INBOX=''
contact=head('08 / CONTACT','Begin a conversation.','Films, conservation stories, partnerships, photography, speaking and prints.')
contact+=f'''<section class="contact-inquiry" aria-labelledby="contact-inquiry-title">
 <video class="contact-inquiry-film" autoplay muted loop playsinline preload="metadata" poster="/assets/impact/impact-opening.jpg" aria-hidden="true" tabindex="-1"><source src="/assets/impact/impact-opening.mp4" type="video/mp4"></video>
 <div class="contact-inquiry-shade"></div>
 <div class="contact-inquiry-shell">
  <div class="contact-inquiry-copy"><small>THE DREAMER / GET IN TOUCH</small><h2 id="contact-inquiry-title">Every story starts somewhere.</h2><p>For films, conservation work, photography and speaking invitations, share a little about what you have in mind.</p><div class="contact-inquiry-links">{a(IG,"Instagram")}{a(YT,"YouTube")}{a('https://www.linkedin.com/in/rabii-ben-brahim-007309141/',"LinkedIn")}</div></div>
  <form class="contact-form" data-recipient="{e(CONTACT_INBOX,quote=True)}">
   <small>START A CONVERSATION / 01</small><h3>Tell Rabii about your idea.</h3>
   <div class="contact-form-row"><label>Your name <span aria-hidden="true">*</span><input name="name" autocomplete="name" required maxlength="120" placeholder="Name"></label><label>Email address <span aria-hidden="true">*</span><input type="email" name="email" autocomplete="email" required maxlength="200" placeholder="you@example.com"></label></div>
   <label>What is this about?<select name="topic" required><option value="" disabled selected>Choose a topic</option><option>Film or documentary</option><option>Conservation or community</option><option>Photography</option><option>Speaking invitation</option><option>Something else</option></select></label>
   <label>Your message <span aria-hidden="true">*</span><textarea name="message" required maxlength="2000" rows="5" placeholder="Tell us about the place, people or story…"></textarea></label>
   <button class="contact-form-submit" type="submit" {'disabled aria-disabled="true"' if not CONTACT_INBOX else ''}>{'Email address pending' if not CONTACT_INBOX else 'Continue to email'} <span aria-hidden="true">↗</span></button>
   <p class="contact-form-note">{'An inquiry email address is being confirmed. Reach Rabii through Instagram in the meantime.' if not CONTACT_INBOX else 'Your email app will open with the message ready to send.'}</p>
   <p class="contact-form-status" role="status" aria-live="polite"></p>
  </form>
 </div>
</section>'''
write('contact','Contact',contact)
