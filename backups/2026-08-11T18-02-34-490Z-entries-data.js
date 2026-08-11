/* ============================================================
   UNFILTERED YASH — DAILY ENTRIES DATA (v2 — corkboard)
   ============================================================
   This file is the entire "database". Each object in the array
   below is one day. To add a new day, copy one entry, change
   the values, and put a comma after the closing } of the day
   before it.

   NEW SIMPLE MODEL:
   - day / date / weekday : always required
   - journal              : the big pinned sticky note — the whole day
                            in 1-2 free paragraphs (plain text; blank
                            line between paragraphs)
   - photo (optional)     : { src: "filename", caption: "..." }
   - documentary (optional): only youtubeUrl — title, duration and
                            thumbnail are fetched automatically

   A lazy day can be just:
     { day: 2, date: "2026-08-12", weekday: "Wednesday", journal: "..." }
   ============================================================ */

const UNFILTERED_ENTRIES = [
  {
    day: 1,
    date: "2026-08-11",
    weekday: "Tuesday",
    journal: "Day one of the documentary \u2014 and the day the website got its second world. Unfiltered Yash went live: a corkboard journal where every day gets pinned like a real memory, one big note at a time. YouTube documenting also starts today, side by side with this page.\n\nNervous but excited. New place, new routine, mixed feeling of everything at once. The plan is simple now: show up every day, write it down, post it. No filter.",
    photo: { src: "", caption: "" },
    documentary: { youtubeUrl: "" }
  }
];
window.UNFILTERED_ENTRIES = UNFILTERED_ENTRIES; // expose globally for the page renderer
