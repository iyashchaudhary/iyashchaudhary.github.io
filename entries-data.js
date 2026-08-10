/* ============================================================
   UNFILTERED YASH — DAILY ENTRIES DATA
   ============================================================
   This file is the entire "database". Each object in the array
   below is one day. To add a new day, copy one entry, change
   the values, and add a comma between entries.

   EVERY FIELD EXCEPT day/date IS OPTIONAL — leave a section out
   entirely (or set it to null) on days where it doesn't apply.
   A lazy day can be just { day, date, dateLabel, weekday, fiveLines }.
   ============================================================ */

const UNFILTERED_ENTRIES = [
  {
    day: 1,
    date: "2026-08-14",
    dateLabel: "14 August 2026",
    weekday: "Friday",
    title: "The day I started again.",

    // Sticky-note cards. type controls the color + icon.
    // Valid types: college, workout, study, work, mood, note (blank/custom)
    cards: [
      { type: "college", label: "College", text: "First day at ARSD. New place, new faces, mixed feeling of excitement & nervousness." },
      { type: "workout", label: "Workout", text: "After a long break, finally hit the gym. Felt heavy in the beginning but happy I showed up." },
      { type: "study",   label: "Study",   text: "Basics of Financial Accounting revision. Long way to go with ACCA, but step 1 is done." },
      { type: "work",    label: "Work",    text: "Worked on website improvements and planned the YouTube documentary format." },
      { type: "mood",    label: "Mood",    text: "Nervous + Excited + Hopeful. Let's see where this journey takes me.", emoji: "🙂" }
    ],

    photo: { src: "", caption: "Beautiful sunset on the first day" },

    fiveLines: [
      "Woke up early and felt motivated.",
      "College was overwhelming but good.",
      "Gym was tough but felt great after.",
      "Worked on my website a lot.",
      "Tomorrow: continue the momentum."
    ],

    reminder: [
      "Wake up early",
      "College notes",
      "Gym (don't skip)",
      "ACCA 2 hours",
      "Edit Day 02 video"
    ],

    stats: { productivity: 6, energy: 7, focus: 6, happiness: 8 },

    documentary: {
      title: "Starting Again",
      youtubeUrl: "",
      duration: "12:47",
      thumb: ""
    },

    tags: ["firstday", "college", "gym", "website", "restart", "newbeginning"],

    quote: { text: "The best way to predict your future is to create it.", author: "Abraham Lincoln" }
  }
];
window.UNFILTERED_ENTRIES = UNFILTERED_ENTRIES; // expose globally for the page renderer

