<div align="center">
  <h1>🎨 Awesome Codex ImageGen Skills</h1>
  <p><a href="README.md">中文</a> · <strong>English</strong></p>
  <p><strong>Discover, compare, and reuse great visual methods.</strong></p>
  <p>A living collection of Codex ImageGen skills with real generated examples.</p>
  <p>
    <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
    <img src="https://img.shields.io/badge/Codex-ImageGen-111827?style=flat-square&logo=openai&logoColor=white" alt="Codex ImageGen">
    <img src="https://img.shields.io/badge/showcases-36-ec4899?style=flat-square" alt="36 skill showcases">
    <img src="https://img.shields.io/badge/generated_samples-144-7c3aed?style=flat-square" alt="144 generated samples">
    <a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-22c55e?style=flat-square" alt="PRs welcome"></a>
  </p>
  <p>
    <a href="#photo--editorial">Explore skills</a> ·
    <a href="#sample-inputs--reproduction">View the sample inputs</a> ·
    <a href="#contributing">Submit a skill</a>
  </p>
  <p><strong>Like the collection? Leave a Star ⭐ Found a great skill? Send a PR 🚀</strong></p>
</div>

---

This collection highlights projects that package visual methods, domain knowledge, and creative workflows into `SKILL.md` files and use the Codex harness built-in `image_gen` capability.

> This repository provides an index, categories, concise reviews, and generated examples. Third-party skills are shallow-cloned only when needed into the Git-ignored `upstream/` directory and are never committed as mirrors. Upstream copyright, licenses, and restrictions still apply.

## 🧭 Contents

- 📸 [Photo & Editorial](#photo--editorial)
- 🪄 [Branding & Identity](#branding--identity)
- 🧶 [Craft & Textile](#craft--textile)
- 📚 [Articles, Knowledge & Presentations](#articles-knowledge--presentations)
- 🖥️ [UI & Product Design](#ui--product-design)
- 🎮 [Game Assets & Characters](#game-assets--characters)
- 🎬 [Storyboards & Visual Narratives](#storyboards--visual-narratives)
- 🧪 [Sample Inputs & Reproduction](#sample-inputs--reproduction)
- 🤝 [Contributing](#contributing)
  - 🔎 [Curation](#curation)
- 🔗 [Related Collections](#related-collections)
  - 🧱 [Official Foundations](#official-foundations)

<a id="photo--editorial"></a>
## Photo & Editorial

### [Photo Abstract Editorial](https://github.com/ZzzLc0405/photo-abstract-editorial)

Turns a photograph into a vertical editorial composition combining an intact photo region, an abstract memory panel derived from the image, and a poetic English title.

- **Author:** [ZzzLc0405](https://github.com/ZzzLc0405)
- **Input:** One photograph
- **Output:** A vertical photographic editorial artwork
- **ImageGen role:** Preserves the photo region while translating subject relationships, spatial axes, light, and color into an abstract panel and title
- **Structure:** `SKILL.md`, `agents/openai.yaml`, bilingual reference prompts, and examples
- **License:** Personal, educational, research, and non-commercial use only; contact the author for commercial licensing

<p><strong>🖼️ Samples</strong> · <code>photo-abstract-editorial</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/photo-abstract-editorial/01-architecture-cafe.png"><img src="examples/photo-abstract-editorial/01-architecture-cafe.png" alt="photo-abstract-editorial — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/photo-abstract-editorial/02-mountain-lake.png"><img src="examples/photo-abstract-editorial/02-mountain-lake.png" alt="photo-abstract-editorial — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/photo-abstract-editorial/03-portrait-camera-duo.png"><img src="examples/photo-abstract-editorial/03-portrait-camera-duo.png" alt="photo-abstract-editorial — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/photo-abstract-editorial/04-animal-cat-dog.png"><img src="examples/photo-abstract-editorial/04-animal-cat-dog.png" alt="photo-abstract-editorial — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Scenes Gathered Zine v1.3](https://github.com/Zeejay0/gathered-scenes-zine-skill/tree/main/skills/scenes-gathered-zine-v1-3)

Extends a recognizable source photograph into a tactile zine poster with torn-paper boundaries, abstract illustration, print texture, and restrained microtype.

- **Author:** [Zeejay0](https://github.com/Zeejay0)
- **Input:** One photograph; optional title, language, and relationship notes
- **Output:** A 3:5 vertical zine collage by default, or a landscape composition when appropriate
- **ImageGen role:** Preserves the central subject and space while deriving an illustrated field from source shapes, colors, and mood
- **Structure:** `SKILL.md`, `agents/openai.yaml`, and two official source/result examples
- **License:** Personal non-commercial use only; commercial, commissioned, internal, and paid use requires written permission

<p><strong>🖼️ Samples</strong> · <code>scenes-gathered-zine-v1-3</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/scenes-gathered-zine-v1-3/01-architecture-cafe.png"><img src="examples/scenes-gathered-zine-v1-3/01-architecture-cafe.png" alt="scenes-gathered-zine-v1-3 — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/scenes-gathered-zine-v1-3/02-mountain-lake.png"><img src="examples/scenes-gathered-zine-v1-3/02-mountain-lake.png" alt="scenes-gathered-zine-v1-3 — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/scenes-gathered-zine-v1-3/03-portrait-camera-duo.png"><img src="examples/scenes-gathered-zine-v1-3/03-portrait-camera-duo.png" alt="scenes-gathered-zine-v1-3 — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/scenes-gathered-zine-v1-3/04-animal-cat-dog.png"><img src="examples/scenes-gathered-zine-v1-3/04-animal-cat-dog.png" alt="scenes-gathered-zine-v1-3 — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Photo to Monthly Zine Postcard](https://github.com/shenchangyi/photo-to-monthly-zine-postcard/tree/main/skills/photo-to-monthly-zine-postcard)

Turns a photo into a 3:4 monthly zine postcard with the complete image above and watercolor, month, literary, music, and footer elements below.

- **Author:** [shenchangyi](https://github.com/shenchangyi)
- **Input:** One photo; optional month, handwritten line, signature, date, footer, reading reference, or song
- **Output:** A 3:4 vertical monthly photo postcard
- **ImageGen role:** Preserves the upper photo and derives the lower watercolor block and layout from its subjects, space, and light
- **Structure:** A compact `SKILL.md`, three workflow references, a full rule draft, visual references, and eight examples
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>photo-to-monthly-zine-postcard</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/photo-to-monthly-zine-postcard/01-architecture-cafe.png"><img src="examples/photo-to-monthly-zine-postcard/01-architecture-cafe.png" alt="photo-to-monthly-zine-postcard — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/photo-to-monthly-zine-postcard/02-mountain-lake.png"><img src="examples/photo-to-monthly-zine-postcard/02-mountain-lake.png" alt="photo-to-monthly-zine-postcard — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/photo-to-monthly-zine-postcard/03-portrait-camera-duo.png"><img src="examples/photo-to-monthly-zine-postcard/03-portrait-camera-duo.png" alt="photo-to-monthly-zine-postcard — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/photo-to-monthly-zine-postcard/04-animal-cat-dog.png"><img src="examples/photo-to-monthly-zine-postcard/04-animal-cat-dog.png" alt="photo-to-monthly-zine-postcard — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [GC Minimal Zine Poster v0.3.1](https://github.com/LiamGvchi/gc-minimal-zine-poster)

Transforms text, objects, moods, photos, or references into quiet paper-textured micro-editorial posters with generous negative space and one saturated focal color.

- **Author:** [LiamGvchi](https://github.com/LiamGvchi)
- **Input:** A text topic, article, photo, reference image, or image folder
- **Output:** A 3:5 raster poster by default, plus the final prompt, recipe, and rationale; analysis-only and prompt-only modes are supported
- **ImageGen role:** Calls built-in image generation, passes the real source in photo mode, checks preservation invariants, and allows one targeted regeneration
- **Structure:** `SKILL.md`, five references, six author examples, eight evals, Codex UI metadata, and a trilingual README
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>gc-minimal-zine-poster-v0-3</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/gc-minimal-zine-poster-v0-3/01-architecture-cafe.png"><img src="examples/gc-minimal-zine-poster-v0-3/01-architecture-cafe.png" alt="gc-minimal-zine-poster-v0-3 — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/gc-minimal-zine-poster-v0-3/02-mountain-lake.png"><img src="examples/gc-minimal-zine-poster-v0-3/02-mountain-lake.png" alt="gc-minimal-zine-poster-v0-3 — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/gc-minimal-zine-poster-v0-3/03-portrait-camera-duo.png"><img src="examples/gc-minimal-zine-poster-v0-3/03-portrait-camera-duo.png" alt="gc-minimal-zine-poster-v0-3 — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/gc-minimal-zine-poster-v0-3/04-animal-cat-dog.png"><img src="examples/gc-minimal-zine-poster-v0-3/04-animal-cat-dog.png" alt="gc-minimal-zine-poster-v0-3 — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Dreamcore Collage Poster](https://github.com/AndrwewHan/dreamcore-collage-poster)

Recomposes a theme or photo as a dense dreamcore collage with one recognizable anchor, several echoes, a memory environment, geometric interruptions, and one impossible relationship.

- **Author:** [AndrwewHan](https://github.com/AndrwewHan)
- **Input:** A text theme or up to five references with distinct roles
- **Output:** A vertical dreamcore, digital-memory, ritual-archive, or surreal collage poster
- **ImageGen role:** Uses Codex built-in `image_gen` for generation or editing without an external image backend
- **Structure:** A single `SKILL.md`, Codex UI metadata, and a compact README
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>dreamcore-collage-poster</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/dreamcore-collage-poster/01-architecture-cafe.png"><img src="examples/dreamcore-collage-poster/01-architecture-cafe.png" alt="dreamcore-collage-poster — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/dreamcore-collage-poster/02-mountain-lake.png"><img src="examples/dreamcore-collage-poster/02-mountain-lake.png" alt="dreamcore-collage-poster — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/dreamcore-collage-poster/03-portrait-camera-duo.png"><img src="examples/dreamcore-collage-poster/03-portrait-camera-duo.png" alt="dreamcore-collage-poster — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/dreamcore-collage-poster/04-animal-cat-dog.png"><img src="examples/dreamcore-collage-poster/04-animal-cat-dog.png" alt="dreamcore-collage-poster — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Make Photo Stamp Archive](https://github.com/Dlcccc71913/skill-make-photo-stamp-archive)

Pairs a photo with warm archival paper, a small handmade stamp derived from the subject, and restrained typewriter annotations.

- **Author:** [Dlcccc71913](https://github.com/Dlcccc71913)
- **Input:** One or more photos; revisions may target the stamp, border, size, position, ink, title, paper age, or join direction
- **Output:** One flat raster per source photo; the default is a horizontal 55/45 photo-to-paper split
- **ImageGen role:** Calls built-in generation/editing for each photo and locks untouched attributes during revisions
- **Structure:** `SKILL.md`, a prompt/revision template, `agents/openai.yaml`, a trilingual README, and three linked examples
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>make-photo-stamp-archive</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/make-photo-stamp-archive/01-architecture-cafe.png"><img src="examples/make-photo-stamp-archive/01-architecture-cafe.png" alt="make-photo-stamp-archive — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/make-photo-stamp-archive/02-mountain-lake.png"><img src="examples/make-photo-stamp-archive/02-mountain-lake.png" alt="make-photo-stamp-archive — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/make-photo-stamp-archive/03-portrait-camera-duo.png"><img src="examples/make-photo-stamp-archive/03-portrait-camera-duo.png" alt="make-photo-stamp-archive — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/make-photo-stamp-archive/04-animal-cat-dog.png"><img src="examples/make-photo-stamp-archive/04-animal-cat-dog.png" alt="make-photo-stamp-archive — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<a id="branding--identity"></a>
## Branding & Identity

### [IP as Logo](https://github.com/s1dashu/ip-as-logo-skill)

Generates extremely simplified, rounded square mascot candidates designed to remain recognizable at 32×32.

- **Author:** [s1dashu](https://github.com/s1dashu)
- **Input:** A specific animal, object, or character; directions may be inferred from product context, audience, and brand personality
- **Output:** Six independent 1:1 raster candidates with labels, directions, composition, prompt/color mappings, dimensions, and paths
- **ImageGen role:** Generates each candidate independently under shape, palette, proportion, and small-size recognition constraints
- **Structure:** A single `SKILL.md`, README, MIT License, and one showcase wall
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>ip-as-logo</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/ip-as-logo/01-architecture-cafe.png"><img src="examples/ip-as-logo/01-architecture-cafe.png" alt="ip-as-logo — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/ip-as-logo/02-mountain-lake.png"><img src="examples/ip-as-logo/02-mountain-lake.png" alt="ip-as-logo — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/ip-as-logo/03-portrait-camera-duo.png"><img src="examples/ip-as-logo/03-portrait-camera-duo.png" alt="ip-as-logo — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/ip-as-logo/04-animal-cat-dog.png"><img src="examples/ip-as-logo/04-animal-cat-dog.png" alt="ip-as-logo — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [30x-image](https://github.com/norahe0304-art/30x-image)

Combines a brand `DESIGN.md`, eight marketing templates, variation axes, and anti-slop rules to create many kinds of branded marketing images.

- **Author:** [norahe0304-art](https://github.com/norahe0304-art)
- **Input:** A brand profile or URL, design tokens, Figma Variables, CSS, screenshots, and a written brief
- **Output:** Brand-consistent standalone marketing rasters plus a JSON manifest
- **ImageGen role:** Requires OpenAI/Codex built-in `image_generation` and stops rather than substituting HTML, SVG, or local drawing
- **Structure:** An approximately 800-line entry skill, three references, brand profiles, and Codex metadata
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>30x-image</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/30x-image/01-architecture-cafe.png"><img src="examples/30x-image/01-architecture-cafe.png" alt="30x-image — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/30x-image/02-mountain-lake.png"><img src="examples/30x-image/02-mountain-lake.png" alt="30x-image — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/30x-image/03-portrait-camera-duo.png"><img src="examples/30x-image/03-portrait-camera-duo.png" alt="30x-image — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/30x-image/04-animal-cat-dog.png"><img src="examples/30x-image/04-animal-cat-dog.png" alt="30x-image — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<a id="craft--textile"></a>
## Craft & Textile

### [Yarn Rug Reference](https://github.com/rlx-better/yarn-rug-reference)

Simplifies an image into a low-color handmade yarn, tufted-rug, or textile interpretation and presents it beneath the original.

- **Author:** [rlx-better](https://github.com/rlx-better)
- **Input:** One source image and an optional textile-style reference
- **Output:** A 2:3 vertical before/after comparison
- **ImageGen role:** Rebuilds the source as a 6–8-color blocky yarn rug while preserving subject, composition, and fiber direction
- **Structure:** `SKILL.md`, `agents/openai.yaml`, and five reference images
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>yarn-rug-reference</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/yarn-rug-reference/01-architecture-cafe.png"><img src="examples/yarn-rug-reference/01-architecture-cafe.png" alt="yarn-rug-reference — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/yarn-rug-reference/02-mountain-lake.png"><img src="examples/yarn-rug-reference/02-mountain-lake.png" alt="yarn-rug-reference — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/yarn-rug-reference/03-portrait-camera-duo.png"><img src="examples/yarn-rug-reference/03-portrait-camera-duo.png" alt="yarn-rug-reference — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/yarn-rug-reference/04-animal-cat-dog.png"><img src="examples/yarn-rug-reference/04-animal-cat-dog.png" alt="yarn-rug-reference — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<a id="articles-knowledge--presentations"></a>
## Articles, Knowledge & Presentations

### [Ian Xiaohei Illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)

Translates key claims, processes, states, and metaphors from Chinese articles into 16:9 white-background Xiaohei illustrations.

- **Author:** [helloianneo](https://github.com/helloianneo)
- **Input:** A Chinese article, post, blog, Notion/Markdown document, or single idea
- **Output:** Four to eight standalone body illustrations by default, or a shot list
- **ImageGen role:** Uses built-in `image_gen` and generates each illustration separately
- **Structure:** A compact `SKILL.md`, five references, fourteen style anchors, and example prompts
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>ian-xiaohei-illustrations</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-illustrations/01-architecture-cafe.png"><img src="examples/ian-xiaohei-illustrations/01-architecture-cafe.png" alt="ian-xiaohei-illustrations — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-illustrations/02-mountain-lake.png"><img src="examples/ian-xiaohei-illustrations/02-mountain-lake.png" alt="ian-xiaohei-illustrations — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-illustrations/03-portrait-camera-duo.png"><img src="examples/ian-xiaohei-illustrations/03-portrait-camera-duo.png" alt="ian-xiaohei-illustrations — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-illustrations/04-animal-cat-dog.png"><img src="examples/ian-xiaohei-illustrations/04-animal-cat-dog.png" alt="ian-xiaohei-illustrations — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Ian Xiaohei Scenes](https://github.com/helloianneo/ian-xiaohei-scenes)

Uses Xiaohei, real objects, and physical action to illustrate workplace situations and project stories, with an ultra-wide narrative mode.

- **Author:** [helloianneo](https://github.com/helloianneo)
- **Input:** Body copy, a theme, retrospective, personal story, or five to eight sequential beats
- **Output:** A 16:9 white-studio scene or an approximately 2.6:1–3:1 long-form image
- **ImageGen role:** Locks a quality master, then generates, compares, and selectively regenerates each scene
- **Structure:** A detailed `SKILL.md`, seven references, and seven master-quality examples
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>ian-xiaohei-scenes</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-scenes/01-architecture-cafe.png"><img src="examples/ian-xiaohei-scenes/01-architecture-cafe.png" alt="ian-xiaohei-scenes — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-scenes/02-mountain-lake.png"><img src="examples/ian-xiaohei-scenes/02-mountain-lake.png" alt="ian-xiaohei-scenes — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-scenes/03-portrait-camera-duo.png"><img src="examples/ian-xiaohei-scenes/03-portrait-camera-duo.png" alt="ian-xiaohei-scenes — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/ian-xiaohei-scenes/04-animal-cat-dog.png"><img src="examples/ian-xiaohei-scenes/04-animal-cat-dog.png" alt="ian-xiaohei-scenes — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt)

Turns articles, courses, PDFs, DOCX files, or existing presentation material into complete Chinese hand-drawn technical explainer slides.

- **Author:** [helloianneo](https://github.com/helloianneo)
- **Input:** An article, document, course deck, script, outline, or rough idea
- **Output:** A 21:9 cover, 16:9 body/slide PNGs, and a multi-page contact sheet
- **ImageGen role:** Generates each page as a raster and uses deterministic tools only for exact text, cropping, or dimensions
- **Structure:** An entry `SKILL.md`, six narrative and visual references, theme tokens, and four examples
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>ian-handdrawn-ppt</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/ian-handdrawn-ppt/01-architecture-cafe.png"><img src="examples/ian-handdrawn-ppt/01-architecture-cafe.png" alt="ian-handdrawn-ppt — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/ian-handdrawn-ppt/02-mountain-lake.png"><img src="examples/ian-handdrawn-ppt/02-mountain-lake.png" alt="ian-handdrawn-ppt — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/ian-handdrawn-ppt/03-portrait-camera-duo.png"><img src="examples/ian-handdrawn-ppt/03-portrait-camera-duo.png" alt="ian-handdrawn-ppt — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/ian-handdrawn-ppt/04-animal-cat-dog.png"><img src="examples/ian-handdrawn-ppt/04-animal-cat-dog.png" alt="ian-handdrawn-ppt — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Codex Illustrator](https://github.com/99Gaoxiaoqi/codex-illustrator)

Detects passages in Markdown that need visual explanation and routes them to Mermaid, Excalidraw, or ImageGen.

- **Author:** [99Gaoxiaoqi](https://github.com/99Gaoxiaoqi)
- **Input:** A Markdown document, with optional cover or presentation-image needs
- **Output:** Markdown with image references, standalone illustrations, covers, or presentation graphics
- **ImageGen role:** Uses built-in `image_gen.imagegen` for creative visuals and deterministic tools for structural diagrams
- **Structure:** `SKILL.md`, `agents/openai.yaml`, three references, five styles, two export scripts, and a workflow diagram
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>codex-illustrator</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/codex-illustrator/01-architecture-cafe.png"><img src="examples/codex-illustrator/01-architecture-cafe.png" alt="codex-illustrator — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/codex-illustrator/02-mountain-lake.png"><img src="examples/codex-illustrator/02-mountain-lake.png" alt="codex-illustrator — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/codex-illustrator/03-portrait-camera-duo.png"><img src="examples/codex-illustrator/03-portrait-camera-duo.png" alt="codex-illustrator — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/codex-illustrator/04-animal-cat-dog.png"><img src="examples/codex-illustrator/04-animal-cat-dog.png" alt="codex-illustrator — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Baoyu Visual Skills Suite](https://github.com/JimLiu/baoyu-skills)

A multi-skill suite for article illustrations, covers, comics, infographics, and Xiaohongshu card sets.

- **Author:** [Jim Liu](https://github.com/JimLiu)
- **Input:** An article, topic, or publishing need; optional references, brand colors, audience, style, and layout
- **Output:** Article images, covers, sequential comics, infographics, or card sets, with saved prompts
- **ImageGen role:** Supports several runtimes and prefers native `imagegen` when detected in Codex
- **Structure:** Five independent skills with their own workflows, references, and examples
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>baoyu-article-illustrator</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/baoyu-article-illustrator/01-architecture-cafe.png"><img src="examples/baoyu-article-illustrator/01-architecture-cafe.png" alt="baoyu-article-illustrator — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-article-illustrator/02-mountain-lake.png"><img src="examples/baoyu-article-illustrator/02-mountain-lake.png" alt="baoyu-article-illustrator — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-article-illustrator/03-portrait-camera-duo.png"><img src="examples/baoyu-article-illustrator/03-portrait-camera-duo.png" alt="baoyu-article-illustrator — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-article-illustrator/04-animal-cat-dog.png"><img src="examples/baoyu-article-illustrator/04-animal-cat-dog.png" alt="baoyu-article-illustrator — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<p><strong>🖼️ Samples</strong> · <code>baoyu-cover-image</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/baoyu-cover-image/01-architecture-cafe.png"><img src="examples/baoyu-cover-image/01-architecture-cafe.png" alt="baoyu-cover-image — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-cover-image/02-mountain-lake.png"><img src="examples/baoyu-cover-image/02-mountain-lake.png" alt="baoyu-cover-image — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-cover-image/03-portrait-camera-duo.png"><img src="examples/baoyu-cover-image/03-portrait-camera-duo.png" alt="baoyu-cover-image — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-cover-image/04-animal-cat-dog.png"><img src="examples/baoyu-cover-image/04-animal-cat-dog.png" alt="baoyu-cover-image — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<p><strong>🖼️ Samples</strong> · <code>baoyu-comic</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/baoyu-comic/01-architecture-cafe.png"><img src="examples/baoyu-comic/01-architecture-cafe.png" alt="baoyu-comic — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-comic/02-mountain-lake.png"><img src="examples/baoyu-comic/02-mountain-lake.png" alt="baoyu-comic — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-comic/03-portrait-camera-duo.png"><img src="examples/baoyu-comic/03-portrait-camera-duo.png" alt="baoyu-comic — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-comic/04-animal-cat-dog.png"><img src="examples/baoyu-comic/04-animal-cat-dog.png" alt="baoyu-comic — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<p><strong>🖼️ Samples</strong> · <code>baoyu-infographic</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/baoyu-infographic/01-architecture-cafe.png"><img src="examples/baoyu-infographic/01-architecture-cafe.png" alt="baoyu-infographic — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-infographic/02-mountain-lake.png"><img src="examples/baoyu-infographic/02-mountain-lake.png" alt="baoyu-infographic — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-infographic/03-portrait-camera-duo.png"><img src="examples/baoyu-infographic/03-portrait-camera-duo.png" alt="baoyu-infographic — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-infographic/04-animal-cat-dog.png"><img src="examples/baoyu-infographic/04-animal-cat-dog.png" alt="baoyu-infographic — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<p><strong>🖼️ Samples</strong> · <code>baoyu-xhs-images</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/baoyu-xhs-images/01-architecture-cafe.png"><img src="examples/baoyu-xhs-images/01-architecture-cafe.png" alt="baoyu-xhs-images — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-xhs-images/02-mountain-lake.png"><img src="examples/baoyu-xhs-images/02-mountain-lake.png" alt="baoyu-xhs-images — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-xhs-images/03-portrait-camera-duo.png"><img src="examples/baoyu-xhs-images/03-portrait-camera-duo.png" alt="baoyu-xhs-images — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/baoyu-xhs-images/04-animal-cat-dog.png"><img src="examples/baoyu-xhs-images/04-animal-cat-dog.png" alt="baoyu-xhs-images — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Codex Image: Technical Infographics](https://github.com/philipbankier/codex-image-skill)

Creates source-grounded technical infographics, explainers, and content packs from URLs, briefs, local files, or repositories.

- **Author:** [Philip Bankier](https://github.com/philipbankier)
- **Input:** A URL, pasted text, local file, or local repository
- **Output:** `research-brief.md`, `image-prompt.md`, and `final.png`; pack mode produces three targeted outputs
- **ImageGen role:** Uses only Codex built-in `gpt-image-2` and forbids direct API calls or API-key requests
- **Structure:** A skill file, three templates, three examples, acceptance docs, tests, and static checks
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>codex-image</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/codex-image/01-architecture-cafe.png"><img src="examples/codex-image/01-architecture-cafe.png" alt="codex-image — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/codex-image/02-mountain-lake.png"><img src="examples/codex-image/02-mountain-lake.png" alt="codex-image — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/codex-image/03-portrait-camera-duo.png"><img src="examples/codex-image/03-portrait-camera-duo.png" alt="codex-image — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/codex-image/04-animal-cat-dog.png"><img src="examples/codex-image/04-animal-cat-dog.png" alt="codex-image — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Codex Paper Figure Skill](https://github.com/pengqianhan/codex-paper-figure-skill)

Explores academic-figure composition with built-in ImageGen, then rebuilds the result as editable native Draw.io geometry.

- **Author:** [Pengqian Han](https://github.com/pengqianhan)
- **Input:** Paper text, method or result descriptions, mechanism diagrams, model architectures, or graphical-abstract ideas
- **Output:** A `.drawio` file, with an optional raster reference and PNG/SVG/PDF previews
- **ImageGen role:** Generates composition references without treating unreliable raster text as the editable final
- **Structure:** One `SKILL.md`, Codex metadata, and two Draw.io/preview examples
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>codex-paper-figure-skill</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/codex-paper-figure-skill/01-architecture-cafe.png"><img src="examples/codex-paper-figure-skill/01-architecture-cafe.png" alt="codex-paper-figure-skill — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/codex-paper-figure-skill/02-mountain-lake.png"><img src="examples/codex-paper-figure-skill/02-mountain-lake.png" alt="codex-paper-figure-skill — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/codex-paper-figure-skill/03-portrait-camera-duo.png"><img src="examples/codex-paper-figure-skill/03-portrait-camera-duo.png" alt="codex-paper-figure-skill — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/codex-paper-figure-skill/04-animal-cat-dog.png"><img src="examples/codex-paper-figure-skill/04-animal-cat-dog.png" alt="codex-paper-figure-skill — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<a id="ui--product-design"></a>
## UI & Product Design

### [Prototype Native UI with Image Generation](https://github.com/dnesdan/Skills/tree/main/prototype-ui-with-imagegen)

Explores several native Apple or Android UI directions, compares them with product and platform constraints, and implements only after selection.

- **Author:** [dnesdan](https://github.com/dnesdan)
- **Input:** A component, screen, state, or short flow; optional screenshots, product content, and platform constraints
- **Output:** Three native UI directions by default, up to five, with an annotated sheet and comparison; selected work can be rebuilt in SwiftUI or Jetpack Compose
- **ImageGen role:** Uses Codex ImageGen for visual hypotheses, never as production UI
- **Structure:** `SKILL.md` plus focused references for backends, prompting, native components, implementation, dialogue, and validation
- **License:** No open-source license declared upstream

<p><strong>🖼️ Samples</strong> · <code>prototype-ui-with-imagegen</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/prototype-ui-with-imagegen/01-architecture-cafe.png"><img src="examples/prototype-ui-with-imagegen/01-architecture-cafe.png" alt="prototype-ui-with-imagegen — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/prototype-ui-with-imagegen/02-mountain-lake.png"><img src="examples/prototype-ui-with-imagegen/02-mountain-lake.png" alt="prototype-ui-with-imagegen — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/prototype-ui-with-imagegen/03-portrait-camera-duo.png"><img src="examples/prototype-ui-with-imagegen/03-portrait-camera-duo.png" alt="prototype-ui-with-imagegen — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/prototype-ui-with-imagegen/04-animal-cat-dog.png"><img src="examples/prototype-ui-with-imagegen/04-animal-cat-dog.png" alt="prototype-ui-with-imagegen — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Frontend App Builder](https://github.com/openai/plugins/tree/main/plugins/build-web-apps/skills/frontend-app-builder)

An official OpenAI composite skill that designs complete pages, UI states, or game screens before implementing and validating them in a browser.

- **Author:** [OpenAI](https://github.com/openai)
- **Input:** A new or existing frontend project, product brief, content, and requirements; optional references and backend provider
- **Output:** Visual concepts, production bitmap assets, a responsive implementation, and browser-validation screenshots
- **ImageGen role:** Creates full-page or state-level design references before coding and supplies production bitmap assets
- **Structure:** `SKILL.md`, `agents/openai.yaml`, and references for website concepts and visual validation
- **License:** No open-source license declared upstream

<p><strong>🖼️ Samples</strong> · <code>frontend-app-builder</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/frontend-app-builder/01-architecture-cafe.png"><img src="examples/frontend-app-builder/01-architecture-cafe.png" alt="frontend-app-builder — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/frontend-app-builder/02-mountain-lake.png"><img src="examples/frontend-app-builder/02-mountain-lake.png" alt="frontend-app-builder — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/frontend-app-builder/03-portrait-camera-duo.png"><img src="examples/frontend-app-builder/03-portrait-camera-duo.png" alt="frontend-app-builder — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/frontend-app-builder/04-animal-cat-dog.png"><img src="examples/frontend-app-builder/04-animal-cat-dog.png" alt="frontend-app-builder — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Img to Frontend](https://github.com/am-will/codex-skills/tree/main/skills/img-to-frontend)

Generates four genuinely distinct web directions, waits for a user choice, then implements the selected responsive frontend.

- **Author:** [am-will](https://github.com/am-will)
- **Input:** An existing frontend repository or website brief, content, references, and technical constraints
- **Output:** Four differentiated concepts, the selected implementation, and multi-viewport QA screenshots
- **ImageGen role:** Requires four separate `$imagegen` calls before implementation begins
- **Structure:** `SKILL.md`, `agents/openai.yaml`, and one visual-iteration reference
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>img-to-frontend</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/img-to-frontend/01-architecture-cafe.png"><img src="examples/img-to-frontend/01-architecture-cafe.png" alt="img-to-frontend — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/img-to-frontend/02-mountain-lake.png"><img src="examples/img-to-frontend/02-mountain-lake.png" alt="img-to-frontend — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/img-to-frontend/03-portrait-camera-duo.png"><img src="examples/img-to-frontend/03-portrait-camera-duo.png" alt="img-to-frontend — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/img-to-frontend/04-animal-cat-dog.png"><img src="examples/img-to-frontend/04-animal-cat-dog.png" alt="img-to-frontend — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Taste Image Generation Suite](https://github.com/Leonxlnx/taste-skill#image-generation-skills)

A set of image-only skills for web sections, mobile screens and flows, and full brand-identity boards.

- **Author:** [Leonxlnx](https://github.com/Leonxlnx)
- **Input:** A website section, mobile screen or flow, or brand-system brief; optional content, platform, audience, and references
- **Output:** One landscape image per web section, mobile image sets, or a 2×2 to 3×3 brand-system board
- **ImageGen role:** Provides instructions compatible with ChatGPT Images, Codex image mode, and other image agents
- **Structure:** Three standalone skills: `imagegen-frontend-web`, `imagegen-frontend-mobile`, and `brandkit`
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>taste-imagegen-frontend-web</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-web/01-architecture-cafe.png"><img src="examples/taste-imagegen-frontend-web/01-architecture-cafe.png" alt="taste-imagegen-frontend-web — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-web/02-mountain-lake.png"><img src="examples/taste-imagegen-frontend-web/02-mountain-lake.png" alt="taste-imagegen-frontend-web — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-web/03-portrait-camera-duo.png"><img src="examples/taste-imagegen-frontend-web/03-portrait-camera-duo.png" alt="taste-imagegen-frontend-web — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-web/04-animal-cat-dog.png"><img src="examples/taste-imagegen-frontend-web/04-animal-cat-dog.png" alt="taste-imagegen-frontend-web — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<p><strong>🖼️ Samples</strong> · <code>taste-imagegen-frontend-mobile</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-mobile/01-architecture-cafe.png"><img src="examples/taste-imagegen-frontend-mobile/01-architecture-cafe.png" alt="taste-imagegen-frontend-mobile — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-mobile/02-mountain-lake.png"><img src="examples/taste-imagegen-frontend-mobile/02-mountain-lake.png" alt="taste-imagegen-frontend-mobile — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-mobile/03-portrait-camera-duo.png"><img src="examples/taste-imagegen-frontend-mobile/03-portrait-camera-duo.png" alt="taste-imagegen-frontend-mobile — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/taste-imagegen-frontend-mobile/04-animal-cat-dog.png"><img src="examples/taste-imagegen-frontend-mobile/04-animal-cat-dog.png" alt="taste-imagegen-frontend-mobile — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<p><strong>🖼️ Samples</strong> · <code>taste-brandkit</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/taste-brandkit/01-architecture-cafe.png"><img src="examples/taste-brandkit/01-architecture-cafe.png" alt="taste-brandkit — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/taste-brandkit/02-mountain-lake.png"><img src="examples/taste-brandkit/02-mountain-lake.png" alt="taste-brandkit — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/taste-brandkit/03-portrait-camera-duo.png"><img src="examples/taste-brandkit/03-portrait-camera-duo.png" alt="taste-brandkit — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/taste-brandkit/04-animal-cat-dog.png"><img src="examples/taste-brandkit/04-animal-cat-dog.png" alt="taste-brandkit — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [HIAPI Icon Skills](https://github.com/HiAPIAI/hiapi-icon-skills)

Generates consistent icon sets for apps, websites, and product features, supporting sheets, standalone PNGs, revisions, and transparency preparation.

- **Author:** [HiAPIAI](https://github.com/HiAPIAI)
- **Input:** One to twenty icon subjects; optional style, palette, output mode, background, and reference character
- **Output:** A multi-icon sheet or one 1:1 image per subject, with request, jobs, manifest, and QC state
- **ImageGen role:** The local CLI builds deterministic jobs; each visual is delegated to Codex built-in `image_gen`
- **Structure:** A compact skill, ten styles, five palettes, planning/registration/QC CLIs, examples, and tests
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>hiapi-icon-skills</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/hiapi-icon-skills/01-architecture-cafe.png"><img src="examples/hiapi-icon-skills/01-architecture-cafe.png" alt="hiapi-icon-skills — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/hiapi-icon-skills/02-mountain-lake.png"><img src="examples/hiapi-icon-skills/02-mountain-lake.png" alt="hiapi-icon-skills — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/hiapi-icon-skills/03-portrait-camera-duo.png"><img src="examples/hiapi-icon-skills/03-portrait-camera-duo.png" alt="hiapi-icon-skills — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/hiapi-icon-skills/04-animal-cat-dog.png"><img src="examples/hiapi-icon-skills/04-animal-cat-dog.png" alt="hiapi-icon-skills — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Identity Skill](https://github.com/Sac-Y/identity-skill)

An image-first personal-site workflow that generates and locks section references before extracting assets, implementing, and validating the site.

- **Author:** [Sac-Y](https://github.com/Sac-Y)
- **Input:** A résumé, LinkedIn profile, project links, personal narrative, references, or a style direction
- **Output:** Section references, render contract, asset manifest, responsive site, fidelity ledger, and QA screenshots
- **ImageGen role:** Prefers `imagegen-frontend-web`; otherwise uses a bundled adapter for references and approved assets
- **Structure:** An approximately 480-line workflow, eight references, twelve samples, and an evidence validator
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>identity-skill</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/identity-skill/01-architecture-cafe.png"><img src="examples/identity-skill/01-architecture-cafe.png" alt="identity-skill — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/identity-skill/02-mountain-lake.png"><img src="examples/identity-skill/02-mountain-lake.png" alt="identity-skill — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/identity-skill/03-portrait-camera-duo.png"><img src="examples/identity-skill/03-portrait-camera-duo.png" alt="identity-skill — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/identity-skill/04-animal-cat-dog.png"><img src="examples/identity-skill/04-animal-cat-dog.png" alt="identity-skill — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<a id="game-assets--characters"></a>
## Game Assets & Characters

### [Hatch Pet](https://github.com/openai/skills/tree/main/skills/.curated/hatch-pet)

Creates an animatable pet from a concept or reference. ImageGen supplies the base look and actions; deterministic scripts handle layout, slicing, mirroring, validation, atlases, and previews.

- **Author:** [OpenAI](https://github.com/openai)
- **Input:** A pet concept, brand cues, product name, or character references; name, description, and style may be inferred
- **Output:** An 8×9 atlas, `spritesheet.webp`, `pet.json`, contact sheet, GIF preview, and validation records
- **ImageGen role:** Composes `$imagegen` for the character and action rows, then scripts transparency, slicing, atlasing, QA, and packaging
- **Structure:** `SKILL.md`, metadata, references, complete spritesheet/validation scripts, and `LICENSE.txt`
- **License:** Apache-2.0

<p><strong>🖼️ Samples</strong> · <code>hatch-pet</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/hatch-pet/01-architecture-cafe.png"><img src="examples/hatch-pet/01-architecture-cafe.png" alt="hatch-pet — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/hatch-pet/02-mountain-lake.png"><img src="examples/hatch-pet/02-mountain-lake.png" alt="hatch-pet — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/hatch-pet/03-portrait-camera-duo.png"><img src="examples/hatch-pet/03-portrait-camera-duo.png" alt="hatch-pet — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/hatch-pet/04-animal-cat-dog.png"><img src="examples/hatch-pet/04-animal-cat-dog.png" alt="hatch-pet — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Character Sprite Maker](https://github.com/Clad3815/character-sprite-maker)

A character-sprite and animation-row workflow focused on consistency, strict chroma backgrounds, task-state tracking, and validation.

- **Author:** [Clad3815](https://github.com/Clad3815)
- **Input:** A character concept, style, animation list, frame count, cell size, viewpoint, and optional references
- **Output:** Configurable PNG/WebP spritesheets, frames, a contact sheet, GIF preview, and `character.json`
- **ImageGen role:** Uses `$imagegen` for the baseline, action rows, and repairs; scripts perform deterministic processing and validation
- **Structure:** `SKILL.md`, `agents/`, `references/`, `scripts/`, `examples/`, and `LICENSE.txt`
- **License:** Apache-2.0

<p><strong>🖼️ Samples</strong> · <code>character-sprite-maker</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/character-sprite-maker/01-architecture-cafe.png"><img src="examples/character-sprite-maker/01-architecture-cafe.png" alt="character-sprite-maker — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/character-sprite-maker/02-mountain-lake.png"><img src="examples/character-sprite-maker/02-mountain-lake.png" alt="character-sprite-maker — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/character-sprite-maker/03-portrait-camera-duo.png"><img src="examples/character-sprite-maker/03-portrait-camera-duo.png" alt="character-sprite-maker — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/character-sprite-maker/04-animal-cat-dog.png"><img src="examples/character-sprite-maker/04-animal-cat-dog.png" alt="character-sprite-maker — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Generating Dot Assets](https://github.com/abagames/agentic-gamedev-skills/tree/main/.agents/skills/generating-dot-assets)

An ImageGen skill for game objects, props, icons, and transparent-background pixel assets.

- **Author:** [abagames](https://github.com/abagames)
- **Input:** One object, target pixel dimensions, and output path; optional style, palette, color count, chroma key, and fit mode
- **Output:** An exact-size transparent pixel asset plus prompt, raw, cutout, and pixelized intermediates
- **ImageGen role:** Generates a high-resolution source with built-in `image_gen`, then uses ImageMagick for cutout, pixelization, fitting, and validation
- **Structure:** `SKILL.md`, an ImageGen recovery reference, and cutout/pixelize/fit/validate scripts
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>generating-dot-assets</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/generating-dot-assets/01-architecture-cafe.png"><img src="examples/generating-dot-assets/01-architecture-cafe.png" alt="generating-dot-assets — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/generating-dot-assets/02-mountain-lake.png"><img src="examples/generating-dot-assets/02-mountain-lake.png" alt="generating-dot-assets — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/generating-dot-assets/03-portrait-camera-duo.png"><img src="examples/generating-dot-assets/03-portrait-camera-duo.png" alt="generating-dot-assets — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/generating-dot-assets/04-animal-cat-dog.png"><img src="examples/generating-dot-assets/04-animal-cat-dog.png" alt="generating-dot-assets — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Minecraft Image Generation](https://github.com/Jahrome907/minecraft-agent-skills/tree/main/.codex/skills/minecraft-imagegen)

Generates pack concepts, banners, marketplace thumbnails, texture look-dev, server branding, and HUD/menu mockups for Minecraft projects.

- **Author:** [Jahrome907](https://github.com/Jahrome907)
- **Input:** Project context, asset type, theme, style, and use; optional existing packs, textures, or brand references
- **Output:** `pack.png` concepts, banners, thumbnails, texture look-dev, branding, UI mockups, and briefs
- **ImageGen role:** Calls built-in `image_gen` by default; generated textures are concepts for a manual pixel pass
- **Structure:** An approximately 190-line skill, prompt patterns, recipes, a brief scaffold, and handoff guidance
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>minecraft-imagegen</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/minecraft-imagegen/01-architecture-cafe.png"><img src="examples/minecraft-imagegen/01-architecture-cafe.png" alt="minecraft-imagegen — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/minecraft-imagegen/02-mountain-lake.png"><img src="examples/minecraft-imagegen/02-mountain-lake.png" alt="minecraft-imagegen — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/minecraft-imagegen/03-portrait-camera-duo.png"><img src="examples/minecraft-imagegen/03-portrait-camera-duo.png" alt="minecraft-imagegen — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/minecraft-imagegen/04-animal-cat-dog.png"><img src="examples/minecraft-imagegen/04-animal-cat-dog.png" alt="minecraft-imagegen — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Sprite Pipeline](https://github.com/openai/plugins/tree/main/plugins/game-studio/skills/sprite-pipeline)

An official OpenAI game-studio skill that generates action strips from an approved character or seed, then normalizes, slices, aligns, and previews them deterministically.

- **Author:** [OpenAI](https://github.com/openai)
- **Input:** An approved seed frame, target action, frame count, dimensions, and alignment requirements
- **Output:** Normalized frames, action strips, and preview sheets ready for a game pipeline
- **ImageGen role:** Uses an installed general `imagegen` skill for a full action row while this skill supplies game constraints
- **Structure:** `SKILL.md`, metadata, a workflow reference, and canvas, normalization, and preview scripts
- **License:** No open-source license declared upstream

<p><strong>🖼️ Samples</strong> · <code>sprite-pipeline</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/sprite-pipeline/01-architecture-cafe.png"><img src="examples/sprite-pipeline/01-architecture-cafe.png" alt="sprite-pipeline — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/sprite-pipeline/02-mountain-lake.png"><img src="examples/sprite-pipeline/02-mountain-lake.png" alt="sprite-pipeline — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/sprite-pipeline/03-portrait-camera-duo.png"><img src="examples/sprite-pipeline/03-portrait-camera-duo.png" alt="sprite-pipeline — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/sprite-pipeline/04-animal-cat-dog.png"><img src="examples/sprite-pipeline/04-animal-cat-dog.png" alt="sprite-pipeline — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<a id="storyboards--visual-narratives"></a>
## Storyboards & Visual Narratives

### [Agentara Cinematic Visual Skills](https://github.com/agentara/skills/tree/main/skills/aigc)

A paired poster and storyboard workflow that turns video-project context into 3:4 key art and timed 3×3, 4×3, or 4×4 boards.

- **Author:** [agentara](https://github.com/agentara)
- **Input:** A video plan, story brief, character references, existing boards, product or brand assets, or a prior poster
- **Output:** A poster with optional spec, or storyboard scenes plus a video-generation script
- **ImageGen role:** Uses built-in `image_gen` by default and prioritizes available character and storyboard references
- **Structure:** Two standalone workflows: `video-poster-design` and `video-storyboard`
- **License:** MIT

<p><strong>🖼️ Samples</strong> · <code>video-poster-design</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/video-poster-design/01-architecture-cafe.png"><img src="examples/video-poster-design/01-architecture-cafe.png" alt="video-poster-design — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/video-poster-design/02-mountain-lake.png"><img src="examples/video-poster-design/02-mountain-lake.png" alt="video-poster-design — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/video-poster-design/03-portrait-camera-duo.png"><img src="examples/video-poster-design/03-portrait-camera-duo.png" alt="video-poster-design — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/video-poster-design/04-animal-cat-dog.png"><img src="examples/video-poster-design/04-animal-cat-dog.png" alt="video-poster-design — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<p><strong>🖼️ Samples</strong> · <code>video-storyboard</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/video-storyboard/01-architecture-cafe.png"><img src="examples/video-storyboard/01-architecture-cafe.png" alt="video-storyboard — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/video-storyboard/02-mountain-lake.png"><img src="examples/video-storyboard/02-mountain-lake.png" alt="video-storyboard — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/video-storyboard/03-portrait-camera-duo.png"><img src="examples/video-storyboard/03-portrait-camera-duo.png" alt="video-storyboard — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/video-storyboard/04-animal-cat-dog.png"><img src="examples/video-storyboard/04-animal-cat-dog.png" alt="video-storyboard — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

### [Storyboard Skill](https://github.com/abel-vs/storyboard-skill)

A community skill for building storyboards and continuous visual narratives with imagegen.

- **Author:** [abel-vs](https://github.com/abel-vs)
- **Input:** A built, planned, or conceptual product; features from code, specs, or conversation; optional design references
- **Output:** Interactive HTML, GitHub-renderable Markdown, JSON, and per-feature storyboard images
- **ImageGen role:** Generates frames in parallel through an imagegen CLI; this is an API-key CLI path, not built-in-only
- **Structure:** `SKILL.md`, `assets/template.html`, `references/styles.md`, and `evals/evals.json`
- **License:** No open-source license declared upstream

<p><strong>🖼️ Samples</strong> · <code>storyboard-skill</code></p>

<table>
  <tr>
    <td width="25%" align="center"><a href="examples/storyboard-skill/01-architecture-cafe.png"><img src="examples/storyboard-skill/01-architecture-cafe.png" alt="storyboard-skill — architecture café" width="100%"></a><br><code>architecture-cafe</code></td>
    <td width="25%" align="center"><a href="examples/storyboard-skill/02-mountain-lake.png"><img src="examples/storyboard-skill/02-mountain-lake.png" alt="storyboard-skill — mountain lake" width="100%"></a><br><code>mountain-lake</code></td>
    <td width="25%" align="center"><a href="examples/storyboard-skill/03-portrait-camera-duo.png"><img src="examples/storyboard-skill/03-portrait-camera-duo.png" alt="storyboard-skill — portrait camera duo" width="100%"></a><br><code>portrait-camera-duo</code></td>
    <td width="25%" align="center"><a href="examples/storyboard-skill/04-animal-cat-dog.png"><img src="examples/storyboard-skill/04-animal-cat-dog.png" alt="storyboard-skill — cat and dog" width="100%"></a><br><code>animal-cat-dog</code></td>
  </tr>
</table>

<a id="sample-inputs--reproduction"></a>
## Sample Inputs & Reproduction

### Source images

All four inputs were generated or edited with the system `imagegen` skill. Repository-relative paths keep them visible in forks, clones, and on GitHub.

<table>
  <tr>
    <td width="25%" align="center">
      <a href="fixtures/01-architecture-cafe.png"><img src="fixtures/01-architecture-cafe.png" alt="imagegen — architecture-cafe" width="100%"></a><br>
      <code>imagegen / 01-architecture-cafe</code>
    </td>
    <td width="25%" align="center">
      <a href="fixtures/02-mountain-lake.png"><img src="fixtures/02-mountain-lake.png" alt="imagegen — mountain-lake" width="100%"></a><br>
      <code>imagegen / 02-mountain-lake</code>
    </td>
    <td width="25%" align="center">
      <a href="fixtures/03-portrait-camera-duo.png"><img src="fixtures/03-portrait-camera-duo.png" alt="imagegen — portrait-camera-duo" width="100%"></a><br>
      <code>imagegen / 03-portrait-camera-duo</code>
    </td>
    <td width="25%" align="center">
      <a href="fixtures/04-animal-cat-dog.png"><img src="fixtures/04-animal-cat-dog.png" alt="imagegen — animal-cat-dog" width="100%"></a><br>
      <code>imagegen / 04-animal-cat-dog</code>
    </td>
  </tr>
</table>

Outputs live under `examples/<skill-id>/`. Directory names match skill IDs and filenames match the input scenes. When a skill requires several directions, they are combined into one scene board so the README still shows one image per input.

<a id="contributing"></a>
## Contributing

### Curation

Projects are preferred when they:

- Target Codex directly or can be discovered and run in Codex
- Use harness built-in `image_gen` by default, or clearly document composition with a general imagegen skill
- Provide a reusable method or workflow rather than one prompt
- Publish a reviewable `SKILL.md` and usage guide, preferably with an output example
- Explain inputs, outputs, use cases, and limitations
- State a clear license
- Can be traced to the original author repository

Projects are usually excluded when they:

- Merely wrap a third-party image API without a Codex workflow
- Primarily use SVG, Canvas, HTML/CSS, or local drawing libraries
- Offer only prompt screenshots without reviewable source
- Are unattributed copies or violate upstream licensing
- Have only a weak connection to image generation

### Submit a skill

Issues and pull requests are welcome. A useful submission includes the project name and original repository, a short description, author, inputs and outputs, the role of `image_gen`, package structure, examples, license, and why it belongs here.

Suggested format:

```md
### [Skill Name](https://github.com/owner/repo)

One sentence explaining the visual task.

- **Author:** [owner](https://github.com/owner)
- **Input:** ...
- **Output:** ...
- **ImageGen role:** ...
- **Structure:** ...
- **License:** ...
```

## Disclaimer

“Awesome” means worth studying or using; it is not an endorsement of security, stability, output quality, or licensing scope. Review third-party source and licenses before installation. GitHub visibility does not imply permission to copy, modify, or use a project commercially.

<a id="related-collections"></a>
## Related Collections

These broader collections help discover candidates and understand the Agent Skills ecosystem. Inclusion there does not imply compliance with this repository's ImageGen, example, or licensing standards.

<a id="official-foundations"></a>
### Official Foundations

- [Image Generation Skill](https://github.com/openai/skills/tree/main/skills/.system/imagegen) — General Codex imagegen skill and its generation, editing, prompting, saving, and review rules.
- [Codex bundled imagegen sample](https://github.com/openai/codex/tree/main/codex-rs/skills/src/assets/samples/imagegen) — Bundled sample in the Codex source tree.
- [OpenAI Plugins](https://github.com/openai/plugins) — Current official plugin and skill examples.
- [Build skills](https://learn.chatgpt.com/docs/build-skills) — Official Skills and `SKILL.md` documentation.
- [Save workflows as skills](https://learn.chatgpt.com/use-cases/reusable-codex-skills) — Official reusable Codex skill workflow.
- [Get from idea to proof of concept](https://learn.chatgpt.com/use-cases/idea-to-proof-of-concept) — Official ImageGen prototyping workflow.

> The `openai/skills` repository is deprecated. Prefer `openai/plugins` and `openai/codex` for current official examples.

### Skills discovery

- [Awesome Codex Skills](https://github.com/composio-community/awesome-codex-skills) — A broad Codex skills collection.
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) — A large cross-runtime directory with dedicated OpenAI sections.
- [Agent Skill Index](https://github.com/heilcheng/awesome-agent-skills) — A multilingual guide and index across runtimes.
- [skills.sh](https://skills.sh) / [vercel-labs/skills](https://github.com/vercel-labs/skills) — A searchable ranking and installation CLI.

### Design and plugin ecosystem

- [Awesome Design Skills](https://github.com/bergside/awesome-design-skills) — Design-system and `SKILL.md` / `DESIGN.md` resources focused mainly on UI and design language.
- [Awesome Codex & ChatGPT Plugins](https://github.com/hashgraph-online/awesome-codex-plugins) — A broader collection of Codex plugins, skills, and resources.

