/* ============================================================
   PORTFOLIO DATA — JOURNEY, EXPERIENCE, FOCUS, CREDENTIALS, SKILLS
   ============================================================ */

// ---------- JOURNEY ----------
// ---------- JOURNEY ----------
// ---------- JOURNEY ----------
// ---------- JOURNEY ----------
const JOURNEY_DATA = [
  {
    title: "B.A. Economics — Sri Venkateswara College, DU",
    date: "Aug 2025 – Aug 2026",
    paragraphs: [
      "Started a B.A. Economics after CUET 2025. A few months in, my interest in the course kept dropping — it wasn't matching where I actually wanted to go with finance.",
      "So I made the call to sit CUET again — a harder decision than it sounds, since most people in the same spot were told to just \"adjust\" for two more years."
    ],
    images: [
      {
        src: "venky-4.webp",
        alt: "Sri Venkateswara College campus"
      },
      {
        src: "venky-5.webp",
        alt: "Live at a concert"
      },
      {
        src: "venky-6.webp",
        alt: "College fest night event"
      },
      {
        src: "venky-2.webp",
        alt: "With friends at Sri Venkateswara College"
      },
      {
        src: "venky-3.webp",
        alt: "On a college trip"
      },
      {
        src: "venky-1.webp",
        alt: "A quieter moment during that year"
      }
    ]
  },
  {
    title: "Retook CUET — By Choice",
    date: "Jan 2026",
    paragraphs: [
      "Alongside the B.A. Economics, I was also pursuing a B.Com (Hons) dual degree through DU SOL — and it was going well, unlike the main course. That gap told me exactly what to fix.",
      "I went back into full CUET preparation while still attending regular classes, aiming for a straightforward B.Com (Hons) seat this time — no more mismatch between course and goal."
    ]
  },
  {
    title: "B.Com (Hons) — Atma Ram Sanatan Dharma College, DU",
    date: "Jul 2026 – 2029",
    paragraphs: [
      "Secured a B.Com (Hons) seat at ARSD — the exact course I'd been trying to reach since the beginning. The parallel B.Com (Hons) from DU SOL was withdrawn once this was confirmed, since two degrees can't run at once within DU.",
      "This is where the real build starts: building finance and automation skills around the degree."
    ]
  },
  {
    title: "A NEW JOURNEY BEGINS ",
    date: "14th August 2026",
    paragraphs: [
      "Today was the first day of a new chapter. A new college, a new environment, new people, and honestly, a completely different phase of life. It feels strange to think about how much has changed and how much is still waiting to happen. I don't know exactly where this journey will take me, but this is where I'm starting again — with a fresh college life, new goals, and a lot of things I want to build over the next six months. Maybe one day I'll look back at this first day and realize just how much changed from here."
    ]
  }
];
window.JOURNEY_DATA = JOURNEY_DATA;

// ---------- YASH OS / CURRENT STATE ----------
// Edit values here; the visual components do not need to change.
const YASH_OS_DATA = {
  title: "YASH OS",
  subtitle: "A live snapshot of the current chapter.",
  status: "Currently building",
  items: [
    { label: "Education", value: "B.Com (Hons.)", state: "active" },
    { label: "Current Focus", value: "Finance × Consulting", state: "active" },
    { label: "Exploring", value: "AI & Automation", state: "exploring" },
    { label: "Building", value: "Personal projects / future projects", state: "building" },
    { label: "Current Goal", value: "Build consistently and ship useful work", state: "editable" }
  ]
};
window.YASH_OS_DATA = YASH_OS_DATA;

// ---------- CURRENTLY ----------
// Keep this small snapshot current as life changes.
const CURRENTLY_DATA = [
  { label: "Studying", value: "B.Com (Hons.)" },
  { label: "Exploring", value: "Finance & Consulting" },
  { label: "Building", value: "AI / Automation / Personal Projects" },
  { label: "Learning", value: "n8n, AI workflows and practical finance" }
];
window.CURRENTLY_DATA = CURRENTLY_DATA;

// ---------- JOURNEY YEAR INDEX ----------
// Empty years intentionally stay empty; the UI shows “More chapters coming.”
const JOURNEY_YEAR_DATA = [
  { year: "2024", entries: [] },
  { year: "2025", entries: [
    { category: "Education", title: "B.A. Economics", text: "Started B.A. Economics at Sri Venkateswara College after CUET 2025." },
    { category: "Societies", title: "Design & content work", text: "Worked with Connecting Dreams Foundation SVC, ASCEND (E-Cell) and TEDxSVC." }
  ] },
  { year: "2026", entries: [
    { category: "Milestone", title: "Retook CUET by choice", text: "Went back into CUET preparation while continuing the academic year." },
    { category: "Education", title: "B.Com (Hons.) at ARSD", text: "Secured the B.Com (Hons.) seat at Atma Ram Sanatan Dharma College, DU." },
    { category: "Current chapter", title: "A new journey begins", text: "Started a new college chapter and began building around commerce, finance, creative work and automation." }
  ] },
  { year: "2027", entries: [] },
  { year: "Future", entries: [] }
];
window.JOURNEY_YEAR_DATA = JOURNEY_YEAR_DATA;

// ---------- EXPERIENCE ----------
const EXPERIENCE_DATA = [
  {
    role: "Design & Content Team Member",
    org: "Connecting Dreams Foundation SVC · Sri Venkateswara College",
    date: "Sep 2025 – Jul 2026 · 11 mos",
    desc: "Created posters and reels for the society's annual event."
  },
  {
    role: "Design & Content Team Member",
    org: "ASCEND (E-Cell) · Sri Venkateswara College",
    date: "Sep 2025 – Jul 2026 · 11 mos",
    desc: "Designed social media creatives and edited videos for the society's Instagram and events."
  },
  {
    role: "Design & Content Team Member",
    org: "TEDxSVC · Sri Venkateswara College",
    date: "Sep 2025 – Feb 2026 · 6 mos",
    desc: "Design and content support for an independently organized TEDx event."
  },
  {
    role: "Freelance Video Editor",
    org: "Self-Employed",
    date: "Jul 2025 – Feb 2026 · 8 mos",
    desc: "Edited 50+ videos generating 2M+ combined views across Instagram and YouTube."
  }
];
window.EXPERIENCE_DATA = EXPERIENCE_DATA;

// ---------- CURRENT FOCUS ----------
const FOCUS_DATA = {
  window: "2026 – 2027",
  items: [
    {
      label: "CGPA",
      value: "Target High",
      desc: "Full focus on a strong first-year academic record."
    },
    {
      label: "Client Work",
      value: "Ongoing",
      desc: "Video editing and design work continuing alongside the degree."
    },
    {
      label: "AI Automation",
      value: "Building",
      desc: "Learning Hands-on n8n and AI-agent skill-building, one project at a time."
    }
  ]
};
window.FOCUS_DATA = FOCUS_DATA;

// ---------- PURSUING ----------
const PURSUING_DATA = [];
window.PURSUING_DATA = PURSUING_DATA;

// ---------- CREDENTIALS ----------
const CREDENTIALS_DATA = {
  finance: [
    {
      title: "Goldman Sachs — Operations Job Simulation",
      status: "Completed",
      issuer: "Forage · August 2026",
      desc: "Completed a simulation modeled on an Operations Analyst role — analyzed financial data to identify trade settlement and asset transfer issues for ultra-high-net-worth clients, and worked across Trading, Compliance, and IT to resolve operational trade fails while applying risk management and regulatory compliance (KYC/AML) practices.",
      certImg: "credential-goldman-sachs.webp",
      certAlt: "Goldman Sachs Operations Job Simulation certificate — Yash Chaudhary",
      skills: [
        "Data Analysis",
        "Problem Solving",
        "Risk Management",
        "Transaction Management",
        "Process Improvement",
        "Cross-Functional Teams"
      ],
      verifyUrl: "https://www.theforage.com/completion-certificates/MBA4MnZTNFEoJZGnk/wNge9cjzNTXD2acrv_MBA4MnZTNFEoJZGnk_6a775096beeabacfe3675dcc_1786215893595_completion_certificate.pdf"
    }
  ],
  tech: [],
  strategy: [],
  marketing: [
    {
      title: "Video Editor & Banner Designer",
      status: "Ongoing",
      issuer: "Client — Some Clothing Brand",
      desc: "Handled visual identity for a clothing brand — promotional video edits and digital banners used across their Instagram to drive engagement."
    },
    {
      title: "Video Editing — AI-Assisted Workflow",
      status: "Ongoing Skill",
      issuer: "Self-Directed",
      desc: "Cinematic storytelling and short-form editing using CapCut, and AI-assisted tools."
    },
    {
      title: "Digital Poster & Graphic Design",
      status: "Ongoing Skill",
      issuer: "Self-Directed",
      desc: "Brand-consistent poster and banner design for social media, built alongside real client delivery work."
    }
  ]
};
window.CREDENTIALS_DATA = CREDENTIALS_DATA;

// ---------- SKILLS ----------
const SKILLS_DATA = [
  {
    title: "Finance",
    level: "Finance Fundamentals",
    desc: "Core accounting and financial reporting fundamentals, built through coursework and practical projects."
  },
  {
    title: "Excel",
    level: "Advanced",
    desc: "Advanced formulas, financial modeling structures, and data analysis for both coursework and client projects."
  },
  {
    title: "AI & Automation",
    level: "Building",
    desc: "Learning Hands-on with n8n, AI agents, and workflow automation for real business use cases."
  },
  {
    title: "Video Editing",
    level: "1.5 Years Experience",
    desc: "CapCut PC, and AI-assisted tools — cinematic storytelling and short-form content."
  }
];
window.SKILLS_DATA = SKILLS_DATA;