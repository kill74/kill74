<div align="center">

```
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░  SIGNAL INTERCEPT — WIRED NODE: kill74                  ░
 ░  DECODING...  ████████████████░░░░  78%                 ░
 ░  origin    →  Castelo Branco, PT · 39.8°N 7.5°W        ░
 ░  timestamp →  always                                    ░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

</div>

---

I write code at both ends of the machine.

Not because it's impressive — because you can't reason about a system you only know from one side. I've written bootloaders and I've shipped web apps. The distance between them is smaller than people think, and understanding both changes how you design everything.

```
  name      →  Guilherme
  handle    →  kill74
  age       →  20
  location  →  Castelo Branco, Portugal
  degree    →  Digital & Multimedia Design — IPCB
            →  prev. TeSP Web & Multimedia Dev  [15/20]
```

---

## the work

These are not demos. They are systems designed to survive.

---

**[TeamPulseBridge](https://github.com/kill74/TeamPulseBridge)** `Go · Terraform · OpenTelemetry`

Webhook ingestion bridge for Slack, Teams, GitHub, GitLab — one hardened pipeline.
HMAC/token verification per provider. JWT-protected admin routes. Prometheus metrics, structured logging, distributed tracing from day one. Full Terraform IaC on GCP: GKE, Cloud SQL, VPC, Cloud Armor. Six CI workflows: lint, race detector, vuln scan, smoke tests, automated releases.

*Security, observability, and reliability are load-bearing walls — not furniture.*

---

**[Chatify](https://github.com/kill74/Chatify)** `Rust · SQLite · WebSocket`

Terminal-first, self-hosted chat — engineered for correctness, not convenience.
Multi-channel, DMs, voice, file transfer, reactions, history replay, time-window search. SQLite-backed event persistence. Optional Discord bridge as a Cargo feature flag. Cross-platform binaries with SHA256 checksums via CI.

*What async Rust forces you to think about, you carry into everything else you build.*

---

**[PulseData](https://github.com/kill74/PulseData)** `.NET 8 · PostgreSQL`

Full-stack data engineering platform. Raw events → clean ETL → BI-ready output.
Modelled on real-world e-commerce analytics. Bad data architecture costs more than bad code — this is designed around that truth.

---

**[SPO2SQL](https://github.com/kill74/SPO2SQL)** `C# · SharePoint CSOM · SQL Server`

SharePoint Online → SQL Server sync bridge. Applies data quality routines before anything reaches downstream reports. Unglamorous, critical infrastructure. The kind of tool that runs quietly and saves someone's Monday.

---

## the stack

```
systems    →  C  ·  x86 Assembly  ·  Rust  ·  Go
backend    →  C#  ·  Python  ·  PHP  ·  Node.js
frontend   →  TypeScript  ·  JavaScript  ·  React  ·  Next.js
data       →  PostgreSQL  ·  MySQL  ·  Oracle  ·  SQL Server  ·  SQLite  ·  MongoDB
scripting  →  Bash  ·  Lua
toolchain  →  Linux  ·  Git  ·  Vim  ·  GDB  ·  Docker  ·  Terraform  ·  OpenCV
```

```
know cold  →  x86 protected mode  ·  memory models  ·  CPU rings
           →  async runtimes  ·  network protocols  ·  webhook security
learning   →  eBPF  ·  WASM runtimes  ·  distributed consensus  ·  GitOps
```

---

## currently

```sh
[ ● ] distributed systems — consensus algorithms, CAP theorem in practice
[ ● ] OS internals — scheduler design, memory management deep dives
[ ○ ] eBPF observability tooling in Rust
[ ○ ] open-source systems contributions
[ ∞ ] reading · building · iterating
```

---

## reach me

<div align="center">

[![Portfolio](https://img.shields.io/badge/portfolio-guilhermewebsitee.vercel.app-F7CF6E?style=flat-square&labelColor=0d1117)](https://guilhermewebsitee.vercel.app)
&nbsp;
[![GitHub](https://img.shields.io/badge/github-kill74-white?style=flat-square&logo=github&labelColor=0d1117)](https://github.com/kill74)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/linkedin-guilherme--sales-0077B5?style=flat-square&logo=linkedin&labelColor=0d1117)](https://www.linkedin.com/in/guilherme-sales-35a580299)
&nbsp;
[![Email](https://img.shields.io/badge/email-guilhermesales4563@gmail.com-D14836?style=flat-square&logo=gmail&labelColor=0d1117)](mailto:guilhermesales4563@gmail.com)

</div>

Open to internships, collaboration, and problems worth solving.
If your system needs someone who can read the assembly *and* ship the product — let's talk.

---

<div align="center">

```
no matter where you go, everyone is connected.
```

`// — Lain`

![views](https://komarev.com/ghpvc/?username=kill74&style=flat-square&color=F7CF6E&label=nodes+reached)

</div>
