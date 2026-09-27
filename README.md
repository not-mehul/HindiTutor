# HindiTutor: 40-Day Verbal Hindi for Russian Speakers

An interactive, Duolingo-style learning platform and curriculum designed for native Russian speakers to acquire spoken conversational Hindi in **40 daily 20-minute sessions** (0 to B1 conversational threshold).

Includes an **English / Russian audit toggle** allowing non-Russian instructors and auditors to review and verify all educational content, translations, grammar bridges, and exercises in English.

---

## 🌟 Key Highlights & Pedagogical Architecture

1. **Applied Contrastive Linguistics (Russian ↔ Hindi)**:
   - **Positive Transfer**: Exploits identical alveolar rolling [р]/[r] and pure monophthongs [а, и, у, э, о] without English-style diphthongization.
   - **Anti-Akan'ye (Анти-аканье)**: Systematic training to prevent Russian vowel reduction in unstressed grammatical endings (`-ā`, `-ī`, `-ē`).
   - **Dental vs. Retroflex**: Clear tactile contrast between dental (*т, д* on teeth) and retroflex (*т͟, д͟* curled back to the palate).
   - **Dative Experiencer Bridge**: Anchoring Hindi *mujhe pasand hai* / *mujhe cāhiye* to Russian *мне нравится* / *мне нужно*.
   - **PIE Cognates Bridge**: Leveraging 5,000-year-old Proto-Indo-European shared roots (*дверь ↔ dvār*, *огонь ↔ agni*, *два ↔ do*, *брат ↔ bhrātā*).

2. **Bilingual Audit Mode (EN ↔ RU)**:
   - Learners use the immersive **Russian Mode (`ru`)**.
   - Reviewers, creators, and auditors can instantly switch to **English Mode (`en`)** at any moment via the top navbar or settings to verify instructions, target phrases, grammar mechanics, and simulation dialogues.

3. **Responsive Mobile & Desktop Design**:
   - **Mobile Viewport**: Fixed bottom navigation bar with tactile touch targets (>= 48px), responsive serpentine learning trail, and thumb-friendly word reordering chips.
   - **Desktop Viewport**: Sticky sidebar, spacious multi-column layout, and minimal pairs sound lab.

4. **Hybrid Studio-Grade Audio Engine**:
   - **420+ Pre-rendered Neural MP3s**: Synthesized using Microsoft Azure Neural Hindi (`hi-IN-SwaraNeural`) via `edge-tts` for 100% crystal-clear native phonetics on every device and operating system (zero robotic artifacts).
   - **Covered Assets**: All 172 curriculum vocabulary words, phonetics minimal pairs (*tāl/ṭāl*, *sāt/sāth*, *kam/kām*, *phal/pal*), individual retroflex/dental phonemes, PIE cognates, and essential conversational cues.
   - **Intelligent Fallback**: Seamlessly falls back to an upgraded Web Speech API with voice preloading and neural voice prioritization (`Google हिन्दी` / `Swara Neural`) for dynamic text.
   - **Synthesized UI Sound Effects**: Web Audio API generates celebratory chimes, error buzzes, and fanfare with zero network delay.

---

## 🚀 Quick Start (Web Application)

```bash
# Navigate to web application directory
cd web

# Install dependencies (React 19, TypeScript, Tailwind CSS v4, Lucide React, Canvas Confetti)
npm install

# Start local development server
npm run dev

# Or build and test production bundle
npm run build
npm run preview
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## 📁 Repository Structure

```text
HindiTutor/
├── content/
│   ├── course_manifest.json          # Master 40-day manifest and metadata
│   ├── phonetics_guide.json          # Articulatory mechanics, warnings, and minimal pairs
│   ├── cognates_index.json           # PIE cognates dictionary (Russian <-> Hindi)
│   └── days/
│       ├── day_01.json               # Structured daily modules (Day 01 to Day 40)
│       └── ...
├── dist/
│   ├── hindi_course_bundle.json      # Machine-parsable JSON bundle of full course
│   └── courseBundle.ts               # Bundled TypeScript module
├── docs/
│   ├── curriculum_overview.md        # Comprehensive curriculum guide
│   └── phases/                       # Detailed Phase 1 to Phase 5 documentation
├── schema/
│   ├── course_schema.json            # JSON Schema for course verification
│   └── types.ts                      # Core TypeScript interfaces
├── scripts/
│   ├── generate_course.py            # Automated content generator for 40 days
│   └── validate_course.py            # Automated schema & data validator (Passed 40/40)
└── web/                              # Duolingo-like React 19 + TypeScript + Tailwind web app
    ├── src/
    │   ├── components/
    │   │   ├── Navbar.tsx            # Top header with stats & EN/RU toggle
    │   │   ├── Sidebar.tsx           # Desktop navigation sidebar
    │   │   ├── BottomNav.tsx         # Mobile bottom navigation bar
    │   │   ├── RoadmapView.tsx       # Serpentine Duolingo learning path & modal
    │   │   ├── LessonRunner.tsx      # 4-stage interactive lesson engine
    │   │   ├── PhoneticsGym.tsx      # Consonant soundboard & minimal pairs lab
    │   │   ├── CognatesExplorer.tsx  # Searchable PIE root cognate dictionary
    │   │   └── SettingsView.tsx      # Language, gender, script & progress settings
    │   ├── context/
    │   │   └── AppContext.tsx        # Global state (hearts, XP, streak, localization)
    │   ├── utils/
    │   │   └── audio.ts              # Web Speech TTS + Web Audio synth effects
    │   └── data/
    │       └── courseBundle.ts       # Bundled curriculum data
    └── package.json
```

---

## ⏱️ Daily 20-Minute Cognitive Protocol

Every daily lesson is engineered with a strict 4-phase cognitive rhythm:
1. **00:00–04:00 (Phase 1)**: Phonetic Calibration & Spaced Retrieval (minimal pairs, retroflexion, aspiration check).
2. **04:00–11:00 (Phase 2)**: Structural Core & Cognitive Anchoring (SOV word order, dative experiencers, postpositions).
3. **11:00–17:00 (Phase 3)**: Interactive Drills & Shadowing (tactile word chips, rapid oral challenges).
4. **17:00–20:00 (Phase 4)**: Real-world Simulation & Roleplay (contextual Indian travel dialogues).

---

## 🌐 Free Production Hosting Guide

The web application is a static Single Page Application (Vite + React 19 + TypeScript + Tailwind CSS v4) with zero backend server dependencies and 1,241 pre-rendered studio neural MP3 audio files. You can host it for free online using any of the following recommended platforms:

### Option 1: Cloudflare Pages (Recommended for Audio Bandwidth)
* **Cost**: 100% Free with **Unlimited Bandwidth** (ideal for audio-heavy streaming).
* **Speed**: Ultra-fast edge CDN with POPs in Delhi, Mumbai, Chennai, Bengaluru, Moscow, and Europe.
* **Deploy Steps**:
  1. Push this repository to GitHub.
  2. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com) → **Workers & Pages** → **Create Application** → **Pages** → **Connect to Git**.
  3. Select your repository and set:
     - **Framework preset**: `Vite`
     - **Root directory**: `web`
     - **Build command**: `npm run build`
     - **Build output directory**: `dist`
  4. Click **Save and Deploy**. Your site will be live at `https://<your-project>.pages.dev` with free SSL and custom domain support.

### Option 2: Vercel (Fastest 1-Command CLI Deployment)
* **Cost**: 100% Free (Hobby tier).
* **Deploy Steps**:
  ```bash
  # Inside web/ directory
  cd web
  npx vercel
  ```
  Follow the simple interactive prompts (accept defaults). Vercel will build and deploy your project instantly to a `https://<project-name>.vercel.app` domain.

### Option 3: GitHub Pages (Automated via GitHub Actions)
* **Cost**: 100% Free directly within GitHub.
* **Pre-configured**: This repository includes a turnkey `.github/workflows/deploy.yml` workflow.
* **Deploy Steps**:
  1. Push this repository to GitHub:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git remote add origin https://github.com/<your-username>/HindiTutor.git
     git push -u origin main
     ```
  2. In your GitHub repository, navigate to **Settings** → **Pages**.
  3. Under **Build and deployment** → **Source**, select **GitHub Actions**.
  4. The workflow will run automatically and deploy your site to `https://<your-username>.github.io/HindiTutor/`.

### Option 4: Netlify (Instant Drag-and-Drop)
* **Cost**: 100% Free.
* **Deploy Steps**:
  1. Build the production bundle locally: `cd web && npm run build`.
  2. Open [app.netlify.com/drop](https://app.netlify.com/drop) in your browser.
  3. Drag and drop the `web/dist` folder directly onto the page. Your site will be live in 10 seconds!

