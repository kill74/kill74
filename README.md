<div align="center">

```
██╗  ██╗██╗██╗     ██╗     ███████╗██╗  ██╗
██║ ██╔╝██║██║     ██║     ╚════██║██║  ██║
█████╔╝ ██║██║     ██║         ██╔╝███████║
██╔═██╗ ██║██║     ██║        ██╔╝ ╚════██║
██║  ██╗██║███████╗███████╗   ██║       ██║
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝   ╚═╝       ╚═╝
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=15&pause=1000&color=F7CF6E&center=true&vCenter=true&width=680&lines=Full-Stack+Engineer+%7C+Systems+Programmer;Writes+kernels+in+C+%26+ASM+%E2%80%94+ships+products+in+Rust+%26+React;One+of+the+few+who+understands+both+ends+of+the+stack;Castelo+Branco%2C+Portugal+%F0%9F%87%B5%F0%9F%87%B9+%E2%80%94+building+globally;The+present+is+connected+to+the+past+and+future+%E2%80%94+Lain" alt="Typing SVG" />

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

  education   →  B.Sc. Digital & Multimedia Design
                 Instituto Politécnico de Castelo Branco
  prior       →  TeSP — Web & Multimedia Development    [grade: 15 ✓]

  stack       →  C · Assembly · Rust · Go · C# · JS/TS · Python · PHP · Lua
  data        →  SQLite · PostgreSQL · Oracle · MongoDB · SQL Server
  layers      →  bare-metal kernels  →  systems daemons  →  REST APIs  →  UIs
  philosophy  →  understand the whole stack, own every layer

  status      →  [ BUILDING ] — always.
```

> Most developers live at one end of the stack.
> I write kernels *and* ship products — because you can't truly master one without the other.

---

## `> ls -la ./projects --sort=impact`

> Production systems, open-source tooling, and systems experiments. All shipped.

<br/>

<table>
<tr>
<td width="50%" valign="top">

### 🔁 [TeamPulseBridge](https://github.com/kill74/TeamPulseBridge)
**Production-grade event ingestion bridge — Slack, Teams, GitHub, GitLab → one hardened pipeline.**

Built in **Go** with HMAC/token webhook verification across 4 providers. Ships with OpenTelemetry tracing, structured `slog` logging, Prometheus metrics, JWT-protected admin routes, and full Terraform IaC for GCP (GKE, Cloud SQL, VPC, Cloud Armor). Six CI workflows: lint, race detector, vuln scan, smoke tests, and automated releases.

`→` Designed for production from commit one — security, observability, and reliability are not afterthoughts.

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

</td>
<td width="50%" valign="top">

### 💬 [Chatify](https://github.com/kill74/Chatify)
**Terminal-first, self-hosted chat server — engineered for correctness in Rust.**

WebSocket server with SQLite-backed event persistence, multi-channel messaging, DMs, voice, file transfers, reactions, and time-window history search. Optional Discord bridge behind a Cargo feature flag. Ships as cross-platform binaries with automated Windows release packaging and SHA256 checksums via GitHub Actions CI.

`→` Systems thinking applied to networked, concurrent, production-ready software.

![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-grey?style=flat-square)
![CI](https://img.shields.io/badge/CI-passing-F7CF6E?style=flat-square&labelColor=0d1117)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 [PulseData](https://github.com/kill74/PulseData)
**Full-stack data engineering platform — from raw events to business insight.**

Built on **.NET 8 + PostgreSQL** with a clean ETL pipeline modelling real-world e-commerce analytics. Handles ingestion, transformation, and BI-ready output. Designed around the principle that bad data architecture costs more than bad code.

`→` End-to-end system design — not just endpoints.

![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![.NET 8](https://img.shields.io/badge/.NET_8-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)

</td>
<td width="50%" valign="top">

### 🔌 [SPO2SQL](https://github.com/kill74/SPO2SQL)
**Enterprise integration bridge — SharePoint Online → SQL Server.**

Console tool that syncs SharePoint lists to SQL Server via CSOM, applying data quality routines to catch structural inconsistencies before they corrupt downstream reports. The kind of unglamorous, critical infrastructure that keeps businesses running.

`→` Tools that survive contact with production.

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
    "x86 protected mode",
    "memory management & allocators",
    "CPU protection rings",
    "async runtimes",
    "network protocols (TCP/IP, WebSocket, HTTP/2)",
    "CSOM / SharePoint APIs"
  ],
  "toolchain": [
    "Linux", "Git", "Vim", "GDB", "Bash",
    "Docker", "Terraform", "OpenCV", "npm"
  ],
  "currently_exploring": [
    "eBPF", "WASM runtimes",
    "distributed consensus (Raft/Paxos)",
    "GitOps (ArgoCD / Flux)"
  ]
}
```

---

## `> git log --oneline --all --graph`

<div align="center">

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=kill74&theme=tokyo-night&bg_color=0d1117&color=F7CF6E&line=F7CF6E&point=ffffff&area=true&hide_border=true)](https://github.com/ashutosh00710/github-readme-activity-graph)

<br/>

</div>

---

## `> cat /proc/currently_running`

```
[ ACTIVE ]  Studying distributed systems & consensus algorithms (Raft, Paxos)
[ ACTIVE ]  OS internals — scheduler design, memory models, lock-free structures
[ QUEUED ]  eBPF-based observability tooling in Rust
[ QUEUED ]  Contributing to open-source systems projects
[ ALWAYS ]  Reading. Building. Shipping. Iterating.
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
> If you're building something that demands understanding the full stack — let's talk.

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
