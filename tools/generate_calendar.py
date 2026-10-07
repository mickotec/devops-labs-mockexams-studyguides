#!/usr/bin/env python3
"""
CKA & LFCS 8-Week Study Calendar Generator
Strict Timings:
 - CKA: 8:00 AM - 12:00 PM
 - Recovery: 12:00 PM - 3:00 PM
 - LFCS: 3:00 PM - 6:00 PM
"""

import sys
from datetime import datetime, timedelta

def build_8week_events(start_monday_str="2026-09-14"):
    start_monday = datetime.strptime(start_monday_str, "%Y-%m-%d")
    
    days_curriculum = [
        # ==================== WEEK 1 ====================
        {
            "week": 1, "day_name": "Monday", "offset": 0,
            "cka_title": "Kubernetes Architecture & Container Runtimes",
            "cka_desc": "08:00 AM - 08:20 AM: Warm-up: Sketch Kubernetes control plane components from memory\n08:20 AM - 09:30 AM: Theory: API Server, Controller Manager, Scheduler, Kubelet, Kube-proxy, ContainerD vs Docker\n09:30 AM - 09:45 AM: Movement & Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Explore cluster components & ContainerD\n11:15 AM - 11:30 AM: Eye rest & mobility\n11:30 AM - 12:00 PM: Exploratory: Inspect running static pod manifests in /etc/kubernetes/manifests",
            "lfcs_title": "Consoles, Navigation & System Documentation",
            "lfcs_desc": "03:00 PM - 03:20 PM: Terminal navigation speed drills (cd, pushd, popd, ls flags)\n03:20 PM - 04:20 PM: Theory: Graphical vs text consoles, man pages (sections 1, 5, 8), info, --help\n04:20 PM - 04:35 PM: Walk & cognitive reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Logging in and System Documentation\n05:35 PM - 06:00 PM: Cheat sheet update: Documentation lookup recipes"
        },
        {
            "week": 1, "day_name": "Tuesday", "offset": 1,
            "cka_title": "ETCD Fundamentals & Cluster State Store",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Role of ETCD in consensus and high availability\n08:20 AM - 09:30 AM: Theory: Key-value store, Raft protocol overview, etcd in Kubernetes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: etcd for Beginners & etcd in Kubernetes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Querying etcd endpoint health and members",
            "lfcs_title": "Files, Directories, Hard & Soft Links",
            "lfcs_desc": "03:00 PM - 03:20 PM: File operation warm-up (mkdir -p, cp -r, rm -rf safety)\n03:20 PM - 04:20 PM: Theory: Inodes, hard links vs symbolic links (ln vs ln -s), link limits across filesystems\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Files, Directories, Hard and Soft Links\n05:35 PM - 06:00 PM: Synthesis: Inode verification drills with ls -i"
        },
        {
            "week": 1, "day_name": "Wednesday", "offset": 2,
            "cka_title": "Pod Internals & YAML Architecture",
            "cka_desc": "08:00 AM - 08:20 AM: Speed drill: Write a complete Pod YAML from memory\n08:20 AM - 09:30 AM: Theory: Pod specification, containers, ports, environment, volumes layout\n09:30 AM - 09:45 AM: Hydration & stretching\n09:45 AM - 11:15 AM: KodeKloud Labs: Pods & Pods with YAML\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Break YAML indentation and observe kubectl error parsers",
            "lfcs_title": "Standard Linux File Permissions",
            "lfcs_desc": "03:00 PM - 03:20 PM: Octal permission conversion warm-up (rwx calculations)\n03:20 PM - 04:20 PM: Theory: Owner, group, other (ugo), chmod (numeric vs symbolic), chown, chgrp, umask\n04:20 PM - 04:35 PM: Physical reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Standard File Permissions\n05:35 PM - 06:00 PM: Synthesis: Default umask calculation drills"
        },
        {
            "week": 1, "day_name": "Thursday", "offset": 3,
            "cka_title": "Multi-Container Pod Patterns & Init Containers",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Pod shared network and IPC namespaces\n08:20 AM - 09:30 AM: Theory: Sidecar, adapter, and ambassador design patterns; initContainers order of execution\n09:30 AM - 09:45 AM: Movement & posture check\n09:45 AM - 11:15 AM: KodeKloud Labs: Multi-Container Pods & Init Containers\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Shared volume logging sidecar demo",
            "lfcs_title": "Special Permissions: SUID, SGID & Sticky Bit",
            "lfcs_desc": "03:00 PM - 03:20 PM: Permission bit calculation drills (4000, 2000, 1000)\n03:20 PM - 04:20 PM: Theory: SUID execution as owner, SGID for shared directories, Sticky bit on /tmp\n04:20 PM - 04:35 PM: Walk break\n04:35 PM - 05:35 PM: KodeKloud Labs: SUID, SGID, and Sticky Bit\n05:35 PM - 06:00 PM: Command ledger update: find / -perm /4000 drills"
        },
        {
            "week": 1, "day_name": "Friday", "offset": 4,
            "cka_title": "Fast Imperative CLI Mastery with Kubectl",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Fast imperative command generator syntax\n08:20 AM - 09:30 AM: Theory: Imperative vs declarative, kubectl run, create, expose, --dry-run=client -o yaml\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Imperative Commands with Kubectl\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Speed Synthesis: Set up ~/.bashrc aliases (k, do, now) and vimrc tabstop settings",
            "lfcs_title": "Pagers, Vim Mastery & Terminal Editing",
            "lfcs_desc": "03:00 PM - 03:20 PM: Vim navigation warm-up (hjkl, w, b, gg, G, 0, $)\n03:20 PM - 04:20 PM: Theory: Vim command vs insert mode, visual selection, yanking, search/replace (:s/old/new/g)\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Pagers and VI\n05:35 PM - 06:00 PM: Error Ledger review & personal ~/.vimrc configuration"
        },
        {
            "week": 1, "day_name": "Saturday", "offset": 5,
            "cka_title": "Week 1 Integration & Speedrun Drill",
            "cka_desc": "08:00 AM - 09:30 AM: Review Week 1 error notes and YAML structures\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:00 AM: Speed Drill: Generate 20 different Pod manifests without documentation in 20 min\n11:00 AM - 12:00 PM: Milestone Assessment 1: Pod deployment and multi-container debugging",
            "lfcs_title": "Week 1 Consolidation & Permission Auditing",
            "lfcs_desc": "03:00 PM - 04:15 PM: Permissions speed drill: Audit and enforce correct SUID/SGID/Sticky bits across a mock directory tree\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: VimGolf / openvim speed challenge\n05:30 PM - 06:00 PM: Milestone Assessment 1: System permissions verification"
        },

        # ==================== WEEK 2 ====================
        {
            "week": 2, "day_name": "Monday", "offset": 7,
            "cka_title": "ReplicaSets & Self-Healing Controllers",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: ReplicaSet matchLabels vs Pod template labels\n08:20 AM - 09:30 AM: Theory: Controller manager loops, desired vs current state, scaling ReplicaSets\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: ReplicaSets\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Deleting pods to witness reconciliation loop in real time",
            "lfcs_title": "File Searching with Find and Locate",
            "lfcs_desc": "03:00 PM - 03:20 PM: find command warm-up (-name, -type f, -type d)\n03:20 PM - 04:20 PM: Theory: find expressions (-size, -mtime, -user, -perm), -exec vs xargs, locate vs updatedb\n04:20 PM - 04:35 PM: Walk & mental reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Search for Files\n05:35 PM - 06:00 PM: Synthesis: Complex find -exec chmod/rm one-liners"
        },
        {
            "week": 2, "day_name": "Tuesday", "offset": 8,
            "cka_title": "Deployments, Rollouts & Revisions",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Deployment vs ReplicaSet relationship\n08:20 AM - 09:30 AM: Theory: RollingUpdate strategy, maxSurge, maxUnavailable, rollout status, rollout history\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Deployments & Rollout Updates\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Rollout undo to a specific previous revision (--to-revision)",
            "lfcs_title": "Text Processing: Grep & Regular Expressions",
            "lfcs_desc": "03:00 PM - 03:20 PM: Regex anchors drill (^, $, .)\n03:20 PM - 04:20 PM: Theory: grep flags (-i, -v, -r, -n, -E), Basic Regular Expressions (BRE) vs Extended (ERE)\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Search File Using Grep & Regex\n05:35 PM - 06:00 PM: Cheat sheet update: High-yield regex pattern catalog"
        },
        {
            "week": 2, "day_name": "Wednesday", "offset": 9,
            "cka_title": "Services: ClusterIP, NodePort & LoadBalancer",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Service targetPort vs port vs nodePort\n08:20 AM - 09:30 AM: Theory: kube-proxy IPTables/IPVS modes, Endpoints, headless services, service discovery\n09:30 AM - 09:45 AM: Hydration & stretch\n09:45 AM - 11:15 AM: KodeKloud Labs: Services (ClusterIP & NodePort)\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Inspecting cluster iptables rules generated for a Service",
            "lfcs_title": "Advanced Stream Analysis: Sed & Awk Fundamentals",
            "lfcs_desc": "03:00 PM - 03:20 PM: Piping warm-up (cat, cut, sort, uniq -c)\n03:20 PM - 04:20 PM: Theory: sed line replacement (sed 's/foo/bar/g'), awk column extraction (awk '{print $1, $3}')\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: Practical Terminal Drills: Parse /etc/passwd and /etc/group using awk and sed\n05:35 PM - 06:00 PM: Synthesis: Formatting system metrics with awk"
        },
        {
            "week": 2, "day_name": "Thursday", "offset": 10,
            "cka_title": "Namespaces & DNS Resolution Inside Clusters",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: FQDN structure (svc.cluster.local)\n08:20 AM - 09:30 AM: Theory: Namespace isolation, CoreDNS resolution, cross-namespace service communication\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Namespaces & CoreDNS Exploration\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Launch temporary busybox pod for nslookup and curl tests",
            "lfcs_title": "I/O Redirection & Stream Multiplexing",
            "lfcs_desc": "03:00 PM - 03:20 PM: Redirection warm-up (stdout, stderr, &>)\n03:20 PM - 04:20 PM: Theory: File descriptors (0, 1, 2), redirecting stderr (2>), appending (>>), pipelines (|), tee\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Use Input-Output Redirection\n05:35 PM - 06:00 PM: Terminal drill: Redirecting output and errors to separate log files"
        },
        {
            "week": 2, "day_name": "Friday", "offset": 11,
            "cka_title": "Kubectl Explain & Declarative Workflow",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Fast navigation using kubectl explain --recursive\n08:20 AM - 09:30 AM: Theory: kubectl apply algorithm, last-applied-configuration annotation, manifest management\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Kubectl Apply Command & Imperative vs Declarative\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Synthesis: Constructing a complete 3-tier app manifest declaratively",
            "lfcs_title": "Archiving, Compression & Remote Backups",
            "lfcs_desc": "03:00 PM - 03:20 PM: Tar flags drill (-czvf, -xzvf, -cjvf, -xpvf)\n03:20 PM - 04:20 PM: Theory: tar, gzip, bzip2, xz compression ratios, preserving permissions (-p), rsync basics\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Archive, Back Up, Compress, Unpack\n05:35 PM - 06:00 PM: Synthesis: Automated incremental tar backup script"
        },
        {
            "week": 2, "day_name": "Saturday", "offset": 12,
            "cka_title": "Week 2 Speed Drills & Controller Triathlon",
            "cka_desc": "08:00 AM - 09:30 AM: Speed drill: Build Pod + Deployment + Service in under 7 minutes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Rolling update failure scenario & rollback under pressure\n11:00 AM - 12:00 PM: Milestone 2 Assessment: Multi-tier deployment with namespace routing",
            "lfcs_title": "Week 2 Speed Drills & Git Version Control",
            "lfcs_desc": "03:00 PM - 04:15 PM: Git operations: init, stage, commit, branch, merge, diff, remote tracking\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Fast text stream filtering marathon (parse 10,000 log lines with grep/sed/awk)\n05:30 PM - 06:00 PM: Milestone 2 Assessment: Text processing & archive verification"
        },

        # ==================== WEEK 3 ====================
        {
            "week": 3, "day_name": "Monday", "offset": 14,
            "cka_title": "Manual Scheduling, Labels & Selectors",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: nodeName attribute in Pod spec\n08:20 AM - 09:30 AM: Theory: Scheduler bypass via nodeName, label management, matchExpressions vs matchLabels\n09:30 AM - 09:45 AM: Movement break\n09:45 AM - 11:15 AM: KodeKloud Labs: Manual Scheduling, Labels and Selectors\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Manually binding an unscheduled pod via binding API",
            "lfcs_title": "Linux Boot Architecture & GRUB2",
            "lfcs_desc": "03:00 PM - 03:20 PM: Boot sequence recall (BIOS/UEFI -> MBR/GPT -> GRUB2 -> Kernel -> Init)\n03:20 PM - 04:20 PM: Theory: GRUB2 configuration (/etc/default/grub, grub2-mkconfig), kernel parameters at boot\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Boot, Reboot, and Shutdown a System Safely\n05:35 PM - 06:00 PM: Synthesis: Interrupting boot to access emergency/rescue target"
        },
        {
            "week": 3, "day_name": "Tuesday", "offset": 15,
            "cka_title": "Taints, Tolerations & Node Affinity",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Taints repel pods, Affinity attracts pods\n08:20 AM - 09:30 AM: Theory: Taint effects (NoSchedule, PreferNoSchedule, NoExecute), nodeAffinity (required vs preferred)\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Taints & Tolerations, Node Affinity\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Evicting running pods using NoExecute taints",
            "lfcs_title": "Systemd Targets & Runlevel Management",
            "lfcs_desc": "03:00 PM - 03:20 PM: Runlevel to systemd target mapping drills (3=multi-user, 5=graphical)\n03:20 PM - 04:20 PM: Theory: systemctl get-default, set-default, isolate, emergency.target vs rescue.target\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Boot or Change System Into Different Operating Modes\n05:35 PM - 06:00 PM: Summary notes & recovery workflows"
        },
        {
            "week": 3, "day_name": "Wednesday", "offset": 16,
            "cka_title": "Resource Requirements, Limits & LimitRanges",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: CPU millis (1000m = 1 core) and Memory mebibytes (Mi vs MB)\n08:20 AM - 09:30 AM: Theory: Requests vs limits, OOMKilled status (Exit code 137), CPU throttling, LimitRanges\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Resource Requirements & Limits\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Simulating memory leak pod to witness OOMKilled",
            "lfcs_title": "Creating & Managing Systemd Services",
            "lfcs_desc": "03:00 PM - 03:20 PM: systemctl status/start/stop/restart/reload warm-up\n03:20 PM - 04:20 PM: Theory: Unit file layout (/etc/systemd/system/), [Unit], [Service] (ExecStart, Restart), [Install]\n04:20 PM - 04:35 PM: Walk & posture check\n04:35 PM - 05:35 PM: KodeKloud Labs: Create systemd Services\n05:35 PM - 06:00 PM: Synthesis: Write a custom Python/Bash background service from scratch"
        },
        {
            "week": 3, "day_name": "Thursday", "offset": 17,
            "cka_title": "DaemonSets & Static Pods Architecture",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Where are control plane static pod manifests stored?\n08:20 AM - 09:30 AM: Theory: DaemonSets scheduling, static pods managed directly by kubelet, /etc/kubernetes/manifests\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: DaemonSets & Static Pods\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Deploying custom static pod on worker node and verifying node name suffix",
            "lfcs_title": "Process Diagnostics & Signal Management",
            "lfcs_desc": "03:00 PM - 03:20 PM: ps aux / pgrep warm-up\n03:20 PM - 04:20 PM: Theory: Process states (R, S, D, Z), signals (SIGTERM 15, SIGKILL 9, SIGHUP 1), nice & renice\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Diagnose and Manage Processes\n05:35 PM - 06:00 PM: Synthesis: Killing runaway processes and identifying zombie processes"
        },
        {
            "week": 3, "day_name": "Friday", "offset": 18,
            "cka_title": "Priority Classes & Multiple Schedulers",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: PriorityClass value ranges and preemption policy\n08:20 AM - 09:30 AM: Theory: PriorityClass, Pod preemption, deploying a secondary custom kube-scheduler\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:15 AM: KodeKloud Labs: Priority Classes & Multiple Schedulers\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Assigning pods to custom scheduler via schedulerName",
            "lfcs_title": "System Integrity, Resource Monitoring & Top",
            "lfcs_desc": "03:00 PM - 03:20 PM: top / htop interactive shortcut drills (P, M, k, r)\n03:20 PM - 04:20 PM: Theory: System load averages (1, 5, 15 min), uptime, free -m, vmstat, iostat, lsof\n04:20 PM - 04:35 PM: Physical walk\n04:35 PM - 05:35 PM: KodeKloud Labs: Verify Integrity and Availability of Resources and Processes\n05:35 PM - 06:00 PM: Error Ledger analysis"
        },
        {
            "week": 3, "day_name": "Saturday", "offset": 19,
            "cka_title": "Week 3 Scheduling Troubleshooting Matrix",
            "cka_desc": "08:00 AM - 09:30 AM: Debugging 10 pods stuck in Pending state (Taints, Affinities, Resources, NodeSelector)\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Static pod troubleshooting (broken manifest path in kubelet config)\n11:00 AM - 12:00 PM: Milestone 3 Assessment: Advanced scheduling orchestration",
            "lfcs_title": "Week 3 Systemd & Process Orchestration",
            "lfcs_desc": "03:00 PM - 04:15 PM: Build custom systemd service with automated restart on failure and log output\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Process troubleshooting under memory/CPU stress (stress/stress-ng drills)\n05:30 PM - 06:00 PM: Milestone 3 Assessment: Service & process resilience"
        },

        # ==================== WEEK 4 ====================
        {
            "week": 4, "day_name": "Monday", "offset": 21,
            "cka_title": "Commands & Arguments (Docker vs Kubernetes)",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: ENTRYPOINT = command, CMD = args mapping\n08:20 AM - 09:30 AM: Theory: Overriding container entrypoint/cmd, passing environment variables\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Commands and Arguments in Kubernetes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Sleeping pods for debugging using command override",
            "lfcs_title": "Journald & System Log File Analysis",
            "lfcs_desc": "03:00 PM - 03:20 PM: journalctl flag speedrun (-u, -f, -p err, --since)\n03:20 PM - 04:20 PM: Theory: Systemd journal storage (volatile vs persistent /var/log/journal), rsyslog, /var/log/auth.log\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Locate and Analyze System Log Files\n05:35 PM - 06:00 PM: Synthesis: Log auditing with journalctl and logrotate review"
        },
        {
            "week": 4, "day_name": "Tuesday", "offset": 22,
            "cka_title": "ConfigMaps & Application Configuration",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Creating ConfigMap from literal vs from file\n08:20 AM - 09:30 AM: Theory: ConfigMaps as environment variables (env, envFrom) and as mounted volume files\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Configuring ConfigMaps in Applications\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Hot-reloading application configuration from volume mounts",
            "lfcs_title": "Task Scheduling with Cron and At",
            "lfcs_desc": "03:00 PM - 03:20 PM: Cron 5-field syntax drill (minute, hour, day, month, weekday)\n03:20 PM - 04:20 PM: Theory: crontab -e, crontab -l, /etc/crontab, /etc/cron.*, at, atq, atrm, batch\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Schedule Tasks to Run at a Set Date and Time\n05:35 PM - 06:00 PM: Synthesis: Setting up automated disk monitoring cron job"
        },
        {
            "week": 4, "day_name": "Wednesday", "offset": 23,
            "cka_title": "Secrets Management & Encryption at Rest",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Base64 encoding vs encryption (echo -n ... | base64)\n08:20 AM - 09:30 AM: Theory: Generic, docker-registry, tls secrets; configuring EncryptionConfiguration on kube-apiserver\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Secrets & Encrypting Secret Data at Rest\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Verifying encrypted data directly inside etcd database",
            "lfcs_title": "Package Managers (APT, DNF/YUM & RPM)",
            "lfcs_desc": "03:00 PM - 03:20 PM: Package manager command comparison drills\n03:20 PM - 04:20 PM: Theory: apt update/install/purge, dpkg -i/-l, dnf/yum install/remove, rpm -ivh/-qa, repo configs\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage Software with Package Manager & Repositories\n05:35 PM - 06:00 PM: Synthesis: Adding third-party repository and verifying GPG keys"
        },
        {
            "week": 4, "day_name": "Thursday", "offset": 24,
            "cka_title": "Autoscaling: HPA, VPA & In-Place Pod Resize",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Metrics-server installation verification (kubectl top)\n08:20 AM - 09:30 AM: Theory: Horizontal Pod Autoscaler (HPA v2), Vertical Pod Autoscaler (VPA), In-place resize (2025)\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: HPA, VPA & Modifying CPU Resources in VPA\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Generating CPU load to trigger HPA pod scaling",
            "lfcs_title": "Compiling Software from Source Code",
            "lfcs_desc": "03:00 PM - 03:20 PM: Tar extraction & build tools warm-up (gcc, make)\n03:20 PM - 04:20 PM: Theory: ./configure flags (--prefix), make compilation, make install, managing shared libraries (ldconfig)\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Install Software by Compiling Source Code\n05:35 PM - 06:00 PM: Synthesis: Custom compile and install of a utility tool"
        },
        {
            "week": 4, "day_name": "Friday", "offset": 25,
            "cka_title": "Admission Controllers & Validating Webhooks",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Kubernetes API request pipeline (Authn -> Authz -> Admission)\n08:20 AM - 09:30 AM: Theory: Built-in controllers (NamespaceLifecycle, LimitRanger), Mutating vs Validating webhooks\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Admission Controllers & Validating/Mutating Webhooks\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Enabling and disabling admission plugins in kube-apiserver manifest",
            "lfcs_title": "Bash Automation & Maintenance Scripting",
            "lfcs_desc": "03:00 PM - 03:20 PM: Bash syntax warm-up (variables, conditionals [ ], exit codes $?)\n03:20 PM - 04:20 PM: Theory: Positional parameters ($1, $@), loops (for, while), functions, error handling (set -e)\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: Practical Scripting Lab: Write an automated log rotation and cleanup maintenance script\n05:35 PM - 06:00 PM: Script review and execution"
        },
        {
            "week": 4, "day_name": "Saturday", "offset": 26,
            "cka_title": "Week 4 App Lifecycle & Secret Security Drill",
            "cka_desc": "08:00 AM - 09:30 AM: Timed deployment with ConfigMap, Secret, encrypted at rest, and HPA autoscaling\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Debugging Secret decoding and environment injection errors\n11:00 AM - 12:00 PM: Milestone 4 Assessment: Application Lifecycle Mastery",
            "lfcs_title": "Week 4 System Automation & Maintenance Triathlon",
            "lfcs_desc": "03:00 PM - 04:15 PM: Automate system backup and log cleanup using custom cron and bash script\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Package troubleshooting and repository recovery drill\n05:30 PM - 06:00 PM: Milestone 4 Assessment: Scripting and service automation"
        },

        # ==================== WEEK 5 ====================
        {
            "week": 5, "day_name": "Monday", "offset": 28,
            "cka_title": "Node Maintenance: Cordon, Drain & Uncordon",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: cordon vs drain vs drain --ignore-daemonsets\n08:20 AM - 09:30 AM: Theory: Safe workload eviction, PodDisruptionBudgets (PDB), node scheduling states\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: OS Upgrades & Maintenance\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Evicting pods respecting PDB minAvailable / maxUnavailable",
            "lfcs_title": "Local User Management & /etc/passwd",
            "lfcs_desc": "03:00 PM - 03:20 PM: useradd / usermod flag drills (-u, -g, -G, -d, -s)\n03:20 PM - 04:20 PM: Theory: User IDs, system users vs regular users, /etc/passwd fields, /etc/shadow fields, userdel\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Create, Delete, and Modify Local User Accounts\n05:35 PM - 06:00 PM: Synthesis: User account expiration and password policy enforcement (chage)"
        },
        {
            "week": 5, "day_name": "Tuesday", "offset": 29,
            "cka_title": "Cluster Upgrade: Kubeadm Control Plane",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Kubernetes version skew policy rules\n08:20 AM - 09:30 AM: Theory: kubeadm upgrade plan, upgrading kubeadm, kubelet, kubectl on primary master\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Cluster Upgrade Process - Control Plane\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Verifying control plane component versions after upgrade",
            "lfcs_title": "Groups, Sudo Privileges & Visudo",
            "lfcs_desc": "03:00 PM - 03:20 PM: groupadd / groupmod drills\n03:20 PM - 04:20 PM: Theory: /etc/group, group passwords, /etc/sudoers format (User Host=(Runas) Commands), visudo safety\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Groups & Sudo Privileges\n05:35 PM - 06:00 PM: Synthesis: Granting passwordless sudo to specific administrative commands"
        },
        {
            "week": 5, "day_name": "Wednesday", "offset": 30,
            "cka_title": "Cluster Upgrade: Worker Nodes",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Steps on worker node: drain -> upgrade kubeadm -> upgrade kubelet -> uncordon\n08:20 AM - 09:30 AM: Theory: Safe worker node rollouts without downtime, daemonset pod handling\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Cluster Upgrade Process - Worker Nodes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Speed Drill: Upgrading worker node in under 6 minutes",
            "lfcs_title": "Profiles, Template Environments & User Limits",
            "lfcs_desc": "03:00 PM - 03:20 PM: Login vs non-login shell startup file drills\n03:20 PM - 04:20 PM: Theory: /etc/profile, /etc/bashrc, ~/.bash_profile, /etc/skel skeleton files, /etc/security/limits.conf\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage Profiles & User Resource Limits\n05:35 PM - 06:00 PM: Synthesis: Restricting max user processes (nproc) and open files (nofile)"
        },
        {
            "week": 5, "day_name": "Thursday", "offset": 31,
            "cka_title": "ETCD Snapshot Backup & Disaster Recovery",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Mandatory ETCDCTL environment variables and flags\n08:20 AM - 09:30 AM: Theory: ETCDCTL_API=3 snapshot save, snapshot restore, swapping data-dir in static pod manifest\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Backup and Restore Methods (ETCD)\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Speed Drill: Timed ETCD backup and complete cluster recovery from snapshot",
            "lfcs_title": "Kernel Runtime Tuning with Sysctl",
            "lfcs_desc": "03:00 PM - 03:20 PM: sysctl inspection drills (sysctl -a | grep ip_forward)\n03:20 PM - 04:20 PM: Theory: /proc/sys filesystem, ephemeral tuning (sysctl -w), persistent configuration (/etc/sysctl.conf)\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Change Kernel Runtime Parameters\n05:35 PM - 06:00 PM: Synthesis: Enabling IP forwarding and adjusting virtual memory swappiness"
        },
        {
            "week": 5, "day_name": "Friday", "offset": 32,
            "cka_title": "TLS Basics & PKI in Kubernetes",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Symmetric vs asymmetric encryption and certificate chains\n08:20 AM - 09:30 AM: Theory: Kubernetes CA, server certs, client certs, inspecting certificate details with openssl\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: TLS Basics & View Certificate Details\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Diagnosing expired certificate errors on kube-apiserver",
            "lfcs_title": "Mandatory Access Control: SELinux & AppArmor",
            "lfcs_desc": "03:00 PM - 03:20 PM: SELinux mode check (getenforce, sestatus)\n03:20 PM - 04:20 PM: Theory: DAC vs MAC, SELinux contexts (user:role:type:level), semanage, restorecon, chcon, /etc/selinux/config\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: SELinux Contexts & Policy Enforcement\n05:35 PM - 06:00 PM: Error Ledger review: SELinux denial analysis (ausearch, audit2why)"
        },
        {
            "week": 5, "day_name": "Saturday", "offset": 33,
            "cka_title": "Full Disaster Recovery & Upgrade Drill",
            "cka_desc": "08:00 AM - 09:30 AM: Disaster Simulation: Control plane crash + etcd snapshot restore under 15 minutes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Full multi-node kubeadm upgrade across 3 nodes\n11:00 AM - 12:00 PM: Milestone 5 Assessment: Disaster recovery & cluster maintenance",
            "lfcs_title": "Security Audit, User Quarantine & Recovery",
            "lfcs_desc": "03:00 PM - 04:15 PM: Lock down compromised user accounts, audit root privileges, repair corrupted sudoers file\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Troubleshoot and fix web server blocked by SELinux context\n05:30 PM - 06:00 PM: Milestone 5 Assessment: Security & access audit verification"
        },

        # ==================== WEEK 6 ====================
        {
            "week": 6, "day_name": "Monday", "offset": 35,
            "cka_title": "Certificates API & KubeConfig Management",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: CertificateSigningRequest (CSR) manifest structure\n08:20 AM - 09:30 AM: Theory: CSR approval workflow (kubectl certificate approve), Kubeconfig clusters, users, contexts\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Certificates API & KubeConfig\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Generating custom user kubeconfig with client certs and key",
            "lfcs_title": "Storage Partitions (MBR vs GPT) & Swap",
            "lfcs_desc": "03:00 PM - 03:20 PM: Storage listing drills (lsblk, blkid, fdisk -l)\n03:20 PM - 04:20 PM: Theory: MBR vs GPT partition tables, fdisk, gdisk, parted, creating and activating swap (mkswap, swapon)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage Partitions and Swap Space\n05:35 PM - 06:00 PM: Synthesis: Permanent swap configuration in /etc/fstab"
        },
        {
            "week": 6, "day_name": "Tuesday", "offset": 36,
            "cka_title": "RBAC (Roles, RoleBindings & ClusterRoles)",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Role vs ClusterRole scope\n08:20 AM - 09:30 AM: Theory: apiGroups, resources, verbs, subjects, RoleBindings, ClusterRoleBindings, kubectl auth can-i\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Role-Based Access Controls & Cluster Roles\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Testing developer permissions via --as=developer flag",
            "lfcs_title": "Filesystems & Boot Mounting (/etc/fstab)",
            "lfcs_desc": "03:00 PM - 03:20 PM: Filesystem creation commands (mkfs.ext4, mkfs.xfs)\n03:20 PM - 04:20 PM: Theory: Ext4 vs XFS features, mount options (ro, rw, noexec, nodev), /etc/fstab 6-field layout, UUID mounting\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Create Filesystems and Mount Them at Boot\n05:35 PM - 06:00 PM: Synthesis: Safe mounting tests with mount -a"
        },
        {
            "week": 6, "day_name": "Wednesday", "offset": 37,
            "cka_title": "ServiceAccounts & SecurityContexts",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: ServiceAccount token projection\n08:20 AM - 09:30 AM: Theory: ServiceAccounts, default tokens, Pod Security Standards, runAsUser, runAsNonRoot, capabilities\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Service Accounts & Security Contexts\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Adding NET_ADMIN capability to a pod",
            "lfcs_title": "Logical Volume Management (LVM) Architecture",
            "lfcs_desc": "03:00 PM - 03:20 PM: LVM hierarchy recall (Physical Devices -> PV -> VG -> LV -> Filesystem)\n03:20 PM - 04:20 PM: Theory: pvcreate, vgcreate, lvcreate, Volume Groups, Logical Volumes, PE (Physical Extents)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage and Configure LVM Storage\n05:35 PM - 06:00 PM: Synthesis: Creating and formatting a 2GB LVM volume"
        },
        {
            "week": 6, "day_name": "Thursday", "offset": 38,
            "cka_title": "Storage: Volumes, PV, PVC & StorageClasses",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: PV and PVC binding criteria (accessModes, capacity, storageClassName)\n08:20 AM - 09:30 AM: Theory: Persistent Volumes, PVCs, StorageClasses, dynamic volume provisioning, reclaim policies\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Persistent Volumes and Storage Classes\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Retain vs Delete reclaim policy verification",
            "lfcs_title": "Dynamic LVM Volume Expansion",
            "lfcs_desc": "03:00 PM - 03:20 PM: lvextend flag speedrun (-L +1G, -r, resize2fs, xfs_growfs)\n03:20 PM - 04:20 PM: Theory: Non-destructive volume expansion, resizing Ext4 vs XFS filesystems while mounted\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: Practical Terminal Lab: Extend an active LVM volume by 500MB without unmounting or data loss\n05:35 PM - 06:00 PM: Synthesis: Extending a Volume Group with a new physical disk (vgextend)"
        },
        {
            "week": 6, "day_name": "Friday", "offset": 39,
            "cka_title": "Helm & Kustomize (2025 Updates)",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Helm chart layout vs Kustomize directory structure\n08:20 AM - 09:30 AM: Theory: Helm repo/install/upgrade/values, Kustomize kustomization.yaml, overlays, transformers, patches\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:15 AM: KodeKloud Labs: Helm Basics & Kustomize Basics\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Generating patched environments using kustomize build",
            "lfcs_title": "Remote Filesystems: NFS & Storage Monitoring",
            "lfcs_desc": "03:00 PM - 03:20 PM: NFS export syntax drills (/etc/exports)\n03:20 PM - 04:20 PM: Theory: NFS server configuration, exportfs -r, NFS client mounting, storage performance monitoring (df -h, du -sh, iostat)\n04:20 PM - 04:35 PM: Walk break\n04:35 PM - 05:35 PM: KodeKloud Labs: Remote Filesystems (NFS) & Monitor Storage Performance\n05:35 PM - 06:00 PM: Error Ledger review"
        },
        {
            "week": 6, "day_name": "Saturday", "offset": 40,
            "cka_title": "Security & Storage Lab Triathlon",
            "cka_desc": "08:00 AM - 09:30 AM: Multi-tenant RBAC + ServiceAccount + PVC volume mounting scenario\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Helm chart deployment with custom values and Kustomize overlay\n11:00 AM - 12:00 PM: Milestone 6 Assessment: Enterprise security & storage configuration",
            "lfcs_title": "Week 6 Storage Mastery & LVM Drill",
            "lfcs_desc": "03:00 PM - 04:15 PM: Complete storage marathon: Partition disk, create LVM, format XFS, mount in /etc/fstab, expand online\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Configure NFS share and mount persistently from client VM\n05:30 PM - 06:00 PM: Milestone 6 Assessment: Storage integrity and LVM expansion"
        },

        # ==================== WEEK 7 ====================
        {
            "week": 7, "day_name": "Monday", "offset": 42,
            "cka_title": "Cluster & Pod Networking Prerequisites",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Network namespaces and veth pairs\n08:20 AM - 09:30 AM: Theory: Pod network CIDR, IPAM, CNI (Container Network Interface) plugins (Calico, Flannel, Weave)\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Prerequisite Switching, Routing, Gateways & CNI in Kubernetes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Inspecting CNI configuration files in /etc/cni/net.d/",
            "lfcs_title": "Linux Networking Configuration (IP & Routing)",
            "lfcs_desc": "03:00 PM - 03:20 PM: ip command speedrun (ip addr, ip link, ip route)\n03:20 PM - 04:20 PM: Theory: Static vs DHCP IP configuration, routing tables, default gateway, hostname resolution (/etc/hosts, /etc/resolv.conf)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure IPv4 & IPv6 Networking and Hostname Resolution\n05:35 PM - 06:00 PM: Synthesis: Configuring network interfaces via nmcli and ip commands"
        },
        {
            "week": 7, "day_name": "Tuesday", "offset": 43,
            "cka_title": "Service Networking & CoreDNS Deep Dive",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Service CIDR vs Pod CIDR separation\n08:20 AM - 09:30 AM: Theory: How kube-proxy intercepts service IPs, CoreDNS Corefile configuration, troubleshooting DNS lookup failures\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Service Networking & CoreDNS in Kubernetes\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Modifying CoreDNS configmap and watching resolution changes",
            "lfcs_title": "Network Bonding & Bridging",
            "lfcs_desc": "03:00 PM - 03:20 PM: Bonding modes recall (round-robin, active-backup, 802.3ad LACP)\n03:20 PM - 04:20 PM: Theory: Network device bonding for redundancy/throughput, Linux bridge devices for VM/container networks\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure Bridge and Bonding Devices\n05:35 PM - 06:00 PM: Synthesis: Creating a software bridge interface"
        },
        {
            "week": 7, "day_name": "Wednesday", "offset": 44,
            "cka_title": "Ingress Controllers & Routing Rules",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Ingress resource vs Ingress controller\n08:20 AM - 09:30 AM: Theory: Ingress rules (host-based, path-based), annotations, rewrite-target, default-backend\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: CKA Ingress Networking Labs 1 & 2\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Testing path rewriting on Nginx ingress controller",
            "lfcs_title": "Packet Filtering with Firewalld & Iptables",
            "lfcs_desc": "03:00 PM - 03:20 PM: firewall-cmd speedrun (--add-port, --permanent, --reload)\n03:20 PM - 04:20 PM: Theory: Netfilter architecture, firewalld zones, services, rich rules, basic iptables chains (INPUT, OUTPUT, FORWARD)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure Packet Filtering (Firewall)\n05:35 PM - 06:00 PM: Synthesis: Hardening server to allow only SSH and HTTPS"
        },
        {
            "week": 7, "day_name": "Thursday", "offset": 45,
            "cka_title": "Gateway API (2025 Updates)",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Gateway API role separation (GatewayClass, Gateway, HTTPRoute)\n08:20 AM - 09:30 AM: Theory: Gateway API architecture, comparing Ingress vs Gateway API, HTTPRoute routing matches\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Gateway API (2025 Updates)\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Configuring weighted routing between service versions via HTTPRoute",
            "lfcs_title": "NAT, Port Redirection & Reverse Proxies",
            "lfcs_desc": "03:00 PM - 03:20 PM: NAT terminology (SNAT, DNAT, Masquerading)\n03:20 PM - 04:20 PM: Theory: Port forwarding via firewall, configuring reverse proxy / load balancer (HAProxy/Nginx fundamentals)\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Port Redirection and NAT & Reverse Proxies\n05:35 PM - 06:00 PM: Synthesis: Port forwarding local port 8080 to internal backend port 80"
        },
        {
            "week": 7, "day_name": "Friday", "offset": 46,
            "cka_title": "Network Policies Deep Dive",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Default deny ingress and egress manifest structure\n08:20 AM - 09:30 AM: Theory: NetworkPolicy spec, podSelector, namespaceSelector, ipBlock CIDR exceptions, ports\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:15 AM: KodeKloud Labs: Network Policies Labs\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Visual Sketch: Drawing multi-namespace network policy isolation on whiteboard",
            "lfcs_title": "SSH Hardening, Key Auth & Time Sync",
            "lfcs_desc": "03:00 PM - 03:20 PM: ssh-keygen and ssh-copy-id speed drills\n03:20 PM - 04:20 PM: Theory: /etc/ssh/sshd_config hardening (Disable root login, password auth, custom port), chrony / timedatectl time sync\n04:20 PM - 04:35 PM: Walk break\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure SSH Servers/Clients & Time Servers\n05:35 PM - 06:00 PM: Synthesis: Setting up SSH key-based access with passphrase"
        },
        {
            "week": 7, "day_name": "Saturday", "offset": 47,
            "cka_title": "Week 7 Network Mastery Triathlon",
            "cka_desc": "08:00 AM - 09:30 AM: Deploy multi-service Ingress with TLS termination and Network Policy isolation\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: CNI crash troubleshooting and pod IP allocation recovery\n11:00 AM - 12:00 PM: Milestone 7 Assessment: Networking, Ingress & Security lockdown",
            "lfcs_title": "Week 7 Linux Networking & Firewall Marathon",
            "lfcs_desc": "03:00 PM - 04:15 PM: Build bridge network, configure static IP, set up firewalld port redirection and harden SSH\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Timed network troubleshooting (broken default route, DNS resolver failure)\n05:30 PM - 06:00 PM: Milestone 7 Assessment: Network configuration and firewall lockdown"
        },

        # ==================== WEEK 8 ====================
        {
            "week": 8, "day_name": "Monday", "offset": 49,
            "cka_title": "Troubleshooting: Control Plane & Applications",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Checking control plane logs in /var/log/pods and static pod manifests\n08:20 AM - 09:30 AM: Theory: Troubleshooting kube-apiserver crashloops, etcd connection loss, misconfigured kubelet ports\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Application Failure & Control Plane Failure Labs\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Intentionally corrupting kube-apiserver manifest and restoring service",
            "lfcs_title": "Containers & Virtual Machines on Linux",
            "lfcs_desc": "03:00 PM - 03:20 PM: Podman/Docker command speedrun (run, ps, images, exec)\n03:20 PM - 04:20 PM: Theory: Container isolation (namespaces & cgroups), KVM/QEMU, virsh CLI for VM management\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Create and Manage Containers & VMs\n05:35 PM - 06:00 PM: Synthesis: Deploying a containerized web server and binding ports"
        },
        {
            "week": 8, "day_name": "Tuesday", "offset": 50,
            "cka_title": "Troubleshooting: Worker Nodes & Network Failure",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Node NotReady diagnostic workflow (systemctl status kubelet, journalctl -u kubelet)\n08:20 AM - 09:30 AM: Theory: Kubelet certificates renewal, CNI plugin binary issues, CoreDNS crashes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Worker Node Failure & Network Troubleshooting Labs\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Speed Drill: Diagnosing and joining a detached worker node in under 5 minutes",
            "lfcs_title": "Timed Mock Exam 1 (Strict Exam Conditions)",
            "lfcs_desc": "03:00 PM - 03:10 PM: Terminal setup and mental grounding\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 1 (Strict timed conditions, no external help)\n04:25 PM - 04:45 PM: Walk break & cognitive decompression\n04:45 PM - 05:45 PM: Mock Exam 1 Error Analysis: Review mistakes and document in Error Ledger\n05:45 PM - 06:00 PM: Redo missed questions immediately"
        },
        {
            "week": 8, "day_name": "Wednesday", "offset": 51,
            "cka_title": "JSONPath Queries & Lightning Labs 1 & 2",
            "cka_desc": "08:00 AM - 08:20 AM: Retrieval: JSONPath syntax (-o jsonpath='{.items[*].metadata.name}')\n08:20 AM - 09:30 AM: Theory & Drills: Custom column formatting, range filtering, sorting by fields (--sort-by)\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: JSON Path in Kubernetes & Lightning Labs 1 & 2\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Speed review of Lightning Lab questions completed under target time",
            "lfcs_title": "Timed Mock Exam 2 (Strict Exam Conditions)",
            "lfcs_desc": "03:00 PM - 03:10 PM: Setup & deep breathing\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 2 (Strict timed conditions)\n04:25 PM - 04:45 PM: Movement & posture reset\n04:45 PM - 05:45 PM: Mock Exam 2 Error Analysis & deep dive on missed topics\n05:45 PM - 06:00 PM: Redo failed tasks from scratch"
        },
        {
            "week": 8, "day_name": "Thursday", "offset": 52,
            "cka_title": "Timed Mock Exam 1 & Step-by-Step Review",
            "cka_desc": "08:00 AM - 08:15 AM: Terminal environment prep (alias k=kubectl, export do, export now)\n08:15 AM - 10:15 AM: KodeKloud CKA Mock Exam 1 (Strict 2-hour timed exam simulation)\n10:15 AM - 10:30 AM: Physical walk & mental reset\n10:30 AM - 12:00 PM: Comprehensive Mock 1 Review: Analyze scoring, optimize slow commands",
            "lfcs_title": "Timed Mock Exam 3 (Strict Exam Conditions)",
            "lfcs_desc": "03:00 PM - 03:10 PM: Setup & focus\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 3 (Strict timed conditions)\n04:25 PM - 04:45 PM: Physical walk\n04:45 PM - 05:45 PM: Mock Exam 3 Error Analysis & command refinement\n05:45 PM - 06:00 PM: Redo missed questions"
        },
        {
            "week": 8, "day_name": "Friday", "offset": 53,
            "cka_title": "Timed Mock Exam 2 & 3 Marathon",
            "cka_desc": "08:00 AM - 08:15 AM: Terminal warm-up\n08:15 AM - 10:00 AM: KodeKloud CKA Mock Exam 2 & 3 high-weight scenario drills\n10:00 AM - 10:15 AM: Movement & eye rest\n10:15 AM - 11:30 AM: KodeKloud Ultimate Mock Exam challenges\n11:30 AM - 12:00 PM: Verify allowed documentation bookmarks on kubernetes.io/docs",
            "lfcs_title": "Timed Mock Exam 4 & Final Speed Marathon",
            "lfcs_desc": "03:00 PM - 03:10 PM: Final exam setup\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 4 (Strict timed conditions)\n04:25 PM - 04:45 PM: Walk break\n04:45 PM - 05:45 PM: 20-Question Rapid Linux Admin Scenario Sprint\n05:45 PM - 06:00 PM: Final Error Ledger consolidation"
        },
        {
            "week": 8, "day_name": "Saturday", "offset": 54,
            "cka_title": "Killer.sh Simulator Marathon (Exam Benchmark)",
            "cka_desc": "08:00 AM - 08:15 AM: Grounding, water, and full screen isolation\n08:15 AM - 10:15 AM: Killer.sh CKA Simulator Session (Strict 2-hour uninterrupted simulation)\n10:15 AM - 10:45 AM: Extended walk, fresh air, cognitive recovery\n10:45 AM - 12:00 PM: Killer.sh in-depth question review & explanation study (Target: score >= 80%)\nFinal Milestone Gate cleared!",
            "lfcs_title": "Certification Gate Review & Readiness Audit",
            "lfcs_desc": "03:00 PM - 04:30 PM: Comprehensive review of personal command cheat sheets (LVM, systemd, networking, permissions, regex)\n04:30 PM - 04:45 PM: Movement break\n04:45 PM - 06:00 PM: Final confidence check across all LFCS exam domains\nFinal Milestone Gate cleared!"
        },
    ]

    sundays = [
        {"week": 1, "offset": 6},
        # 2-week pause for family matters: Sep 21 - Oct 04 (offsets 7 to 20)
        {"week": 2, "offset": 27},
        {"week": 3, "offset": 34},
        {"week": 4, "offset": 41},
        {"week": 5, "offset": 48},
        {"week": 6, "offset": 55},
        {"week": 7, "offset": 62},
        {"week": 8, "offset": 69},
    ]

    pause_events = [
        {
            "offset": 7,
            "subject": "[PAUSE] Study Paused: Family Matters (Week 1 of 2)",
            "desc": "Study paused due to family matters.\nScheduled to resume on Monday, October 5, 2026 with Week 2."
        },
        {
            "offset": 14,
            "subject": "[PAUSE] Study Paused: Family Matters (Week 2 of 2)",
            "desc": "Study paused due to family matters.\nResumes Monday, October 5, 2026 with Week 2 (ReplicaSets & Self-Healing Controllers)."
        }
    ]

    events = []
    
    # Pause events for the 2-week break
    for p in pause_events:
        p_date = start_monday + timedelta(days=p["offset"])
        date_str = p_date.strftime("%Y%m%d")
        csv_date_str = p_date.strftime("%m/%d/%Y")
        events.append({
            "uid": f"pause-d{p['offset']}@{date_str}",
            "subject": p["subject"],
            "start_dt": f"{date_str}T080000",
            "end_dt": f"{date_str}T180000",
            "csv_date": csv_date_str,
            "csv_start": "08:00 AM",
            "csv_end": "06:00 PM",
            "desc": p["desc"],
            "type": "REST"
        })

    for day in days_curriculum:
        # Week 1 stays at offset 0-5. Weeks 2-8 are pushed by 14 days (2 weeks).
        actual_offset = day["offset"] if day["week"] == 1 else (day["offset"] + 14)
        event_date = start_monday + timedelta(days=actual_offset)
        date_str = event_date.strftime("%Y%m%d")
        csv_date_str = event_date.strftime("%m/%d/%Y")

        # CKA Event: 8:00 AM to 12:00 PM
        events.append({
            "uid": f"cka-w{day['week']}d{actual_offset}@{date_str}",
            "subject": f"[CKA] 8am-12pm: {day['cka_title']}",
            "start_dt": f"{date_str}T080000",
            "end_dt": f"{date_str}T120000",
            "csv_date": csv_date_str,
            "csv_start": "08:00 AM",
            "csv_end": "12:00 PM",
            "desc": f"CKA STUDY BLOCK (8:00 AM - 12:00 PM)\nTopic: {day['cka_title']}\n\nSchedule:\n{day['cka_desc']}",
            "type": "CKA"
        })

        # Midday Recovery Event: 12:00 PM to 3:00 PM
        events.append({
            "uid": f"recovery-w{day['week']}d{actual_offset}@{date_str}",
            "subject": "[RECOVERY] 12pm-3pm: Cognitive Reset & Physical Regeneration",
            "start_dt": f"{date_str}T120000",
            "end_dt": f"{date_str}T150000",
            "csv_date": csv_date_str,
            "csv_start": "12:00 PM",
            "csv_end": "03:00 PM",
            "desc": "COGNITIVE RECOVERY & INTEGRATION (12:00 PM - 3:00 PM)\n12:00 PM - 01:00 PM: Nutritious lunch & total screen detachment\n01:00 PM - 02:00 PM: Aerobic exercise / brisk walk outside (BDNF boost)\n02:00 PM - 02:45 PM: Power nap or Non-Sleep Deep Rest (NSDR)\n02:45 PM - 03:00 PM: Terminal & desk prep for LFCS",
            "type": "RECOVERY"
        })

        # LFCS Event: strictly 3:00 PM to 6:00 PM
        events.append({
            "uid": f"lfcs-w{day['week']}d{actual_offset}@{date_str}",
            "subject": f"[LFCS] 3pm-6pm: {day['lfcs_title']}",
            "start_dt": f"{date_str}T150000",
            "end_dt": f"{date_str}T180000",
            "csv_date": csv_date_str,
            "csv_start": "03:00 PM",
            "csv_end": "06:00 PM",
            "desc": f"LFCS STUDY BLOCK (3:00 PM - 6:00 PM)\nTopic: {day['lfcs_title']}\n\nSchedule:\n{day['lfcs_desc']}",
            "type": "LFCS"
        })

    for sun in sundays:
        sun_date = start_monday + timedelta(days=sun["offset"])
        date_str = sun_date.strftime("%Y%m%d")
        csv_date_str = sun_date.strftime("%m/%d/%Y")

        label = "Exam Ready! Full Rest & Mental Grounding" if sun['week'] == 8 else f"Full Recovery & Memory Consolidation (Week {sun['week']})"
        events.append({
            "uid": f"rest-w{sun['week']}@{date_str}",
            "subject": f"[REST] {label}",
            "start_dt": f"{date_str}T080000",
            "end_dt": f"{date_str}T180000",
            "csv_date": csv_date_str,
            "csv_start": "08:00 AM",
            "csv_end": "06:00 PM",
            "desc": "Complete detachment from code and terminal.\nEngage in physical movement, outdoor activities, social time, and restorative sleep.\nAllows long-term synaptic consolidation of weekly concepts.",
            "type": "REST"
        })

    return events

def generate_ics(events, output_path="cka_lfcs_schedule.ics"):
    # Note: Omit X-WR-TIMEZONE so Google Calendar imports floating local times directly into the user's timezone!
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Antigravity AI//CKA LFCS 8-Week Architecture//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:CKA & LFCS 8-Week Dual Certification Track"
    ]
    
    now_stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    for ev in events:
        lines.append("BEGIN:VEVENT")
        lines.append(f"UID:{ev['uid']}")
        lines.append(f"DTSTAMP:{now_stamp}")
        lines.append(f"DTSTART:{ev['start_dt']}")
        lines.append(f"DTEND:{ev['end_dt']}")
        lines.append(f"SUMMARY:{ev['subject']}")
        
        escaped_desc = ev['desc'].replace("\n", "\\n")
        lines.append(f"DESCRIPTION:{escaped_desc}")
        lines.append("STATUS:CONFIRMED")
        lines.append("TRANSP:OPAQUE")
        lines.append("END:VEVENT")
        
    lines.append("END:VCALENDAR")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\r\n".join(lines) + "\r\n")
    print(f"Generated 8-Week iCalendar: {output_path}")

def generate_csv(events, output_path="cka_lfcs_schedule.csv"):
    headers = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]
    rows = [",".join(headers)]
    
    for ev in events:
        safe_desc = '"' + ev['desc'].replace('"', '""') + '"'
        safe_subject = '"' + ev['subject'].replace('"', '""') + '"'
        row = f"{safe_subject},{ev['csv_date']},{ev['csv_start']},{ev['csv_date']},{ev['csv_end']},False,{safe_desc},,False"
        rows.append(row)
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(rows) + "\n")
    print(f"Generated 8-Week Google Calendar CSV: {output_path}")

if __name__ == "__main__":
    start_date = sys.argv[1] if len(sys.argv) > 1 else "2026-09-14"
    print(f"Building 8-Week schedule starting Monday: {start_date}")
    evs = build_8week_events(start_date)
    generate_ics(evs, "cka_lfcs_schedule.ics")
    generate_csv(evs, "cka_lfcs_schedule.csv")
