# ☸ CKA & 🐧 LFCS Hands-on Practice Labs, Mock Exams & Study Suite

A comprehensive, calendar-aligned preparation suite for the **Certified Kubernetes Administrator (CKA)** and **Linux Foundation Certified System Administrator (LFCS)** certifications.

Built for local execution on Oracle VirtualBox using automated Vagrant provisioning, an interactive terminal orchestrator, realistic killer.sh / PSI exam simulators, dedicated daily study guides, and productivity tooling.

---

## 📁 Repository Architecture

```text
labs_&_exams/
├── cka/                            # Certified Kubernetes Administrator Track
│   ├── guides/                     # 48 Track-specific CKA daily study guides & notes
│   ├── kodekloud_cka/              # KodeKloud CKA course notes and references
│   ├── mock-cka-1/                 # Full-scale CKA timed mock exam 1 (17 questions)
│   ├── mock-cka-2/                 # Full-scale CKA timed mock exam 2 (17 questions)
│   └── w1d1-cka/ ... w8d6-cka/     # 48 Calendar-aligned hands-on Kubernetes lab scenarios
│
├── lfcs/                           # Linux Foundation Certified SysAdmin Track
│   ├── guides/                     # 48 Track-specific LFCS daily study guides & notes
│   ├── mock-lfcs-1/ ... 4/         # 4 Full-scale LFCS timed mock exams (20 questions each)
│   └── w1d1-lfcs/ ... w8d6-lfcs/   # 48 Calendar-aligned hands-on Linux lab scenarios
│
├── vagrant/                        # Infrastructure & VM Provisioning (VirtualBox)
│   ├── Vagrantfile                 # Multi-node K8s cluster + LFCS VM definition
│   ├── docs/                       # Compute & connectivity prerequisites
│   └── ubuntu/                     # Provisioning scripts (kubeadm, containerd, hosts, ssh)
│
├── tools/                          # Consolidated Utilities, Webapp & Extension
│   ├── webapp/                     # Flask interactive dashboard & exam simulator
│   ├── pomodoro-extension/         # Manifest V3 Chrome Pomodoro study timer
│   ├── curriculum/                 # Python syllabus definitions & mock questions
│   ├── generate_daily_guide.py     # Parallel HTML/PDF daily study guide generator
│   ├── study_todo.py               # Terminal Curses daily checklist & progress tracker
│   ├── start_simulator.sh          # Killer.sh / PSI exam simulator launcher
│   └── start_webapp.sh             # Web dashboard launcher
│
├── lab                             # Unified CLI Orchestrator (start, check, solve, reset)
├── cka_lfcs_schedule.csv           # 8-Week Master Study Schedule (CSV)
├── cka_lfcs_schedule.ics           # 8-Week Master Study Schedule (iCalendar)
├── .gitignore
└── README.md
```

---

## 🖥 Lab Infrastructure (VirtualBox via Vagrant)

The VirtualBox lab environment is automated using Vagrant, adapted from [KodeKloud's Certified Kubernetes Administrator Course](https://github.com/kodekloudhub/certified-kubernetes-administrator-course/tree/master/kubeadm-clusters/virtualbox).

### Virtual Machine Topology

| VM Name | Hostname | Role | OS | Memory | CPUs | Default NAT IP | Port Forward |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `controlplane` | `controlplane` | K8s Control Plane Master | Ubuntu 22.04 | 2048 MB | 2 | `192.168.56.11` | `2710 -> 22` |
| `node01` | `node01` | K8s Worker Node 1 | Ubuntu 22.04 | 1024 MB | 1 | `192.168.56.21` | `2721 -> 22` |
| `node02` | `node02` | K8s Worker Node 2 | Ubuntu 22.04 | 1024 MB | 1 | `192.168.56.22` | `2722 -> 22` |
| `LFCS` | `LFCS` | Linux SysAdmin Target | Ubuntu 22.04 | 2048 MB | 2 | `192.168.56.30` | `2730 -> 22` |

### Spinning Up the VMs

```bash
cd vagrant

# Spin up all 4 machines (Kubernetes cluster + LFCS VM):
vagrant up

# Or spin up only the Kubernetes cluster:
vagrant up controlplane node01 node02

# Or spin up only the LFCS machine:
vagrant up LFCS
```

### Initializing the Kubernetes Cluster
1. SSH into the control plane:
   ```bash
   vagrant ssh controlplane
   ```
2. Run kubeadm init:
   ```bash
   sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=$(cat /usr/local/bin/public-ip)
   ```
3. Configure `kubectl` access:
   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```
4. Install CNI (Flannel):
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/flannel-io/flannel/master/Documentation/kube-flannel.yml
   ```
5. Join worker nodes (`node01`, `node02`) using the `kubeadm join` token output.

---

## 🛠 Unified Lab CLI (`./lab`)

Use the root `./lab` command to manage all lab scenarios, grading, and VM sessions:

```bash
# List all 100 hands-on scenarios across Weeks 1-8
./lab list

# Filter by track or week
./lab list cka
./lab list lfcs
./lab list w2

# Start a scenario (injects broken state / initial manifests into target VM)
./lab start w1d1-cka
./lab start w1d1-lfcs

# View the problem statement & objectives
./lab show w1d1-cka

# Verify and grade your solution
./lab check w1d1-cka

# View official step-by-step walkthrough & solution
./lab solve w1d1-cka

# Clean up scenario artifacts and restore clean state
./lab reset w1d1-cka

# Check VirtualBox VM status
./lab vm status
./lab vm start

# Direct SSH shortcut into VMs
./lab ssh controlplane
./lab ssh node01
./lab ssh node02
./lab ssh lfcs
```

---

## 🎓 Track-Separated Study Guides

Each study day includes dedicated, self-contained guides in HTML format:

- **CKA Guides** (`cka/guides/`):
  - Focuses on morning 4-hour Kubernetes deep dive
  - Architectural theory, component lifecycle & etcd internals
  - High-resolution SVG topology diagrams
  - Daily speed drills and kubectl imperative aliases
  - Full hands-on lab task & grader solution walkthrough
  - CKA-only self-assessment checklist

- **LFCS Guides** (`lfcs/guides/`):
  - Focuses on afternoon 3-hour Linux administration mastery
  - Storage (LVM, RAID, ext4/xfs), networking, systemd, user management, and diagnostics
  - Architectural concept diagrams
  - Daily speed drills and bash shortcuts
  - Full hands-on lab task & grader solution walkthrough
  - LFCS-only self-assessment checklist

### Re-generating Guides
```bash
# Generate both guides for a specific day
python3 tools/generate_daily_guide.py w1d1

# Generate only CKA or LFCS guide
python3 tools/generate_daily_guide.py w1d1 --cka
python3 tools/generate_daily_guide.py w1d1 --lfcs

# Batch generate all 48 days (96 guides total) in parallel
python3 tools/generate_daily_guide.py --all
```

---

## 💻 Exam Simulator & Web Dashboard

Reproduces the **killer.sh** and **PSI Secure Browser** remote desktop experience:

- Split terminal connected live to cluster nodes
- Restricted documentation browser
- 120-minute timed countdown with alerts
- Automated grader adhering to official domain weightings

```bash
# Launch interactive mock exam simulator
./lab exam mock-cka-1
./lab exam mock-lfcs-1

# Launch the general Study Todo web dashboard (port 5050)
bash tools/start_webapp.sh
```

---

## ⏱ Chrome Pomodoro Study Timer Extension

Located in `tools/pomodoro-extension/`. A Manifest V3 Chrome extension featuring:
- Time-blocked sessions (50m study / 10m break)
- Audio alerts and notifications
- Persistent study history tracking

### Installation
1. Open Google Chrome / Brave and navigate to `chrome://extensions/`.
2. Enable **Developer mode** (toggle in upper right).
3. Click **Load unpacked** and select `tools/pomodoro-extension/`.

---

## 📅 Schedule Synchronization

The study plan follows an 8-week structured roadmap:
- **Morning (08:00 - 12:00)**: CKA Deep Dive & Terminal Practice
- **Midday (12:00 - 15:00)**: Cognitive Reset & Integration Break
- **Afternoon (15:00 - 18:00)**: LFCS Deep Dive & Hands-on Labs
- Synchronized via `cka_lfcs_schedule.ics` (importable into Google Calendar, Apple Calendar, or Thunderbird).
