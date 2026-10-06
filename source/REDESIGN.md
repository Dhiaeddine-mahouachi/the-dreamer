# The Dreamer — editorial redesign

## Audit

Base: `c58222e327d460307722e28bdc36558a3da5c7c4`. Nine existing pages; 111 directly stored assets, including 52 photography images, 13 About photographs, eight Djerba photographs, field video, posters and the existing Dreamer logo. Twelve full-quality videos are reconstructed from verified parts by the deployment script. `media-audit.json` inventories every stored file, image dimensions and reconstructed media. Existing asset files and source content are retained.

The existing source credit ledger is `CONTENT_SOURCES.md`. Confirmed content includes Wildlife Wonders, Blue Future, Land Rover Defender/YKONE, Tunisia, Djerba field material, community photography and appearances. Filenames alone do not establish dates, destinations, species, technical metadata or print availability. No Kenya, Namibia, Tanzania or South Africa expedition is inferred from wildlife pictures. New editorial titles describe supplied material; they are not claimed original film titles. No first-person field recollections or attributed quotes are invented.

## Revised sitemap

- `/`: editorial front page
- `/stories/`: curated visual essays
- `/stories/wildlife-wonders/`, `/stories/blue-future/`, `/stories/djerba-between-sea-and-stone/`, `/stories/the-defender-journey/`, `/stories/a-country-in-motion/`, `/stories/a-different-way-of-seeing/`
- `/films/` and individual `/films/<slug>/` pages: documented films and inline player
- `/photography/` and `/photography/<category>/`: the complete supplied photo archive
- `/expeditions/`, `/expeditions/tunisia/`, `/expeditions/djerba/`: documented journeys, not travel products
- `/conservation/`: wildlife, blue livelihoods and community photography
- `/field-notes/` and `/field-notes/<slug>/`: editorial observations of supplied images, not fabricated diary entries
- `/about/`, `/collaborations/`, `/speaking/`, `/prints/`, `/contact/`: retain existing routes

## Homepage wireframe

1. Full-viewport film / small logo and transparent horizontal navigation / bottom-left serif title / film controls
2. Warm-paper cover story: editorial label, huge title, full-width landscape, short introduction
3. Latest stories: dominant left feature + two smaller stacked features / fine horizontal rules
4. Frame from the wild: one large naturally framed photograph and descriptive caption
5. Black film section: main documentary poster and click-to-load player / three secondary films
6. Journeys: large Tunisia and Djerba photographs / documentary route links
7. Photography: mixed portrait and landscape spread, original compositions preserved
8. Conservation: emotional image and mission / verified project context
9. Field notes: three image-led journal entries
10. About: environmental portrait, concise biography and link
11. Selected collaborations: project-context images and explicit credits
12. Full-screen final photographic invitation
13. Minimal footer with secondary routes and AuraDigital credit

## Component architecture

`source/editorial.py` is the deterministic static generator. Shared document shell, publication navigation, footer, image/source helper, story tiles, film poster, captions, article template and curated gallery. `editorial.css` contains the new design system, independent of legacy CSS. `editorial.js` handles accessible menu, modal film/photo viewers, photo filters, progressive video loading, pause/sound controls and reduced motion. HTML remains navigable without JavaScript; native links open standalone film/photo routes.

## Media mapping

| Module | Existing material |
| --- | --- |
| Opening | Optimized excerpt of the supplied Tunisia film; existing hero poster |
| Cover story | `645836414.jpg`, `650871801.jpg`, `650643519.jpg` elephant photography; Wildlife Wonders context |
| Blue Future | Coast photography, coastal voices footage, verified film embed and WWF/COGITO credits |
| Djerba | All eight supplied Djerba photographs and `coastline.mp4` |
| Defender | `defender-field` still/clip, road footage and documented YKONE film |
| Frame from the wild | `645836414.jpg`, descriptive caption only |
| Photography | All 52 supplied photos, category assignments based on visible subject |
| About | All 13 supplied images, both original portrait films |
| Conservation | Existing community imagery, field-stories clip, three original impact clips |
| Speaking | Existing two local clips, three selected interview embeds and appearance links |
| Prints | Existing six photographs; availability inquiry, no active checkout or invented offer |

Responsive WebP derivatives are generated from originals without upscaling; original files remain untouched. Metadata fields with no evidence are omitted. Field observations use third-person editorial copy rather than simulated author testimony.

## Typography and colour

Georgia/Times serif: titles, statements and editorial headings. System sans-serif: navigation, categories, metadata, captions and controls. Main desktop headline `clamp(3.5rem,8vw,9rem)`; mobile 2.7–4rem. Body 18px / 1.7 with 700px maximum measure. Black `#080808`, charcoal `#151515`, warm paper `#F2F0EA`, grey `#A5A5A1`, muted gold `#C6A15B`. Thin rules, square edges, generous spacing. No cloned NatGeo visual identity.

## Responsive and accessibility rules

Desktop: twelve-column visual logic, fluid margins and asymmetric spreads. Tablet: two-column editorial grid. Below 760px: fullscreen navigation, cover title above image, generous single-column story pacing, portrait photographs remain contained, films use full native aspect ratios. No scroll hijacking. Native dialog supplies focus containment and Escape handling; focus returns to trigger. Visible focus, keyboard gallery navigation, alt text, captions, skip link, meaningful labels. Reduced motion and Save-Data retain poster instead of autoplay; automatic video is muted, paused offscreen and has a pause control. Film embeds load only on user action.

## Deployment

Retain GitHub Pages, existing `CNAME` (`fifty.ink`) and checksum-based original media assembly. Generate static route files before packaging; validate internal links and media, parse JavaScript, verify media checksums. Canonicals, Open Graph, sitemap and appropriate Article/Person metadata are generated per route. No Site-host migration.
