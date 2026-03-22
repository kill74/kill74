<div align="center">

```
██╗  ██╗██╗██╗     ██╗     ███████╗██╗  ██╗
██║ ██╔╝██║██║     ██║     ╚════██║██║  ██║
█████╔╝ ██║██║     ██║         ██╔╝███████║
██╔═██╗ ██║██║     ██║        ██╔╝ ╚════██║
██║  ██╗██║███████╗███████╗   ██║       ██║
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝   ╚═╝       ╚═╝
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1000&color=F7CF6E&center=true&vCenter=true&width=650&lines=Full-Stack+Engineer+%7C+Systems+Programmer;Writes+kernels+in+C+%26+ASM+%E2%80%94+ships+apps+in+React+%26+Rust;One+of+the+few+who+understands+both+ends+of+the+stack;Castelo+Branco%2C+Portugal+%F0%9F%87%B5%F0%9F%87%B9+%E2%80%94+building+globally;The+present+is+connected+to+the+past+and+future+%E2%80%94+Lain" alt="Typing SVG" />

<br/>

</div>

---

## `> whoami`

```sh
┌─[guilherme@kill74]─[~]
└──╼ $ cat /etc/profile.d/me.conf

  handle      →  kill74
  name        →  Guilherme
  location    →  Castelo Branco, Portugal 🇵🇹
  age         →  20

  education   →  Lic. Design Digital e Multimédia
                 Instituto Politécnico de Castelo Branco
  prior       →  TeSP Desenvolvimento Web e Multimédia  [grade: 15 ✓]

  stack       →  C · Assembly · Rust · Go · C# · JS/TS · Python · PHP · Lua
  layers      →  bare-metal kernels  →  systems daemons  →  REST APIs  →  UIs
  philosophy  →  understand the whole stack, own every layer

  status      →  [ BUILDING ] — always.
```

> Most developers live at one end of the stack.
> I build kernels *and* ship products — because you can't truly master one without understanding the other.

---

## `> ls -la ./projects --sort=impact`

> Production systems, open-source tools, and systems experiments. All shipped.

<br/>

<table>
<tr>
<td width="50%" valign="top">

### 🖥️ [TinyOS](https://github.com/kill74/TinyOS)
**Bare-metal x86 kernel — no stdlib, no libc, no safety net.**

Written from scratch in **C & Assembly**. Handles CPU protection rings (Ring 0/3), configures the GDT/IDT, implements a basic memory manager, and boots on real hardware. No dependencies. No OS beneath it. Just silicon and intent.

**What this proves:** I understand what happens *before* `main()`.

![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![Assembly](https://img.shields.io/badge/ASM-x86-grey?style=flat-square)
![Kernel](https://img.shields.io/badge/bare--metal-kernel-F7CF6E?style=flat-square&labelColor=0d1117)

</td>
<td width="50%" valign="top">

### 💬 [Chatify](https://github.com/kill74/Chatify)
**Real-time chat engine built in Rust — engineered for correctness.**

Channels, DMs, voice, file transfers, message editing, reactions, and presence tracking. Built with Rust's ownership model as the architecture — no data races by design, not by discipline.

**What this proves:** Systems thinking applied to networked, concurrent software.

![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Async](https://img.shields.io/badge/async-tokio-F7CF6E?style=flat-square&labelColor=0d1117)
![Networking](https://img.shields.io/badge/real--time-networking-grey?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 [PulseData](https://github.com/kill74/PulseData)
**Full-stack data engineering platform — from raw events to business insight.**

Built on **.NET 8 + PostgreSQL** with a clean ETL pipeline modelling real-world e-commerce analytics. Handles ingestion, transformation, and BI-ready output. Designed around the principle that bad data architecture costs more than bad code.

**What this proves:** I design systems end-to-end, not just endpoints.

![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![.NET 8](https://img.shields.io/badge/.NET_8-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)

</td>
<td width="50%" valign="top">

### 🔗 [SPO2SQL](https://github.com/kill74/SPO2SQL)
**Enterprise integration bridge — SharePoint Online → SQL Server.**

Console tool that syncs SharePoint lists to SQL Server via CSOM, applying data quality routines to catch structural inconsistencies before they corrupt downstream reports. The kind of unglamorous, critical infrastructure that keeps businesses running.

**What this proves:** I build tools that survive contact with production.

![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![SharePoint](https://img.shields.io/badge/SharePoint-0078D4?style=flat-square&logo=microsoftsharepoint&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)

</td>
</tr>
</table>

---

## `> cat skills.json | jq`

```json
{
  "languages": {
    "systems":   ["C", "Assembly (x86)", "Rust", "Go"],
    "backend":   ["C#", "Python", "PHP", "Node.js"],
    "frontend":  ["JavaScript", "TypeScript"],
    "scripting": ["Bash", "Lua"]
  },
  "frameworks": {
    "web":  ["React", "Next.js", ".NET 8"],
    "data": ["ETL pipelines", "PostgreSQL", "MySQL", "Oracle", "SQL Server"]
  },
  "systems_knowledge": [
    "x86 protected mode", "memory management",
    "CPU protection rings", "async runtimes",
    "network protocols", "CSOM / SharePoint APIs"
  ],
  "toolchain": ["Linux", "Git", "Vim", "GDB", "Bash", "npm", "OpenCV"],
  "currently_exploring": ["eBPF", "WASM runtimes", "distributed consensus"]
}
```

<br/>

<div align="center">

**Systems Layer**

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Assembly](https://img.shields.io/badge/ASM-x86-555555?style=for-the-badge)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)

**Application Layer**

![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)

**Interface Layer**

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Data Layer**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)

**Environment**

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Vim](https://img.shields.io/badge/Vim-019733?style=for-the-badge&logo=vim&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

</div>

---

## `> git log --oneline --all --graph`

<div align="center">

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=kill74&theme=tokyo-night&bg_color=0d1117&color=F7CF6E&line=F7CF6E&point=ffffff&area=true&hide_border=true)](https://github.com/ashutosh00710/github-readme-activity-graph)

<br/>

<img height="165em" src="https://github-readme-stats.vercel.app/api?username=kill74&show_icons=true&theme=tokyo-night&bg_color=0d1117&title_color=F7CF6E&icon_color=F7CF6E&text_color=ffffff&border_color=30363d&count_private=true&include_all_commits=true" />
<img height="165em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=kill74&layout=compact&theme=tokyo-night&bg_color=0d1117&title_color=F7CF6E&text_color=ffffff&border_color=30363d&langs_count=8" />

<br/>

[![GitHub Streak](https://streak-stats.demolab.com?user=kill74&theme=tokyo-night&background=0d1117&border=30363d&ring=F7CF6E&fire=F7CF6E&currStreakLabel=F7CF6E)](https://git.io/streak-stats)

</div>

---

## `> cat /proc/currently_running`

```
[ ACTIVE ]  Studying distributed systems & consensus algorithms
[ ACTIVE ]  Deepening OS internals — scheduler design, memory models
[ QUEUED ]  eBPF-based observability tooling (Rust)
[ QUEUED ]  Contributing to open-source systems projects
[ ALWAYS ]  Reading. Building. Iterating.
```

---

## `> ls ./contact`

<div align="center">

[![Portfolio](https://img.shields.io/badge/↗_Portfolio-0d1117?style=for-the-badge&logo=vercel&logoColor=F7CF6E)](https://guilhermewebsitee.vercel.app)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kill74)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-sales-35a580299)
&nbsp;
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guilhermesales4563@gmail.com)

<br/>

> Open to **internships**, **collaborative projects**, and **interesting problems.**
> If you're building something that requires understanding the full stack — let's talk.

</div>

---

<div align="center">

```sh
┌─[guilherme@kill74]─[~]
└──╼ $ sudo shutdown -h now

  Syncing filesystems...
  Saving state...
  [ always building → never stopping ]

Connection to kill74 closed.
```

<sub><code>// The present is connected to the past and future. — Lain</code></sub>

<br/>

![Profile views](https://komarev.com/ghpvc/?username=kill74&style=flat-square&color=F7CF6E&label=profile+views)

</div>
