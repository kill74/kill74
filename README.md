<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=F7CF6E&height=120&section=header" width="100%"/>

```
██╗  ██╗██╗██╗     ██╗     ███████╗██╗  ██╗
██║ ██╔╝██║██║     ██║     ╚════██║██║  ██║
█████╔╝ ██║██║     ██║         ██╔╝███████║
██╔═██╗ ██║██║     ██║        ██╔╝ ╚════██║
██║  ██╗██║███████╗███████╗   ██║       ██║
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝   ╚═╝       ╚═╝
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=15&duration=2800&pause=1200&color=F7CF6E&center=true&vCenter=true&width=700&lines=Full-Stack+Engineer+%7C+Systems+Programmer;Writes+kernels+in+C+%26+ASM+%E2%80%94+ships+products+in+Rust+%26+React;One+of+the+few+who+understands+both+ends+of+the+stack;Castelo+Branco%2C+Portugal+%F0%9F%87%B5%F0%9F%87%B9+%E2%80%94+building+globally;The+present+is+connected+to+the+past+and+future+%E2%80%94+Lain" alt="Typing SVG" />

<br/>

**Rust backend/systems developer open to contract work.**
Async Rust, WebSocket systems, SQLite persistence, CI/release automation, and security-minded protocol work.

[![Portfolio](https://img.shields.io/badge/↗_Portfolio-0d1117?style=for-the-badge&logo=vercel&logoColor=F7CF6E)](https://guilhermewebsitee.vercel.app)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kill74)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-sales-35a580299)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guilhermesales4563@gmail.com)

![Profile views](https://komarev.com/ghpvc/?username=kill74&style=flat-square&color=F7CF6E&label=profile+views)

</div>

<br/>

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

  layers      →  bare-metal kernels  →  systems daemons  →  REST APIs  →  UIs
  philosophy  →  understand the whole stack, own every layer

  status      →  [ BUILDING ] — always.
```

> Most developers live at one end of the stack.
> I write kernels *and* ship products — because you can't truly master one without understanding the other.

<br/>

---

## `> cat principles.txt`

```sh
┌─[guilherme@kill74]─[~]
└──╼ $ cat ~/principles.txt

  → Understand the layer below the one you're working in
  → If you can't explain the failure mode, you don't own the code
  → Observability is not optional in production
  → Bad data models outlive bad code by years
  → A system that can't be debugged can't be trusted
  → Ship it. Then make it right. Then make it fast.
```

<br/>

---

## `> ls -la ./projects --sort=impact`

> Production systems, open-source tooling, and systems experiments. All shipped.

<br/>

<table>
<tr>
<td width="50%" valign="top">

<h3>🔁 <a href="https://github.com/kill74/TeamPulseBridge">TeamPulseBridge</a></h3>

**Production-grade event ingestion bridge**
`Slack · Teams · GitHub · GitLab → one hardened pipeline`

Built in **Go** with HMAC/token webhook verification across 4 providers. Ships with OpenTelemetry tracing, structured `slog` logging, Prometheus metrics, JWT-protected admin routes, and full Terraform IaC on GCP (GKE, Cloud SQL, VPC, Cloud Armor). Six CI workflows: lint, race detector, vuln scan, smoke tests, automated releases.

`→` Security, observability, and reliability — from commit one.

<br/>

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat-square&logo=opentelemetry&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

</td>
<td width="50%" valign="top">

<h3>💬 <a href="https://github.com/kill74/Chatify">Chatify</a></h3>

**Terminal-first, self-hosted chat server**
`WebSocket · SQLite · Rust · Cross-platform`

Concurrent WebSocket server with SQLite-backed event persistence, multi-channel messaging, DMs, voice, file transfers, reactions, and time-window history search. Optional Discord bridge behind a Cargo feature flag. Cross-platform binaries with automated Windows packaging and SHA256 checksums.

`→` Systems thinking applied to networked, concurrent software.

<br/>

![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-grey?style=flat-square)
![CI](https://img.shields.io/badge/CI-passing-F7CF6E?style=flat-square&labelColor=0d1117)

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h3>📊 <a href="https://github.com/kill74/PulseData">PulseData</a></h3>

**Full-stack data engineering platform**
`.NET 8 · PostgreSQL · ETL · BI-ready`

Clean ETL pipeline modelling real-world e-commerce analytics — ingestion, transformation, and BI-ready output. Designed around the principle that bad data architecture costs more than bad code.

`→` End-to-end system design, not just endpoints.

<br/>

![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![.NET 8](https://img.shields.io/badge/.NET_8-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)

</td>
<td width="50%" valign="top">

<h3>🔌 <a href="https://github.com/kill74/SPO2SQL">SPO2SQL</a></h3>

**Enterprise integration bridge**
`SharePoint Online → SQL Server · CSOM · Data Quality`

Syncs SharePoint lists to SQL Server via CSOM, applying data quality routines to catch structural inconsistencies before they reach downstream reports. The kind of unglamorous, critical infrastructure that keeps businesses running.

`→` Tools that survive contact with production.

<br/>

![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![SharePoint](https://img.shields.io/badge/SharePoint-0078D4?style=flat-square&logo=microsoftsharepoint&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)

</td>
</tr>
</table>

---

## `> cat war_stories.log`

> Real problems, real fixes. The bugs that taught me the most.

<br/>

```sh
┌─[guilherme@kill74]─[~]
└──╼ $ tail -n 50 ~/war_stories.log
```

**[Chatify] — Race condition at scale**
```
Under 200+ concurrent WebSocket connections, Chatify started dropping messages
silently. No panic, no error — just ghost broadcasts.

Traced it to a lock ordering inconsistency in the channel broadcast logic:
two async tasks acquiring per-channel and global state locks in opposite order,
creating a classic deadlock window under load.

Fix: enforced a strict RwLock acquisition hierarchy — global state always before
channel state, never the inverse. Added a stress-test harness that spawns 500
concurrent clients and asserts zero dropped messages. That test now lives in CI
and blocks every merge.

Lesson: async Rust prevents data races. It doesn't prevent logical races.
You still have to think.
```

**[TeamPulseBridge] — Webhook replay attacks**
```
During a security review I noticed the HMAC verification was correct, but there
was no timestamp validation on incoming webhook payloads. A captured request
could be replayed indefinitely and pass signature checks.

Fix: added a 5-minute receive window check against the provider timestamp header.
Requests outside the window are rejected with 401 before they touch any handler.
Added to the threat model doc and integration test suite.

Lesson: cryptographic correctness ≠ protocol security. Model the attacker, not
just the algorithm.
```

<br/>

---

## `> htop --mode=languages`

<div align="center">

[![Wakatime Stats](https://github-readme-stats.vercel.app/api/wakatime?username=kill74&theme=tokyonight&bg_color=0d1117&title_color=F7CF6E&text_color=ffffff&icon_color=F7CF6E&border_color=F7CF6E&layout=compact&langs_count=8)](https://wakatime.com/@kill74)

> ⚠️ To activate live WakaTime stats: create a free account at [wakatime.com](https://wakatime.com), install the IDE plugin, and update `?username=kill74` above with your WakaTime username.

</div>

<br/>

---

## `> dig chatify.arch +short`

```
                        ┌─────────────────────────────────┐
                        │         Chatify Architecture     │
                        └─────────────────────────────────┘

  Clients (WS)                   Server Core                  Persistence
  ┌──────────┐                 ┌────────────────┐            ┌──────────────┐
  │ Client A │──────────────▶  │  WS Listener   │            │              │
  └──────────┘    upgrade      │  (tokio-tungstenite)        │   SQLite DB  │
                               └───────┬────────┘            │              │
  ┌──────────┐                         │                     │  ┌─────────┐ │
  │ Client B │──────────────▶          ▼                     │  │ messages│ │
  └──────────┘              ┌──────────────────┐    write    │  │ channels│ │
                            │  Session Manager  │ ─────────▶ │  │ users   │ │
  ┌──────────┐              │  (Arc<RwLock<T>>) │            │  │ files   │ │
  │ Client C │──────────────▶          │        │            └──────────────┘
  └──────────┘              └──────────┬───────┘
                                       │
                         ┌─────────────┴──────────────┐
                         │                            │
                  ┌──────▼──────┐            ┌────────▼──────┐
                  │  Channel    │            │  DM / Voice   │
                  │  Broadcast  │            │  Handler      │
                  └──────┬──────┘            └───────────────┘
                         │
              ┌──────────▼──────────┐
              │  Discord Bridge     │  ← optional (Cargo feature flag)
              │  (feature = bridge) │
              └─────────────────────┘

  Lock hierarchy enforced:  GlobalState → ChannelState  (never reversed)
  Message delivery:         broadcast fan-out per channel subscriber list
  Persistence:              every event written to SQLite before ACK
```

<br/>

---

## `> git log --oneline --all --graph`

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=kill74&theme=tokyonight&background=0d1117&border=F7CF6E&stroke=F7CF6E&ring=F7CF6E&fire=FF6B6B&currStreakNum=ffffff&sideNums=F7CF6E&currStreakLabel=F7CF6E&sideLabels=F7CF6E&dates=888888" />

<br/><br/>

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=kill74&theme=tokyo-night&bg_color=0d1117&color=F7CF6E&line=F7CF6E&point=ffffff&area=true&hide_border=true)](https://github.com/ashutosh00710/github-readme-activity-graph)

<br/>

<!-- Contribution Snake — set up the GitHub Action below to activate -->
<!-- ACTION SETUP: Create .github/workflows/snake.yml in your profile repo:

name: Generate Snake
on:
  schedule: [{ cron: "0 0 * * *" }]
  workflow_dispatch:
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: kill74
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

Then uncomment the img tag below: -->

<!-- <img src="https://raw.githubusercontent.com/kill74/kill74/output/github-contribution-grid-snake-dark.svg" alt="contribution snake" /> -->

</div>

---

## `> cat /proc/currently_running`

```
[ ACTIVE ]  Distributed systems & consensus algorithms — Raft, Paxos
[ ACTIVE ]  OS internals — scheduler design, memory models, lock-free structures
[ QUEUED ]  eBPF-based observability tooling in Rust
[ QUEUED ]  Contributing to open-source systems projects
[ ALWAYS ]  Reading. Building. Shipping. Iterating.
```

---

<div align="center">

> Available for **Rust backend/systems contract work**.
> See [Chatify](https://github.com/kill74/Chatify) for shipped proof: async WebSockets, SQLite persistence, protocol contracts, CI, releases, and security notes.

<br/>

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

<img src="https://capsule-render.vercel.app/api?type=waving&color=F7CF6E&height=100&section=footer" width="100%"/>

</div>
