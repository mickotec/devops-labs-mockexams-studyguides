# ☸ CKA & 🐧 LFCS Hands-on Practice Labs, Mock Exams & Study Suite

A comprehensive, calendar-aligned preparation suite for the **Certified Kubernetes Administrator (CKA)** and **Linux Foundation Certified System Administrator (LFCS)** certifications.

> [!IMPORTANT]
> **Kubernetes Cluster Infrastructure Acknowledgement:**
> The Kubernetes multi-node cluster formation and Vagrant provisioning in this repository are based on and adapted from [KodeKloud's Certified Kubernetes Administrator Course (kubeadm-clusters/virtualbox)](https://github.com/kodekloudhub/certified-kubernetes-administrator-course/tree/master/kubeadm-clusters/virtualbox). It has been augmented with a dedicated Ubuntu Linux machine (`LFCS`) to support comprehensive LFCS administration objectives.

Designed with **complete track modularity**: Whether you are studying exclusively for the **CKA**, exclusively for the **LFCS**, or tackling **both certifications in tandem**, each exam track provides a completely autonomous, standalone ecosystem — including its own web dashboard, exam simulator, lab generator, study guide builder, terminal progress tracker, and Pomodoro browser extension.

---

## 📑 Table of Contents

- [📁 Repository Architecture](#repository-architecture)
- [🎯 Choose Your Track](#choose-your-track)
  - [☸ Option A: Preparing ONLY for CKA](#option-a-cka)
  - [🐧 Option B: Preparing ONLY for LFCS](#option-b-lfcs)
  - [🚀 Option C: Dual Track (Both CKA & LFCS)](#option-c-both)
- [🖥 Lab Infrastructure (VirtualBox via Vagrant)](#lab-infrastructure)
  - [Virtual Machine Topology](#vm-topology)
  - [Provisioning the Machines](#provisioning-machines)
  - [Initializing Kubernetes Cluster (Calico CNI)](#initializing-k8s)
- [🛠 Unified Lab CLI (`./lab`)](#unified-lab-cli)
- [💻 Mock Exams & Exam Simulators](#mock-exams)
- [📅 Schedule Synchronization & Customization](#schedule-sync)
  - [Interactive Customization Prompts](#calendar-prompts)
  - [Calendar Outputs & Formats](#calendar-outputs)
- [📜 Credits & Attributions](#credits)
- [📄 License (MIT)](#license)

---

<a id="repository-architecture"></a>
## 📁 Repository Architecture

```text
devops-labs-mockexams-studyguides/
│
├── cka/                            # ☸ STANDALONE CKA TRACK
│   ├── vagrant/                    # Dedicated CKA 3-node K8s cluster Vagrantfile & provisioning
│   ├── lab                         # Dedicated CKA Lab CLI orchestrator (start, check, solve, reset, vm)
│   ├── webapp/                     # Dedicated CKA web dashboard & killer.sh exam simulator (Port 5051)
│   ├── pomodoro-extension/         # Dedicated CKA Pomodoro timer Chrome extension (links to 5051)
│   ├── generate_calendar.py        # Dedicated CKA study calendar generator (prompts start date & duration)
│   ├── generate_labs.py            # Dedicated CKA lab & mock exam generator script
│   ├── generate_guides.py          # Dedicated CKA daily study guide generator script
│   ├── study_todo.py               # Dedicated CKA terminal progress tracker & checklist
│   ├── schedule.template.csv       # Standard CKA curriculum schedule template
│   ├── guides/                     # 48 Track-specific CKA daily study guides & architectural theory
│   ├── kodekloud_cka/              # KodeKloud CKA course notes and references
│   ├── mock-cka-1/                 # Full-scale CKA timed mock exam 1 (17 killer.sh questions)
│   ├── mock-cka-2/                 # Full-scale CKA timed mock exam 2 (17 killer.sh questions)
│   └── w1d1-cka/ ... w8d6-cka/     # 48 Calendar-aligned hands-on Kubernetes lab scenarios
│
├── lfcs/                           # 🐧 STANDALONE LFCS TRACK
│   ├── vagrant/                    # Dedicated LFCS single-node VM Vagrantfile & provisioning
│   ├── lab                         # Dedicated LFCS Lab CLI orchestrator (start, check, solve, reset, vm)
│   ├── webapp/                     # Dedicated LFCS web dashboard & PSI exam simulator (Port 5052)
│   ├── pomodoro-extension/         # Dedicated LFCS Pomodoro timer Chrome extension (links to 5052)
│   ├── generate_calendar.py        # Dedicated LFCS study calendar generator (prompts start date & duration)
│   ├── generate_labs.py            # Dedicated LFCS lab & mock exam generator script
│   ├── generate_guides.py          # Dedicated LFCS daily study guide generator script
│   ├── study_todo.py               # Dedicated LFCS terminal progress tracker & checklist
│   ├── schedule.template.csv       # Standard LFCS curriculum schedule template
│   ├── guides/                     # 48 Track-specific LFCS daily study guides & system concepts
│   ├── mock-lfcs-1/ ... 4/         # 4 Full-scale LFCS timed mock exams (20 PSI questions each)
│   └── w1d1-lfcs/ ... w8d6-lfcs/   # 48 Calendar-aligned hands-on Linux lab scenarios
│
├── vagrant/                        # 🖥 Infrastructure & VM Provisioning (VirtualBox)
│   │                               # Based on KodeKloud kubeadm-clusters/virtualbox
│   ├── Vagrantfile                 # Multi-node K8s cluster (controlplane, node01, node02) + LFCS VM
│   ├── docs/                       # Compute, prerequisites & connectivity setup guides
│   └── ubuntu/                     # Provisioning scripts (kubeadm, containerd, hosts, ssh keys)
│
├── tools/                          # 🧰 Consolidated Utilities (Unified Multi-Track Mode)
│   ├── webapp/                     # Dual-track unified Flask web dashboard (Port 5050)
│   ├── pomodoro-extension/         # Unified Pomodoro extension
│   ├── curriculum/                 # Syllabus data definitions & question bank
│   ├── generate_calendar.py        # Interactive study calendar generator (start date, duration & track)
│   ├── generate_daily_guide.py     # Master parallel study guide generator
│   ├── study_todo.py               # Dual-track curses progress tracker
│   └── start_simulator.sh          # Terminal mock exam launcher
│
├── lab                             # 🚀 Master CLI Launcher & Forwarder (dispatches to cka/lab or lfcs/lab)
├── LICENSE                         # MIT Open Source License
├── .gitignore                      # Ignores personal/generated schedules (*.ics, *.csv, *.json)
└── README.md
```

---

<a id="choose-your-track"></a>
## 🎯 Choose Your Track

<a id="option-a-cka"></a>
### Option A: Preparing ONLY for CKA (Certified Kubernetes Administrator)

You can work entirely inside the `cka/` folder without touching LFCS:

```bash
cd cka

# 1. Provision ONLY the 3-node Kubernetes cluster (controlplane, node01, node02)
./lab vm up                 # Or: cd vagrant && vagrant up

# 2. Dedicated CKA Lab CLI (manage, grade, and solve Kubernetes scenarios)
./lab list                  # List all 48 CKA daily labs and 2 killer.sh mock exams
./lab start w1d1-cka        # Inject scenario into K8s cluster (controlplane, node01, node02)
./lab show w1d1-cka         # View scenario objectives & tasks
./lab check w1d1-cka        # Automatically grade your work
./lab solve w1d1-cka        # Reveal step-by-step solutions
./lab reset w1d1-cka        # Reset scenario to clean state
./lab vm status             # Check cluster VM status
./lab ssh controlplane      # Jump directly into the master node

# 3. Run the terminal progress tracker & daily checklist
python3 study_todo.py

# 4. Customize your study calendar (asks when you start & for how long)
python3 generate_calendar.py

# 5. Launch the dedicated CKA Web Dashboard & Killer.sh Exam Simulator (http://localhost:5051)
bash webapp/start.sh

# 6. Generate or update all 48 CKA daily HTML study guides
python3 generate_guides.py

# 7. Generate or rebuild all 48 CKA labs and killer.sh mock exams
python3 generate_labs.py

# 8. Import cka/schedule.ics into Google Calendar or Thunderbird
```

**Pomodoro Extension for CKA:**
1. Open Google Chrome or Brave and go to `chrome://extensions/`.
2. Turn on **Developer mode** (top right).
3. Click **Load unpacked** and select `cka/pomodoro-extension/`.
4. The extension is pre-configured with CKA focus sessions and direct shortcuts to the CKA webapp at `http://localhost:5051`.

---

<a id="option-b-lfcs"></a>
### Option B: Preparing ONLY for LFCS (Linux Foundation Certified SysAdmin)

You can work entirely inside the `lfcs/` folder without touching CKA:

```bash
cd lfcs

# 1. Provision ONLY the standalone LFCS practice VM
./lab vm up                 # Or: cd vagrant && vagrant up

# 2. Dedicated LFCS Lab CLI (manage, grade, and solve Linux scenarios)
./lab list                  # List all 48 LFCS daily labs and 4 PSI mock exams
./lab start w1d1-lfcs       # Inject scenario into LFCS target VM
./lab show w1d1-lfcs        # View scenario objectives & tasks
./lab check w1d1-lfcs       # Automatically grade your work
./lab solve w1d1-lfcs       # Reveal step-by-step solutions
./lab reset w1d1-lfcs       # Reset scenario to clean state
./lab vm status             # Check LFCS VM status
./lab ssh                   # Jump directly into LFCS VM

# 3. Run the terminal progress tracker & daily checklist
python3 study_todo.py

# 4. Customize your study calendar (asks when you start & for how long)
python3 generate_calendar.py

# 5. Launch the dedicated LFCS Web Dashboard & PSI Exam Simulator (http://localhost:5052)
bash webapp/start.sh

# 6. Generate or update all 48 LFCS daily HTML study guides
python3 generate_guides.py

# 7. Generate or rebuild all 48 LFCS labs and 4 PSI mock exams
python3 generate_labs.py

# 8. Import lfcs/schedule.ics into Google Calendar or Thunderbird
```

**Pomodoro Extension for LFCS:**
1. Open Google Chrome or Brave and go to `chrome://extensions/`.
2. Turn on **Developer mode** (top right).
3. Click **Load unpacked** and select `lfcs/pomodoro-extension/`.
4. The extension is pre-configured with LFCS focus sessions and direct shortcuts to the LFCS webapp at `http://localhost:5052`.

---

<a id="option-c-both"></a>
### Option C: Preparing for BOTH CKA & LFCS Concurrently

Use the root orchestrator `./lab` and unified tooling:

```bash
# List all 100 scenarios across both tracks
./lab list

# Filter scenarios by track
./lab list cka
./lab list lfcs

# Launch the unified webapp dashboard on port 5050
bash tools/start_webapp.sh
```

---

<a id="lab-infrastructure"></a>
## 🖥 Lab Infrastructure (VirtualBox via Vagrant)

The lab environment runs locally on Oracle VirtualBox using automated Vagrant provisioning, adapted from [KodeKloud's Certified Kubernetes Administrator Course](https://github.com/kodekloudhub/certified-kubernetes-administrator-course/tree/master/kubeadm-clusters/virtualbox).

<a id="vm-topology"></a>
### Virtual Machine Topology

| VM Name | Hostname | Role | OS | CPUs | RAM | Default NAT IP | Forwarded SSH Port |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `controlplane` | `controlplane` | K8s Control Plane Master | Ubuntu 22.04 | 2 | 2048 MB | `192.168.56.11` | `2710 -> 22` |
| `node01` | `node01` | K8s Worker Node 1 | Ubuntu 22.04 | 1 | 1024 MB | `192.168.56.21` | `2721 -> 22` |
| `node02` | `node02` | K8s Worker Node 2 | Ubuntu 22.04 | 1 | 1024 MB | `192.168.56.22` | `2722 -> 22` |
| `LFCS` | `LFCS` | Linux SysAdmin Target | Ubuntu 22.04 | 2 | 2048 MB | `192.168.56.30` | `2730 -> 22` |

<a id="provisioning-machines"></a>
### Provisioning the Machines

You can spin up only the exact machines required for your study track to save CPU and RAM resources:

#### 1. CKA Only (3 Nodes: `controlplane`, `node01`, `node02` — 4 vCPUs, 4 GB RAM)
```bash
# Using dedicated CKA runner:
cd cka && ./lab vm up

# Or directly via Vagrant:
cd cka/vagrant && vagrant up
```

#### 2. LFCS Only (1 Node: `LFCS` — 2 vCPUs, 2 GB RAM)
```bash
# Using dedicated LFCS runner:
cd lfcs && ./lab vm up

# Or directly via Vagrant:
cd lfcs/vagrant && vagrant up
```

#### 3. Dual Track / All-in-One (All 4 Nodes — 7 vCPUs, 6 GB RAM)
```bash
# Using root lab runner:
./lab vm up

# Or directly via root Vagrant:
cd vagrant && vagrant up
```

<a id="initializing-k8s"></a>
### Initializing the Kubernetes Cluster
1. SSH into the control plane:
   ```bash
   vagrant ssh controlplane
   ```
2. Initialize the cluster with kubeadm:
   ```bash
   sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=$(cat /usr/local/bin/public-ip)
   ```
3. Set up regular user `kubectl` credentials:
   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```
4. Install CNI (Project Calico):
   ```bash
   # Project Calico provides full NetworkPolicy enforcement required for CKA exam objectives
   kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.2/manifests/calico.yaml
   ```
5. Join `node01` and `node02` using the `kubeadm join` command produced by step 2.

---

<a id="unified-lab-cli"></a>
## 🛠 Lab CLI Orchestrators (`./lab`)

Each certification track includes its own **standalone, decoupled CLI runner** (`cka/lab` and `lfcs/lab`), while the repository root provides an intelligent launcher that forwards commands to the appropriate track:

### Standalone Track Usage (Recommended for Single-Track Study):
- **CKA Track**: `cd cka && ./lab list` (manages only K8s scenarios and `controlplane`/`node01`/`node02` nodes)
- **LFCS Track**: `cd lfcs && ./lab list` (manages only Linux scenarios and the `LFCS` VM)

### Dual-Track & Root Launcher:
When working from the repository root, `./lab` automatically routes your commands:

```bash
# List all scenarios across both tracks
./lab list

# Filter scenarios by exam track
./lab list cka
./lab list lfcs
./lab list w2

# Start a scenario (injects broken state / practice files into the target VM)
./lab start w1d1-cka
./lab start w1d1-lfcs

# View the problem statement and objectives
./lab show w1d1-cka

# Verify and grade your solution automatically
./lab check w1d1-cka

# View official step-by-step walkthrough and solution
./lab solve w1d1-cka

# Reset scenario back to a clean state
./lab reset w1d1-cka

# Check VirtualBox VM status & power state
./lab vm status
./lab vm start

# Direct SSH connection to any node
./lab ssh controlplane
./lab ssh node01
./lab ssh node02
./lab ssh lfcs
```

---

<a id="mock-exams"></a>
## 💻 Mock Exams & Exam Simulators

Realistic, timed exam environments simulating the exact interface and constraints of the real certifications:

- **CKA Mock Exams** (`cka/mock-cka-1`, `cka/mock-cka-2`):
  - Emulates the **killer.sh** remote desktop interface.
  - 17 realistic questions per exam matching official CKA domain weights.
  - 120-minute timer with automatic scoring and detailed explanations.
- **LFCS Mock Exams** (`lfcs/mock-lfcs-1` through `lfcs/mock-lfcs-4`):
  - Emulates the **PSI Secure Browser** remote desktop experience.
  - 20 realistic questions per exam covering system maintenance, storage, networking, service management, and troubleshooting.
  - 120-minute timed environment with automated graders.

---

<a id="schedule-sync"></a>
## 📅 Schedule Synchronization & Customization

The study suite includes an **interactive calendar generator** that asks you when you want to start studying and for how long, allowing you to tailor the pacing to your availability:

```bash
# Run the interactive calendar wizard from repository root:
./lab calendar

# Or run track-specific calendar generators:
cd cka && python3 generate_calendar.py   # Tailored for CKA (4 hrs/day)
cd lfcs && python3 generate_calendar.py  # Tailored for LFCS (3 hrs/day)
```

<a id="calendar-prompts"></a>
### Interactive Customization Prompts:
1. **When do you start?**: Enter any date (`YYYY-MM-DD`), `'today'`, `'tomorrow'`, or press Enter to default to the upcoming Monday.
2. **For how long?**:
   - `8 Weeks`: Standard comprehensive pacing (6 study days/week, ~48 days) [Recommended]
   - `4 Weeks`: Accelerated intensive sprint (condensed double-pace, ~24 days)
   - Custom: Any number of weeks between 1 and 16.
3. **Certification Track**: Choose between `Both (Dual Track)`, `CKA Only`, or `LFCS Only`.
4. **Planned Pauses**: Optionally insert scheduled recovery/pause weeks (e.g. for travel, family, or work commitments) which automatically shifts all remaining modules without disrupting the syllabus flow.
5. **Custom Daily Study Hours**: Specify your exact preferred study hours for each track (e.g. `4am to 12 pm` for early-bird/morning CKA, `6pm to 8pm` for evening LFCS, `18:00 - 21:00`, or press Enter to keep standard defaults `08:00 AM - 12:00 PM` and `03:00 PM - 06:00 PM`).

<a id="calendar-outputs"></a>
### Private Local Calendar Outputs:
When you run the generator, your customized calendar files are generated locally for your private use (and excluded from Git tracking via `.gitignore` so your personal dates and custom hours are never committed):
- **CKA Calendar**: `cka/schedule.ics` & `cka/schedule.csv` (tailored to your chosen hours, e.g. 04:00 AM - 12:00 PM)
- **LFCS Calendar**: `lfcs/schedule.ics` & `lfcs/schedule.csv` (tailored to your chosen hours, e.g. 06:00 PM - 08:00 PM)
- **Dual-Track Calendar**: `cka_lfcs_schedule.ics` & `cka_lfcs_schedule.csv` (when scheduling both)

Importable directly into Google Calendar, Apple Calendar, Microsoft Outlook, Thunderbird, and mobile calendar apps.

---

<a id="credits"></a>
## 📜 Credits & Attributions

- Kubernetes cluster topology and provisioning scripts adapted from [KodeKloud - Certified Kubernetes Administrator Course](https://github.com/kodekloudhub/certified-kubernetes-administrator-course).
- Mock exam question formats and grading inspired by [killer.sh](https://killer.sh) and Linux Foundation exam guidelines.

---

<a id="license"></a>
## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).
