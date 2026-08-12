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
  },
  {
    day: 1,
    date: "2026-08-11",
    weekday: "Tuesday",
    journal: "Today was supposed to be the first proper day of my new routine, and honestly… it did not start the way I had planned. I woke up way later than I was supposed to, mainly because I had stayed up late working on my website, even though I already knew that a completely new routine was starting from today. So yeah, great start. 😂 After finally getting out of bed, I started the morning with some basic things, made lemon water, prepared breakfast, and then got back to my laptop. I spent some time working on Google AI Studio and then shifted my focus towards academics. Since I’m currently a first-year B.Com Honours student at Delhi University, I really want to build a strong academic base from the beginning, so today I studied Business Law and watched the lecture for quite some time. I also checked my schedule and tried to figure out how much of today’s plan I could realistically finish. Later, I decided to start my AI automation learning session as well, but by that point it had already gotten pretty late. I knew that if I started the entire class properly, I would probably end up sitting there till midnight, so I decided to leave today’s AI automation target for tomorrow. Not completed today, but kal pakka. 😭 Apart from academics and work, my health was also not exactly on my side today. I’m still dealing with an injury on my foot, so I couldn’t go running or do my proper workout. In the evening, I also had to visit the medical centre to get my bandage changed, and bhai… when they started removing the old bandage, I swear for a second Yamraj dikh gaye the. 😂😭 That shit hurt. So overall, today was definitely not the perfect start I had imagined. I woke up late, a big part of the routine got messed up, the AI automation target was left incomplete, and the workout/running had to be skipped because of my health. But at the same time, I did get some academic work done, spent time learning, worked on my website, and most importantly, I actually started documenting this journey. College is also starting in just two days, and most of the preparations are already done, so from here things are going to get a lot more real. I’m trying to balance academics, AI automation, fitness, college and everything else at the same time, and I already know that every single day is not going to go perfectly. Maybe some days will be amazing, maybe some days will be complete shit. 😂 But that’s exactly why I’m documenting all of this. I don’t want to remember only the successful days later. I want to remember the late mornings, missed targets, random meals, boring study sessions, injuries, small wins, bad days and everything in between. Day 01 wasn’t perfect, but it happened. And that’s enough for today.",
    photos: [
      {
        src: "media/journal-1786542516506-nkzyx.webp",
        caption: ""
      },
      {
        src: "media/journal-1786542517131-tbi63.png",
        caption: ""
      },
      {
        src: "media/journal-1786542517612-owoa0.png",
        caption: ""
      },
      {
        src: "media/journal-1786542518221-kiq5m.png",
        caption: ""
      },
      {
        src: "media/journal-1786542518856-fzjxx.webp",
        caption: ""
      }
    ],
    discipline: 0,
    mediaCaption: "Stayed home all day today"
  }
];
window.UNFILTERED_ENTRIES = UNFILTERED_ENTRIES;