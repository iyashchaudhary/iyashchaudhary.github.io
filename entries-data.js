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
    journal: "Day one of the documentary — and the day the website got its second world.\n\nToday was supposed to be the beginning of a completely new routine, but honestly, it didn’t exactly go according to plan. I woke up much later than I wanted to, which messed up a good part of the schedule. I still managed to spend some time on academics and Business Law, but the AI automation target had to be pushed to tomorrow. With my health being a little down and an injury on my foot, I also had to skip running and most of the workout.\n\nStill, the day wasn’t completely wasted. I got some important things done, documented the little moments, and started something I’ve been thinking about for a while.\n\nUnfiltered Yash went live today — a corkboard journal where every day gets pinned like a real memory, one big note at a time. YouTube documenting also starts today, side by side with this page.\n\nNervous but excited. New place, new routine, mixed feelings of everything at once. The plan is simple now: show up every day, write it down, post it.\n\nNo filter.",
    photo: {
      src: "",
      caption: ""
    },
    documentary: {
      youtubeUrl: "https://youtu.be/fYYwyrSpPZ0",
      title: "Day 01 — The 180-Day Experiment | Starting From Zero",
      thumbnail: "https://i.ytimg.com/vi/fYYwyrSpPZ0/hqdefault.jpg"
    }
  }
];
window.UNFILTERED_ENTRIES = UNFILTERED_ENTRIES;