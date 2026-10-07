# ☸ CKA & 🐧 LFCS Hands-on Practice Labs, Mock Exams & Study Suite

A comprehensive, calendar-aligned preparation suite for the **Certified Kubernetes Administrator (CKA)** and **Linux Foundation Certified System Administrator (LFCS)** certifications.

> [!IMPORTANT]
> **Kubernetes Cluster Infrastructure Acknowledgement:**
> The Kubernetes multi-node cluster formation and Vagrant provisioning in this repository are based on and adapted from [KodeKloud's Certified Kubernetes Administrator Course (kubeadm-clusters/virtualbox)](https://github.com/kodekloudhub/certified-kubernetes-administrator-course/tree/master/kubeadm-clusters/virtualbox). It has been augmented with a dedicated Ubuntu Linux machine (`LFCS`) to support comprehensive LFCS administration objectives.

Designed with **complete track modularity**: Whether you are studying exclusively for the **CKA**, exclusively for the **LFCS**, or tackling **both certifications in tandem**, each exam track provides a completely autonomous, standalone ecosystem — including its own web dashboard, exam simulator, lab generator, study guide builder, terminal progress tracker, and Pomodoro browser extension.

---

## 📁 Repository Architecture

```text
devops-labs-mockexams-studyguides/
│
├── cka/                            # ☸ STANDALONE CKA TRACK
│   ├── webapp/                     # Dedicated CKA web dashboard & killer.sh exam simulator (Port 5051)
│   ├── pomodoro-extension/         # Dedicated CKA Pomodoro timer Chrome extension (links to 5051)
│   ├── generate_labs.py            # Dedicated CKA lab & mock exam generator script
│   ├── generate_guides.py          # Dedicated CKA daily study guide generator script
│   ├── study_todo.py               # Dedicated CKA terminal progress tracker & checklist
│   ├── schedule.csv / .ics         # Dedicated CKA 8-week daily study schedule & calendar
│   ├── guides/                     # 48 Track-specific CKA daily study guides & architectural theory
│   ├── kodekloud_cka/              # KodeKloud CKA course notes and references
│   ├── mock-cka-1/                 # Full-scale CKA timed mock exam 1 (17 killer.sh questions)
│   ├── mock-cka-2/                 # Full-scale CKA timed mock exam 2 (17 killer.sh questions)
│   └── w1d1-cka/ ... w8d6-cka/     # 48 Calendar-aligned hands-on Kubernetes lab scenarios
│
├── lfcs/                           # 🐧 STANDALONE LFCS TRACK
│   ├── webapp/                     # Dedicated LFCS web dashboard & PSI exam simulator (Port 5052)
│   ├── pomodoro-extension/         # Dedicated LFCS Pomodoro timer Chrome extension (links to 5052)
│   ├── generate_labs.py            # Dedicated LFCS lab & mock exam generator script
│   ├── generate_guides.py          # Dedicated LFCS daily study guide generator script
│   ├── study_todo.py               # Dedicated LFCS terminal progress tracker & checklist
│   ├── schedule.csv / .ics         # Dedicated LFCS 8-week daily study schedule & calendar
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
│   ├── generate_daily_guide.py     # Master parallel study guide generator
│   ├── study_todo.py               # Dual-track curses progress tracker
│   └── start_simulator.sh          # Terminal mock exam launcher
│
├── lab                             # 🚀 Master CLI Orchestrator (start, check, solve, reset, vm)
├── cka_lfcs_schedule.csv           # Master dual-track schedule
├── cka_lfcs_schedule.ics           # Master dual-track iCalendar file
├── .gitignore
└── README.md
```

---

## 🎯 Choose Your Track

### Option A: Preparing ONLY for CKA (Certified Kubernetes Administrator)

You can work entirely inside the `cka/` folder without touching LFCS:

```bash
cd cka

# 1. Run the terminal progress tracker & daily checklist
python3 study_todo.py

# 2. Launch the dedicated CKA Web Dashboard & Killer.sh Exam Simulator (http://localhost:5051)
bash webapp/start.sh

# 3. Generate or update all 48 CKA daily HTML study guides
python3 generate_guides.py

# 4. Generate or rebuild all 48 CKA labs and killer.sh mock exams
python3 generate_labs.py

# 5. Import cka/schedule.ics into Google Calendar or Thunderbird
```

**Pomodoro Extension for CKA:**
1. Open Google Chrome or Brave and go to `chrome://extensions/`.
2. Turn on **Developer mode** (top right).
3. Click **Load unpacked** and select `cka/pomodoro-extension/`.
4. The extension is pre-configured with CKA focus sessions and direct shortcuts to the CKA webapp at `http://localhost:5051`.

---

### Option B: Preparing ONLY for LFCS (Linux Foundation Certified SysAdmin)

You can work entirely inside the `lfcs/` folder without touching CKA:

```bash
cd lfcs

# 1. Run the terminal progress tracker & daily checklist
python3 study_todo.py

# 2. Launch the dedicated LFCS Web Dashboard & PSI Exam Simulator (http://localhost:5052)
bash webapp/start.sh

# 3. Generate or update all 48 LFCS daily HTML study guides
python3 generate_guides.py

# 4. Generate or rebuild all 48 LFCS labs and 4 PSI mock exams
python3 generate_labs.py

# 5. Import lfcs/schedule.ics into Google Calendar or Thunderbird
```

**Pomodoro Extension for LFCS:**
1. Open Google Chrome or Brave and go to `chrome://extensions/`.
2. Turn on **Developer mode** (top right).
3. Click **Load unpacked** and select `lfcs/pomodoro-extension/`.
4. The extension is pre-configured with LFCS focus sessions and direct shortcuts to the LFCS webapp at `http://localhost:5052`.

---

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

## 🖥 Lab Infrastructure (VirtualBox via Vagrant)

The lab environment runs locally on Oracle VirtualBox using automated Vagrant provisioning, adapted from [KodeKloud's Certified Kubernetes Administrator Course](https://github.com/kodekloudhub/certified-kubernetes-administrator-course/tree/master/kubeadm-clusters/virtualbox).

### Virtual Machine Topology

| VM Name | Hostname | Role | OS | CPUs | RAM | Default NAT IP | Forwarded SSH Port |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `controlplane` | `controlplane` | K8s Control Plane Master | Ubuntu 22.04 | 2 | 2048 MB | `192.168.56.11` | `2710 -> 22` |
| `node01` | `node01` | K8s Worker Node 1 | Ubuntu 22.04 | 1 | 1024 MB | `192.168.56.21` | `2721 -> 22` |
| `node02` | `node02` | K8s Worker Node 2 | Ubuntu 22.04 | 1 | 1024 MB | `192.168.56.22` | `2722 -> 22` |
| `LFCS` | `LFCS` | Linux SysAdmin Target | Ubuntu 22.04 | 2 | 2048 MB | `192.168.56.30` | `2730 -> 22` |

### Provisioning the Machines

```bash
cd vagrant

# Spin up all 4 machines (K8s cluster + LFCS machine):
vagrant up

# Or spin up only the Kubernetes cluster for CKA:
vagrant up controlplane node01 node02

# Or spin up only the Linux machine for LFCS:
vagrant up LFCS
```

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
4. Install CNI (Flannel):
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
   ```
5. Join `node01` and `node02` using the `kubeadm join` command produced by step 2.

---

## 🛠 Unified Lab CLI (`./lab`)

The repository root includes a master CLI orchestrator for administering scenarios and grading across all VMs:

```bash
# List all scenarios
./lab list

# Filter scenarios
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

## 📅 Schedule Synchronization

Both tracks follow structured, calendar-aligned syllabi with pause/recovery blocks:
- **CKA Calendar**: `cka/schedule.ics` (morning intensive blocks 08:00 - 12:00)
- **LFCS Calendar**: `lfcs/schedule.ics` (afternoon intensive blocks 15:00 - 18:00)
- **Master Combined Calendar**: `cka_lfcs_schedule.ics`

Compatible with Google Calendar, Apple Calendar, Thunderbird, and mobile calendar apps.

---

## 📜 Credits & Attributions

- Kubernetes cluster topology and provisioning scripts adapted from [KodeKloud - Certified Kubernetes Administrator Course](https://github.com/kodekloudhub/certified-kubernetes-administrator-course).
- Mock exam question formats and grading inspired by [killer.sh](https://killer.sh) and Linux Foundation exam guidelines.
