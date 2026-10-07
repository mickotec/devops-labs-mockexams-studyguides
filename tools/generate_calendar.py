#!/usr/bin/env python3
"""
CKA & LFCS Study Calendar & Schedule Generator
Interactively customizes the study calendar based on:
 1. When the learner wants to start studying (Start Date)
 2. Study duration / pacing (8-Week Standard, 4-Week Intensive Sprint, or Custom)
 3. Target certification track (Both Dual-Track, CKA Only, or LFCS Only)
 4. Optional pause / recovery weeks

Outputs synchronized RFC 5545 iCalendar (.ics) and Google Calendar (.csv) files.
"""

import sys
import os
import re
import argparse
from pathlib import Path
from datetime import datetime, timedelta, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent

# ── 8-Week Standard Curriculum (48 Days) ──────────────────────────────────
DAYS_CURRICULUM_8WEEK = [
    # Week 1
    {"week": 1, "day_name": "Monday", "offset": 0,
     "cka_title": "Kubernetes Architecture & Container Runtimes",
     "cka_desc": "08:00 AM - 08:20 AM: Warm-up: Sketch Kubernetes control plane components from memory\n08:20 AM - 09:30 AM: Theory: API Server, Controller Manager, Scheduler, Kubelet, Kube-proxy, ContainerD vs Docker\n09:30 AM - 09:45 AM: Movement & Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Explore cluster components & ContainerD\n11:15 AM - 11:30 AM: Eye rest & mobility\n11:30 AM - 12:00 PM: Exploratory: Inspect running static pod manifests in /etc/kubernetes/manifests",
     "lfcs_title": "Consoles, Navigation & System Documentation",
     "lfcs_desc": "03:00 PM - 03:20 PM: Terminal navigation speed drills (cd, pushd, popd, ls flags)\n03:20 PM - 04:20 PM: Theory: Graphical vs text consoles, man pages (sections 1, 5, 8), info, --help\n04:20 PM - 04:35 PM: Walk & cognitive reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Logging in and System Documentation\n05:35 PM - 06:00 PM: Cheat sheet update: Documentation lookup recipes"},
    {"week": 1, "day_name": "Tuesday", "offset": 1,
     "cka_title": "ETCD Fundamentals & Cluster State Store",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Role of ETCD in consensus and high availability\n08:20 AM - 09:30 AM: Theory: Key-value store, Raft protocol overview, etcd in Kubernetes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: etcd for Beginners & etcd in Kubernetes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Querying etcd endpoint health and members",
     "lfcs_title": "Files, Directories, Hard & Soft Links",
     "lfcs_desc": "03:00 PM - 03:20 PM: File operation warm-up (mkdir -p, cp -r, rm -rf safety)\n03:20 PM - 04:20 PM: Theory: Inodes, hard links vs symbolic links (ln vs ln -s), link limits across filesystems\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Files, Directories, Hard and Soft Links\n05:35 PM - 06:00 PM: Synthesis: Inode verification drills with ls -i"},
    {"week": 1, "day_name": "Wednesday", "offset": 2,
     "cka_title": "Pod Internals & YAML Architecture",
     "cka_desc": "08:00 AM - 08:20 AM: Speed drill: Write a complete Pod YAML from memory\n08:20 AM - 09:30 AM: Theory: Pod specification, containers, ports, environment, volumes layout\n09:30 AM - 09:45 AM: Hydration & stretching\n09:45 AM - 11:15 AM: KodeKloud Labs: Pods & Pods with YAML\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Break YAML indentation and observe kubectl error parsers",
     "lfcs_title": "Standard Linux File Permissions",
     "lfcs_desc": "03:00 PM - 03:20 PM: Octal permission conversion warm-up (rwx calculations)\n03:20 PM - 04:20 PM: Theory: Owner, group, other (ugo), chmod (numeric vs symbolic), chown, chgrp, umask\n04:20 PM - 04:35 PM: Physical reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Standard File Permissions\n05:35 PM - 06:00 PM: Synthesis: Default umask calculation drills"},
    {"week": 1, "day_name": "Thursday", "offset": 3,
     "cka_title": "Multi-Container Pod Patterns & Init Containers",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Pod shared network and IPC namespaces\n08:20 AM - 09:30 AM: Theory: Sidecar, adapter, and ambassador design patterns; initContainers order of execution\n09:30 AM - 09:45 AM: Movement & posture check\n09:45 AM - 11:15 AM: KodeKloud Labs: Multi-Container Pods & Init Containers\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Shared volume logging sidecar demo",
     "lfcs_title": "Special Permissions: SUID, SGID & Sticky Bit",
     "lfcs_desc": "03:00 PM - 03:20 PM: Permission bit calculation drills (4000, 2000, 1000)\n03:20 PM - 04:20 PM: Theory: SUID execution as owner, SGID for shared directories, Sticky bit on /tmp\n04:20 PM - 04:35 PM: Walk break\n04:35 PM - 05:35 PM: KodeKloud Labs: SUID, SGID, and Sticky Bit\n05:35 PM - 06:00 PM: Command ledger update: find / -perm /4000 drills"},
    {"week": 1, "day_name": "Friday", "offset": 4,
     "cka_title": "Fast Imperative CLI Mastery with Kubectl",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Fast imperative command generator syntax\n08:20 AM - 09:30 AM: Theory: Imperative vs declarative, kubectl run, create, expose, --dry-run=client -o yaml\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Imperative Commands with Kubectl\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Speed Synthesis: Set up ~/.bashrc aliases (k, do, now) and vimrc tabstop settings",
     "lfcs_title": "Pagers, Vim Mastery & Terminal Editing",
     "lfcs_desc": "03:00 PM - 03:20 PM: Vim navigation warm-up (hjkl, w, b, gg, G, 0, $)\n03:20 PM - 04:20 PM: Theory: Vim command vs insert mode, visual selection, yanking, search/replace (:s/old/new/g)\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Pagers and VI\n05:35 PM - 06:00 PM: Error Ledger review & personal ~/.vimrc configuration"},
    {"week": 1, "day_name": "Saturday", "offset": 5,
     "cka_title": "Week 1 Integration & Speedrun Drill",
     "cka_desc": "08:00 AM - 09:30 AM: Review Week 1 error notes and YAML structures\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:00 AM: Speed Drill: Generate 20 different Pod manifests without documentation in 20 min\n11:00 AM - 12:00 PM: Milestone Assessment 1: Pod deployment and multi-container debugging",
     "lfcs_title": "Week 1 Consolidation & Permission Auditing",
     "lfcs_desc": "03:00 PM - 04:15 PM: Permissions speed drill: Audit and enforce correct SUID/SGID/Sticky bits across a mock directory tree\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: VimGolf / openvim speed challenge\n05:30 PM - 06:00 PM: Milestone Assessment 1: System permissions verification"},

    # Week 2
    {"week": 2, "day_name": "Monday", "offset": 6,
     "cka_title": "ReplicaSets & Self-Healing Controllers",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: ReplicaSet matchLabels vs Pod template labels\n08:20 AM - 09:30 AM: Theory: Controller manager loops, desired vs current state, scaling ReplicaSets\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: ReplicaSets\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Deleting pods to witness reconciliation loop in real time",
     "lfcs_title": "File Searching with Find and Locate",
     "lfcs_desc": "03:00 PM - 03:20 PM: find command warm-up (-name, -type f, -type d)\n03:20 PM - 04:20 PM: Theory: find expressions (-size, -mtime, -user, -perm), -exec vs xargs, locate vs updatedb\n04:20 PM - 04:35 PM: Walk & mental reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Search for Files\n05:35 PM - 06:00 PM: Synthesis: Complex find -exec chmod/rm one-liners"},
    {"week": 2, "day_name": "Tuesday", "offset": 7,
     "cka_title": "Deployments, Rollouts & Revisions",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Deployment vs ReplicaSet relationship\n08:20 AM - 09:30 AM: Theory: RollingUpdate strategy, maxSurge, maxUnavailable, rollout status, rollout history\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Deployments & Rollout Updates\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Rollout undo to a specific previous revision (--to-revision)",
     "lfcs_title": "Text Processing: Grep & Regular Expressions",
     "lfcs_desc": "03:00 PM - 03:20 PM: Regex anchors drill (^, $, .)\n03:20 PM - 04:20 PM: Theory: grep flags (-i, -v, -r, -n, -E), Basic Regular Expressions (BRE) vs Extended (ERE)\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Search File Using Grep & Regex\n05:35 PM - 06:00 PM: Cheat sheet update: High-yield regex pattern catalog"},
    {"week": 2, "day_name": "Wednesday", "offset": 8,
     "cka_title": "Services: ClusterIP, NodePort & LoadBalancer",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Service targetPort vs port vs nodePort\n08:20 AM - 09:30 AM: Theory: kube-proxy IPTables/IPVS modes, Endpoints, headless services, service discovery\n09:30 AM - 09:45 AM: Hydration & stretch\n09:45 AM - 11:15 AM: KodeKloud Labs: Services (ClusterIP & NodePort)\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Inspecting cluster iptables rules generated for a Service",
     "lfcs_title": "Advanced Stream Analysis: Sed & Awk Fundamentals",
     "lfcs_desc": "03:00 PM - 03:20 PM: Piping warm-up (cat, cut, sort, uniq -c)\n03:20 PM - 04:20 PM: Theory: sed line replacement (sed 's/foo/bar/g'), awk column extraction (awk '{print $1, $3}')\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: Practical Terminal Drills: Parse /etc/passwd and /etc/group using awk and sed\n05:35 PM - 06:00 PM: Synthesis: Formatting system metrics with awk"},
    {"week": 2, "day_name": "Thursday", "offset": 9,
     "cka_title": "Namespaces & DNS Resolution Inside Clusters",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: FQDN structure (svc.cluster.local)\n08:20 AM - 09:30 AM: Theory: Namespace isolation, CoreDNS resolution, cross-namespace service communication\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Namespaces & CoreDNS Exploration\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Launch temporary busybox pod for nslookup and curl tests",
     "lfcs_title": "I/O Redirection & Stream Multiplexing",
     "lfcs_desc": "03:00 PM - 03:20 PM: Redirection warm-up (stdout, stderr, &>)\n03:20 PM - 04:20 PM: Theory: File descriptors (0, 1, 2), redirecting stderr (2>), appending (>>), pipelines (|), tee\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Use Input-Output Redirection\n05:35 PM - 06:00 PM: Terminal drill: Redirecting output and errors to separate log files"},
    {"week": 2, "day_name": "Friday", "offset": 10,
     "cka_title": "Kubectl Explain & Declarative Workflow",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Fast navigation using kubectl explain --recursive\n08:20 AM - 09:30 AM: Theory: kubectl apply algorithm, last-applied-configuration annotation, manifest management\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Kubectl Apply Command & Imperative vs Declarative\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Synthesis: Constructing a complete 3-tier app manifest declaratively",
     "lfcs_title": "Archiving, Compression & Remote Backups",
     "lfcs_desc": "03:00 PM - 03:20 PM: Tar flags drill (-czvf, -xzvf, -cjvf, -xpvf)\n03:20 PM - 04:20 PM: Theory: tar, gzip, bzip2, xz compression ratios, preserving permissions (-p), rsync basics\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Archive, Back Up, Compress, Unpack\n05:35 PM - 06:00 PM: Synthesis: Automated incremental tar backup script"},
    {"week": 2, "day_name": "Saturday", "offset": 11,
     "cka_title": "Week 2 Speed Drills & Controller Triathlon",
     "cka_desc": "08:00 AM - 09:30 AM: Speed drill: Build Pod + Deployment + Service in under 7 minutes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Rolling update failure scenario & rollback under pressure\n11:00 AM - 12:00 PM: Milestone 2 Assessment: Multi-tier deployment with namespace routing",
     "lfcs_title": "Week 2 Speed Drills & Git Version Control",
     "lfcs_desc": "03:00 PM - 04:15 PM: Git operations: init, stage, commit, branch, merge, diff, remote tracking\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Fast text stream filtering marathon (parse 10,000 log lines with grep/sed/awk)\n05:30 PM - 06:00 PM: Milestone 2 Assessment: Text processing & archive verification"},

    # Week 3
    {"week": 3, "day_name": "Monday", "offset": 12,
     "cka_title": "Manual Scheduling, Labels & Selectors",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: nodeName attribute in Pod spec\n08:20 AM - 09:30 AM: Theory: Scheduler bypass via nodeName, label management, matchExpressions vs matchLabels\n09:30 AM - 09:45 AM: Movement break\n09:45 AM - 11:15 AM: KodeKloud Labs: Manual Scheduling, Labels and Selectors\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Manually binding an unscheduled pod via binding API",
     "lfcs_title": "Linux Boot Architecture & GRUB2",
     "lfcs_desc": "03:00 PM - 03:20 PM: Boot sequence recall (BIOS/UEFI -> MBR/GPT -> GRUB2 -> Kernel -> Init)\n03:20 PM - 04:20 PM: Theory: GRUB2 configuration (/etc/default/grub, grub2-mkconfig), kernel parameters at boot\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Boot, Reboot, and Shutdown a System Safely\n05:35 PM - 06:00 PM: Synthesis: Interrupting boot to access emergency/rescue target"},
    {"week": 3, "day_name": "Tuesday", "offset": 13,
     "cka_title": "Taints, Tolerations & Node Affinity",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Taints repel pods, Affinity attracts pods\n08:20 AM - 09:30 AM: Theory: Taint effects (NoSchedule, PreferNoSchedule, NoExecute), nodeAffinity (required vs preferred)\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Taints & Tolerations, Node Affinity\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Evicting running pods using NoExecute taints",
     "lfcs_title": "Systemd Targets & Runlevel Management",
     "lfcs_desc": "03:00 PM - 03:20 PM: Runlevel to systemd target mapping drills (3=multi-user, 5=graphical)\n03:20 PM - 04:20 PM: Theory: systemctl get-default, set-default, isolate, emergency.target vs rescue.target\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Boot or Change System Into Different Operating Modes\n05:35 PM - 06:00 PM: Summary notes & recovery workflows"},
    {"week": 3, "day_name": "Wednesday", "offset": 14,
     "cka_title": "Resource Requirements, Limits & LimitRanges",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: CPU millis (1000m = 1 core) and Memory mebibytes (Mi vs MB)\n08:20 AM - 09:30 AM: Theory: Requests vs limits, OOMKilled status (Exit code 137), CPU throttling, LimitRanges\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Resource Requirements & Limits\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Simulating memory leak pod to witness OOMKilled",
     "lfcs_title": "Creating & Managing Systemd Services",
     "lfcs_desc": "03:00 PM - 03:20 PM: systemctl status/start/stop/restart/reload warm-up\n03:20 PM - 04:20 PM: Theory: Unit file layout (/etc/systemd/system/), [Unit], [Service] (ExecStart, Restart), [Install]\n04:20 PM - 04:35 PM: Walk & posture check\n04:35 PM - 05:35 PM: KodeKloud Labs: Create systemd Services\n05:35 PM - 06:00 PM: Synthesis: Write a custom Python/Bash background service from scratch"},
    {"week": 3, "day_name": "Thursday", "offset": 15,
     "cka_title": "DaemonSets & Static Pods Architecture",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Where are control plane static pod manifests stored?\n08:20 AM - 09:30 AM: Theory: DaemonSets scheduling, static pods managed directly by kubelet, /etc/kubernetes/manifests\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: DaemonSets & Static Pods\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Deploying custom static pod on worker node and verifying node name suffix",
     "lfcs_title": "Process Diagnostics & Signal Management",
     "lfcs_desc": "03:00 PM - 03:20 PM: ps aux / pgrep warm-up\n03:20 PM - 04:20 PM: Theory: Process states (R, S, D, Z), signals (SIGTERM 15, SIGKILL 9, SIGHUP 1), nice & renice\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Diagnose and Manage Processes\n05:35 PM - 06:00 PM: Synthesis: Killing runaway processes and identifying zombie processes"},
    {"week": 3, "day_name": "Friday", "offset": 16,
     "cka_title": "Priority Classes & Multiple Schedulers",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: PriorityClass value ranges and preemption policy\n08:20 AM - 09:30 AM: Theory: PriorityClass, Pod preemption, deploying a secondary custom kube-scheduler\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:15 AM: KodeKloud Labs: Priority Classes & Multiple Schedulers\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Assigning pods to custom scheduler via schedulerName",
     "lfcs_title": "System Integrity, Resource Monitoring & Top",
     "lfcs_desc": "03:00 PM - 03:20 PM: top / htop interactive shortcut drills (P, M, k, r)\n03:20 PM - 04:20 PM: Theory: System load averages (1, 5, 15 min), uptime, free -m, vmstat, iostat, lsof\n04:20 PM - 04:35 PM: Physical walk\n04:35 PM - 05:35 PM: KodeKloud Labs: Verify Integrity and Availability of Resources and Processes\n05:35 PM - 06:00 PM: Error Ledger analysis"},
    {"week": 3, "day_name": "Saturday", "offset": 17,
     "cka_title": "Week 3 Scheduling Troubleshooting Matrix",
     "cka_desc": "08:00 AM - 09:30 AM: Debugging 10 pods stuck in Pending state (Taints, Affinities, Resources, NodeSelector)\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Static pod troubleshooting (broken manifest path in kubelet config)\n11:00 AM - 12:00 PM: Milestone 3 Assessment: Advanced scheduling orchestration",
     "lfcs_title": "Week 3 Systemd & Process Orchestration",
     "lfcs_desc": "03:00 PM - 04:15 PM: Build custom systemd service with automated restart on failure and log output\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Process troubleshooting under memory/CPU stress (stress/stress-ng drills)\n05:30 PM - 06:00 PM: Milestone 3 Assessment: Service & process resilience"},

    # Week 4
    {"week": 4, "day_name": "Monday", "offset": 18,
     "cka_title": "Commands & Arguments (Docker vs Kubernetes)",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: ENTRYPOINT = command, CMD = args mapping\n08:20 AM - 09:30 AM: Theory: Overriding container entrypoint/cmd, passing environment variables\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Commands and Arguments in Kubernetes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Sleeping pods for debugging using command override",
     "lfcs_title": "Journald & System Log File Analysis",
     "lfcs_desc": "03:00 PM - 03:20 PM: journalctl flag speedrun (-u, -f, -p err, --since)\n03:20 PM - 04:20 PM: Theory: Systemd journal storage (volatile vs persistent /var/log/journal), rsyslog, /var/log/auth.log\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Locate and Analyze System Log Files\n05:35 PM - 06:00 PM: Synthesis: Log auditing with journalctl and logrotate review"},
    {"week": 4, "day_name": "Tuesday", "offset": 19,
     "cka_title": "ConfigMaps & Application Configuration",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Creating ConfigMap from literal vs from file\n08:20 AM - 09:30 AM: Theory: ConfigMaps as environment variables (env, envFrom) and as mounted volume files\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Configuring ConfigMaps in Applications\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Hot-reloading application configuration from volume mounts",
     "lfcs_title": "Task Scheduling with Cron and At",
     "lfcs_desc": "03:00 PM - 03:20 PM: Cron 5-field syntax drill (minute, hour, day, month, weekday)\n03:20 PM - 04:20 PM: Theory: crontab -e, crontab -l, /etc/crontab, /etc/cron.*, at, atq, atrm, batch\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Schedule Tasks to Run at a Set Date and Time\n05:35 PM - 06:00 PM: Synthesis: Setting up automated disk monitoring cron job"},
    {"week": 4, "day_name": "Wednesday", "offset": 20,
     "cka_title": "Secrets Management & Encryption at Rest",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Base64 encoding vs encryption (echo -n ... | base64)\n08:20 AM - 09:30 AM: Theory: Generic, docker-registry, tls secrets; configuring EncryptionConfiguration on kube-apiserver\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Secrets & Encrypting Secret Data at Rest\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Verifying encrypted data directly inside etcd database",
     "lfcs_title": "Package Managers (APT, DNF/YUM & RPM)",
     "lfcs_desc": "03:00 PM - 03:20 PM: Package manager command comparison drills\n03:20 PM - 04:20 PM: Theory: apt update/install/purge, dpkg -i/-l, dnf/yum install/remove, rpm -ivh/-qa, repo configs\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage Software with Package Manager & Repositories\n05:35 PM - 06:00 PM: Synthesis: Adding third-party repository and verifying GPG keys"},
    {"week": 4, "day_name": "Thursday", "offset": 21,
     "cka_title": "Autoscaling: HPA, VPA & In-Place Pod Resize",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Metrics-server installation verification (kubectl top)\n08:20 AM - 09:30 AM: Theory: Horizontal Pod Autoscaler (HPA v2), Vertical Pod Autoscaler (VPA), In-place resize (2025)\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: HPA, VPA & Modifying CPU Resources in VPA\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Generating CPU load to trigger HPA pod scaling",
     "lfcs_title": "Compiling Software from Source Code",
     "lfcs_desc": "03:00 PM - 03:20 PM: Tar extraction & build tools warm-up (gcc, make)\n03:20 PM - 04:20 PM: Theory: ./configure flags (--prefix), make compilation, make install, managing shared libraries (ldconfig)\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Install Software by Compiling Source Code\n05:35 PM - 06:00 PM: Synthesis: Custom compile and install of a utility tool"},
    {"week": 4, "day_name": "Friday", "offset": 22,
     "cka_title": "Admission Controllers & Validating Webhooks",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Kubernetes API request pipeline (Authn -> Authz -> Admission)\n08:20 AM - 09:30 AM: Theory: Built-in controllers (NamespaceLifecycle, LimitRanger), Mutating vs Validating webhooks\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Admission Controllers & Validating/Mutating Webhooks\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Enabling and disabling admission plugins in kube-apiserver manifest",
     "lfcs_title": "Bash Automation & Maintenance Scripting",
     "lfcs_desc": "03:00 PM - 03:20 PM: Bash syntax warm-up (variables, conditionals [ ], exit codes $?)\n03:20 PM - 04:20 PM: Theory: Positional parameters ($1, $@), loops (for, while), functions, error handling (set -e)\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: Practical Scripting Lab: Write an automated log rotation and cleanup maintenance script\n05:35 PM - 06:00 PM: Script review and execution"},
    {"week": 4, "day_name": "Saturday", "offset": 23,
     "cka_title": "Week 4 App Lifecycle & Secret Security Drill",
     "cka_desc": "08:00 AM - 09:30 AM: Timed deployment with ConfigMap, Secret, encrypted at rest, and HPA autoscaling\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Debugging Secret decoding and environment injection errors\n11:00 AM - 12:00 PM: Milestone 4 Assessment: Application Lifecycle Mastery",
     "lfcs_title": "Week 4 System Automation & Maintenance Triathlon",
     "lfcs_desc": "03:00 PM - 04:15 PM: Automate system backup and log cleanup using custom cron and bash script\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Package troubleshooting and repository recovery drill\n05:30 PM - 06:00 PM: Milestone 4 Assessment: Scripting and service automation"},

    # Week 5
    {"week": 5, "day_name": "Monday", "offset": 24,
     "cka_title": "Node Maintenance: Cordon, Drain & Uncordon",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: cordon vs drain vs drain --ignore-daemonsets\n08:20 AM - 09:30 AM: Theory: Safe workload eviction, PodDisruptionBudgets (PDB), node scheduling states\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: OS Upgrades & Maintenance\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Evicting pods respecting PDB minAvailable / maxUnavailable",
     "lfcs_title": "Local User Management & /etc/passwd",
     "lfcs_desc": "03:00 PM - 03:20 PM: useradd / usermod flag drills (-u, -g, -G, -d, -s)\n03:20 PM - 04:20 PM: Theory: User IDs, system users vs regular users, /etc/passwd fields, /etc/shadow fields, userdel\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Create, Delete, and Modify Local User Accounts\n05:35 PM - 06:00 PM: Synthesis: User account expiration and password policy enforcement (chage)"},
    {"week": 5, "day_name": "Tuesday", "offset": 25,
     "cka_title": "Cluster Upgrade: Kubeadm Control Plane",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Kubernetes version skew policy rules\n08:20 AM - 09:30 AM: Theory: kubeadm upgrade plan, upgrading kubeadm, kubelet, kubectl on primary master\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Cluster Upgrade Process - Control Plane\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Verifying control plane component versions after upgrade",
     "lfcs_title": "Groups, Sudo Privileges & Visudo",
     "lfcs_desc": "03:00 PM - 03:20 PM: groupadd / groupmod drills\n03:20 PM - 04:20 PM: Theory: /etc/group, group passwords, /etc/sudoers format (User Host=(Runas) Commands), visudo safety\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Groups & Sudo Privileges\n05:35 PM - 06:00 PM: Synthesis: Granting passwordless sudo to specific administrative commands"},
    {"week": 5, "day_name": "Wednesday", "offset": 26,
     "cka_title": "Cluster Upgrade: Worker Nodes",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Steps on worker node: drain -> upgrade kubeadm -> upgrade kubelet -> uncordon\n08:20 AM - 09:30 AM: Theory: Safe worker node rollouts without downtime, daemonset pod handling\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Cluster Upgrade Process - Worker Nodes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Speed Drill: Upgrading worker node in under 6 minutes",
     "lfcs_title": "Profiles, Template Environments & User Limits",
     "lfcs_desc": "03:00 PM - 03:20 PM: Login vs non-login shell startup file drills\n03:20 PM - 04:20 PM: Theory: /etc/profile, /etc/bashrc, ~/.bash_profile, /etc/skel skeleton files, /etc/security/limits.conf\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage Profiles & User Resource Limits\n05:35 PM - 06:00 PM: Synthesis: Restricting max user processes (nproc) and open files (nofile)"},
    {"week": 5, "day_name": "Thursday", "offset": 27,
     "cka_title": "ETCD Snapshot Backup & Disaster Recovery",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Mandatory ETCDCTL environment variables and flags\n08:20 AM - 09:30 AM: Theory: ETCDCTL_API=3 snapshot save, snapshot restore, swapping data-dir in static pod manifest\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Backup and Restore Methods (ETCD)\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Speed Drill: Timed ETCD backup and complete cluster recovery from snapshot",
     "lfcs_title": "Kernel Runtime Tuning with Sysctl",
     "lfcs_desc": "03:00 PM - 03:20 PM: sysctl inspection drills (sysctl -a | grep ip_forward)\n03:20 PM - 04:20 PM: Theory: /proc/sys filesystem, ephemeral tuning (sysctl -w), persistent configuration (/etc/sysctl.conf)\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Change Kernel Runtime Parameters\n05:35 PM - 06:00 PM: Synthesis: Enabling IP forwarding and adjusting virtual memory swappiness"},
    {"week": 5, "day_name": "Friday", "offset": 28,
     "cka_title": "TLS Basics & PKI in Kubernetes",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Symmetric vs asymmetric encryption and certificate chains\n08:20 AM - 09:30 AM: Theory: Kubernetes CA, server certs, client certs, inspecting certificate details with openssl\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: TLS Basics & View Certificate Details\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Diagnosing expired certificate errors on kube-apiserver",
     "lfcs_title": "Mandatory Access Control: SELinux & AppArmor",
     "lfcs_desc": "03:00 PM - 03:20 PM: SELinux mode check (getenforce, sestatus)\n03:20 PM - 04:20 PM: Theory: DAC vs MAC, SELinux contexts (user:role:type:level), semanage, restorecon, chcon, /etc/selinux/config\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: SELinux Contexts & Policy Enforcement\n05:35 PM - 06:00 PM: Error Ledger review: SELinux denial analysis (ausearch, audit2why)"},
    {"week": 5, "day_name": "Saturday", "offset": 29,
     "cka_title": "Full Disaster Recovery & Upgrade Drill",
     "cka_desc": "08:00 AM - 09:30 AM: Disaster Simulation: Control plane crash + etcd snapshot restore under 15 minutes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Full multi-node kubeadm upgrade across 3 nodes\n11:00 AM - 12:00 PM: Milestone 5 Assessment: Disaster recovery & cluster maintenance",
     "lfcs_title": "Security Audit, User Quarantine & Recovery",
     "lfcs_desc": "03:00 PM - 04:15 PM: Lock down compromised user accounts, audit root privileges, repair corrupted sudoers file\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Troubleshoot and fix web server blocked by SELinux context\n05:30 PM - 06:00 PM: Milestone 5 Assessment: Security & access audit verification"},

    # Week 6
    {"week": 6, "day_name": "Monday", "offset": 30,
     "cka_title": "Certificates API & KubeConfig Management",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: CertificateSigningRequest (CSR) manifest structure\n08:20 AM - 09:30 AM: Theory: CSR approval workflow (kubectl certificate approve), Kubeconfig clusters, users, contexts\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Certificates API & KubeConfig\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Generating custom user kubeconfig with client certs and key",
     "lfcs_title": "Storage Partitions (MBR vs GPT) & Swap",
     "lfcs_desc": "03:00 PM - 03:20 PM: Storage listing drills (lsblk, blkid, fdisk -l)\n03:20 PM - 04:20 PM: Theory: MBR vs GPT partition tables, fdisk, gdisk, parted, creating and activating swap (mkswap, swapon)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage Partitions and Swap Space\n05:35 PM - 06:00 PM: Synthesis: Permanent swap configuration in /etc/fstab"},
    {"week": 6, "day_name": "Tuesday", "offset": 31,
     "cka_title": "RBAC (Roles, RoleBindings & ClusterRoles)",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Role vs ClusterRole scope\n08:20 AM - 09:30 AM: Theory: apiGroups, resources, verbs, subjects, RoleBindings, ClusterRoleBindings, kubectl auth can-i\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Role-Based Access Controls & Cluster Roles\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Testing developer permissions via --as=developer flag",
     "lfcs_title": "Filesystems & Boot Mounting (/etc/fstab)",
     "lfcs_desc": "03:00 PM - 03:20 PM: Filesystem creation commands (mkfs.ext4, mkfs.xfs)\n03:20 PM - 04:20 PM: Theory: Ext4 vs XFS features, mount options (ro, rw, noexec, nodev), /etc/fstab 6-field layout, UUID mounting\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Create Filesystems and Mount Them at Boot\n05:35 PM - 06:00 PM: Synthesis: Safe mounting tests with mount -a"},
    {"week": 6, "day_name": "Wednesday", "offset": 32,
     "cka_title": "ServiceAccounts & SecurityContexts",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: ServiceAccount token projection\n08:20 AM - 09:30 AM: Theory: ServiceAccounts, default tokens, Pod Security Standards, runAsUser, runAsNonRoot, capabilities\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: Service Accounts & Security Contexts\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Adding NET_ADMIN capability to a pod",
     "lfcs_title": "Logical Volume Management (LVM) Architecture",
     "lfcs_desc": "03:00 PM - 03:20 PM: LVM hierarchy recall (Physical Devices -> PV -> VG -> LV -> Filesystem)\n03:20 PM - 04:20 PM: Theory: pvcreate, vgcreate, lvcreate, Volume Groups, Logical Volumes, PE (Physical Extents)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Manage and Configure LVM Storage\n05:35 PM - 06:00 PM: Synthesis: Creating and formatting a 2GB LVM volume"},
    {"week": 6, "day_name": "Thursday", "offset": 33,
     "cka_title": "Storage: Volumes, PV, PVC & StorageClasses",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: PV and PVC binding criteria (accessModes, capacity, storageClassName)\n08:20 AM - 09:30 AM: Theory: Persistent Volumes, PVCs, StorageClasses, dynamic volume provisioning, reclaim policies\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Persistent Volumes and Storage Classes\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Retain vs Delete reclaim policy verification",
     "lfcs_title": "Dynamic LVM Volume Expansion",
     "lfcs_desc": "03:00 PM - 03:20 PM: lvextend flag speedrun (-L +1G, -r, resize2fs, xfs_growfs)\n03:20 PM - 04:20 PM: Theory: Non-destructive volume expansion, resizing Ext4 vs XFS filesystems while mounted\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: Practical Terminal Lab: Extend an active LVM volume by 500MB without unmounting or data loss\n05:35 PM - 06:00 PM: Synthesis: Extending a Volume Group with a new physical disk (vgextend)"},
    {"week": 6, "day_name": "Friday", "offset": 34,
     "cka_title": "Helm & Kustomize (2025 Updates)",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Helm chart layout vs Kustomize directory structure\n08:20 AM - 09:30 AM: Theory: Helm repo/install/upgrade/values, Kustomize kustomization.yaml, overlays, transformers, patches\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:15 AM: KodeKloud Labs: Helm Basics & Kustomize Basics\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Generating patched environments using kustomize build",
     "lfcs_title": "Remote Filesystems: NFS & Storage Monitoring",
     "lfcs_desc": "03:00 PM - 03:20 PM: NFS export syntax drills (/etc/exports)\n03:20 PM - 04:20 PM: Theory: NFS server configuration, exportfs -r, NFS client mounting, storage performance monitoring (df -h, du -sh, iostat)\n04:20 PM - 04:35 PM: Walk break\n04:35 PM - 05:35 PM: KodeKloud Labs: Remote Filesystems (NFS) & Monitor Storage Performance\n05:35 PM - 06:00 PM: Error Ledger review"},
    {"week": 6, "day_name": "Saturday", "offset": 35,
     "cka_title": "Security & Storage Lab Triathlon",
     "cka_desc": "08:00 AM - 09:30 AM: Multi-tenant RBAC + ServiceAccount + PVC volume mounting scenario\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: Helm chart deployment with custom values and Kustomize overlay\n11:00 AM - 12:00 PM: Milestone 6 Assessment: Enterprise security & storage configuration",
     "lfcs_title": "Week 6 Storage Mastery & LVM Drill",
     "lfcs_desc": "03:00 PM - 04:15 PM: Complete storage marathon: Partition disk, create LVM, format XFS, mount in /etc/fstab, expand online\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Configure NFS share and mount persistently from client VM\n05:30 PM - 06:00 PM: Milestone 6 Assessment: Storage integrity and LVM expansion"},

    # Week 7
    {"week": 7, "day_name": "Monday", "offset": 36,
     "cka_title": "Cluster & Pod Networking Prerequisites",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Network namespaces and veth pairs\n08:20 AM - 09:30 AM: Theory: Pod network CIDR, IPAM, CNI (Container Network Interface) plugins (Calico, Flannel, Weave)\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Prerequisite Switching, Routing, Gateways & CNI in Kubernetes\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Inspecting CNI configuration files in /etc/cni/net.d/",
     "lfcs_title": "Linux Networking Configuration (IP & Routing)",
     "lfcs_desc": "03:00 PM - 03:20 PM: ip command speedrun (ip addr, ip link, ip route)\n03:20 PM - 04:20 PM: Theory: Static vs DHCP IP configuration, routing tables, default gateway, hostname resolution (/etc/hosts, /etc/resolv.conf)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure IPv4 & IPv6 Networking and Hostname Resolution\n05:35 PM - 06:00 PM: Synthesis: Configuring network interfaces via nmcli and ip commands"},
    {"week": 7, "day_name": "Tuesday", "offset": 37,
     "cka_title": "Service Networking & CoreDNS Deep Dive",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Service CIDR vs Pod CIDR separation\n08:20 AM - 09:30 AM: Theory: How kube-proxy intercepts service IPs, CoreDNS Corefile configuration, troubleshooting DNS lookup failures\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Service Networking & CoreDNS in Kubernetes\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Modifying CoreDNS configmap and watching resolution changes",
     "lfcs_title": "Network Bonding & Bridging",
     "lfcs_desc": "03:00 PM - 03:20 PM: Bonding modes recall (round-robin, active-backup, 802.3ad LACP)\n03:20 PM - 04:20 PM: Theory: Network device bonding for redundancy/throughput, Linux bridge devices for VM/container networks\n04:20 PM - 04:35 PM: Movement break\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure Bridge and Bonding Devices\n05:35 PM - 06:00 PM: Synthesis: Creating a software bridge interface"},
    {"week": 7, "day_name": "Wednesday", "offset": 38,
     "cka_title": "Ingress Controllers & Routing Rules",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Ingress resource vs Ingress controller\n08:20 AM - 09:30 AM: Theory: Ingress rules (host-based, path-based), annotations, rewrite-target, default-backend\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: CKA Ingress Networking Labs 1 & 2\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Testing path rewriting on Nginx ingress controller",
     "lfcs_title": "Packet Filtering with Firewalld & Iptables",
     "lfcs_desc": "03:00 PM - 03:20 PM: firewall-cmd speedrun (--add-port, --permanent, --reload)\n03:20 PM - 04:20 PM: Theory: Netfilter architecture, firewalld zones, services, rich rules, basic iptables chains (INPUT, OUTPUT, FORWARD)\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure Packet Filtering (Firewall)\n05:35 PM - 06:00 PM: Synthesis: Hardening server to allow only SSH and HTTPS"},
    {"week": 7, "day_name": "Thursday", "offset": 39,
     "cka_title": "Gateway API (2025 Updates)",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Gateway API role separation (GatewayClass, Gateway, HTTPRoute)\n08:20 AM - 09:30 AM: Theory: Gateway API architecture, comparing Ingress vs Gateway API, HTTPRoute routing matches\n09:30 AM - 09:45 AM: Physical movement\n09:45 AM - 11:15 AM: KodeKloud Labs: Gateway API (2025 Updates)\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Exploratory: Configuring weighted routing between service versions via HTTPRoute",
     "lfcs_title": "NAT, Port Redirection & Reverse Proxies",
     "lfcs_desc": "03:00 PM - 03:20 PM: NAT terminology (SNAT, DNAT, Masquerading)\n03:20 PM - 04:20 PM: Theory: Port forwarding via firewall, configuring reverse proxy / load balancer (HAProxy/Nginx fundamentals)\n04:20 PM - 04:35 PM: Posture break\n04:35 PM - 05:35 PM: KodeKloud Labs: Port Redirection and NAT & Reverse Proxies\n05:35 PM - 06:00 PM: Synthesis: Port forwarding local port 8080 to internal backend port 80"},
    {"week": 7, "day_name": "Friday", "offset": 40,
     "cka_title": "Network Policies Deep Dive",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Default deny ingress and egress manifest structure\n08:20 AM - 09:30 AM: Theory: NetworkPolicy spec, podSelector, namespaceSelector, ipBlock CIDR exceptions, ports\n09:30 AM - 09:45 AM: Movement & hydration\n09:45 AM - 11:15 AM: KodeKloud Labs: Network Policies Labs\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Visual Sketch: Drawing multi-namespace network policy isolation on whiteboard",
     "lfcs_title": "SSH Hardening, Key Auth & Time Sync",
     "lfcs_desc": "03:00 PM - 03:20 PM: ssh-keygen and ssh-copy-id speed drills\n03:20 PM - 04:20 PM: Theory: /etc/ssh/sshd_config hardening (Disable root login, password auth, custom port), chrony / timedatectl time sync\n04:20 PM - 04:35 PM: Walk break\n04:35 PM - 05:35 PM: KodeKloud Labs: Configure SSH Servers/Clients & Time Servers\n05:35 PM - 06:00 PM: Synthesis: Setting up SSH key-based access with passphrase"},
    {"week": 7, "day_name": "Saturday", "offset": 41,
     "cka_title": "Week 7 Network Mastery Triathlon",
     "cka_desc": "08:00 AM - 09:30 AM: Deploy multi-service Ingress with TLS termination and Network Policy isolation\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:00 AM: CNI crash troubleshooting and pod IP allocation recovery\n11:00 AM - 12:00 PM: Milestone 7 Assessment: Networking, Ingress & Security lockdown",
     "lfcs_title": "Week 7 Linux Networking & Firewall Marathon",
     "lfcs_desc": "03:00 PM - 04:15 PM: Build bridge network, configure static IP, set up firewalld port redirection and harden SSH\n04:15 PM - 04:30 PM: Stretch break\n04:30 PM - 05:30 PM: Timed network troubleshooting (broken default route, DNS resolver failure)\n05:30 PM - 06:00 PM: Milestone 7 Assessment: Network configuration and firewall lockdown"},

    # Week 8
    {"week": 8, "day_name": "Monday", "offset": 42,
     "cka_title": "Troubleshooting: Control Plane & Applications",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Checking control plane logs in /var/log/pods and static pod manifests\n08:20 AM - 09:30 AM: Theory: Troubleshooting kube-apiserver crashloops, etcd connection loss, misconfigured kubelet ports\n09:30 AM - 09:45 AM: Movement & posture reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Application Failure & Control Plane Failure Labs\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Exploratory: Intentionally corrupting kube-apiserver manifest and restoring service",
     "lfcs_title": "Containers & Virtual Machines on Linux",
     "lfcs_desc": "03:00 PM - 03:20 PM: Podman/Docker command speedrun (run, ps, images, exec)\n03:20 PM - 04:20 PM: Theory: Container isolation (namespaces & cgroups), KVM/QEMU, virsh CLI for VM management\n04:20 PM - 04:35 PM: Walk & reset\n04:35 PM - 05:35 PM: KodeKloud Labs: Create and Manage Containers & VMs\n05:35 PM - 06:00 PM: Synthesis: Deploying a containerized web server and binding ports"},
    {"week": 8, "day_name": "Tuesday", "offset": 43,
     "cka_title": "Troubleshooting: Worker Nodes & Network Failure",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: Node NotReady diagnostic workflow (systemctl status kubelet, journalctl -u kubelet)\n08:20 AM - 09:30 AM: Theory: Kubelet certificates renewal, CNI plugin binary issues, CoreDNS crashes\n09:30 AM - 09:45 AM: Physical reset\n09:45 AM - 11:15 AM: KodeKloud Labs: Worker Node Failure & Network Troubleshooting Labs\n11:15 AM - 11:30 AM: Micro-break\n11:30 AM - 12:00 PM: Speed Drill: Diagnosing and joining a detached worker node in under 5 minutes",
     "lfcs_title": "Timed Mock Exam 1 (Strict Exam Conditions)",
     "lfcs_desc": "03:00 PM - 03:10 PM: Terminal setup and mental grounding\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 1 (Strict timed conditions, no external help)\n04:25 PM - 04:45 PM: Walk break & cognitive decompression\n04:45 PM - 05:45 PM: Mock Exam 1 Error Analysis: Review mistakes and document in Error Ledger\n05:45 PM - 06:00 PM: Redo missed questions immediately"},
    {"week": 8, "day_name": "Wednesday", "offset": 44,
     "cka_title": "JSONPath Queries & Lightning Labs 1 & 2",
     "cka_desc": "08:00 AM - 08:20 AM: Retrieval: JSONPath syntax (-o jsonpath='{.items[*].metadata.name}')\n08:20 AM - 09:30 AM: Theory & Drills: Custom column formatting, range filtering, sorting by fields (--sort-by)\n09:30 AM - 09:45 AM: Hydration break\n09:45 AM - 11:15 AM: KodeKloud Labs: JSON Path in Kubernetes & Lightning Labs 1 & 2\n11:15 AM - 11:30 AM: Eye rest\n11:30 AM - 12:00 PM: Speed review of Lightning Lab questions completed under target time",
     "lfcs_title": "Timed Mock Exam 2 (Strict Exam Conditions)",
     "lfcs_desc": "03:00 PM - 03:10 PM: Setup & deep breathing\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 2 (Strict timed conditions)\n04:25 PM - 04:45 PM: Movement & posture reset\n04:45 PM - 05:45 PM: Mock Exam 2 Error Analysis & deep dive on missed topics\n05:45 PM - 06:00 PM: Redo failed tasks from scratch"},
    {"week": 8, "day_name": "Thursday", "offset": 45,
     "cka_title": "Timed Mock Exam 1 & Step-by-Step Review",
     "cka_desc": "08:00 AM - 08:15 AM: Terminal environment prep (alias k=kubectl, export do, export now)\n08:15 AM - 10:15 AM: KodeKloud CKA Mock Exam 1 (Strict 2-hour timed exam simulation)\n10:15 AM - 10:30 AM: Physical walk & mental reset\n10:30 AM - 12:00 PM: Comprehensive Mock 1 Review: Analyze scoring, optimize slow commands",
     "lfcs_title": "Timed Mock Exam 3 (Strict Exam Conditions)",
     "lfcs_desc": "03:00 PM - 03:10 PM: Setup & focus\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 3 (Strict timed conditions)\n04:25 PM - 04:45 PM: Physical walk\n04:45 PM - 05:45 PM: Mock Exam 3 Error Analysis & command refinement\n05:45 PM - 06:00 PM: Redo missed questions"},
    {"week": 8, "day_name": "Friday", "offset": 46,
     "cka_title": "Timed Mock Exam 2 & 3 Marathon",
     "cka_desc": "08:00 AM - 08:15 AM: Terminal warm-up\n08:15 AM - 10:00 AM: KodeKloud CKA Mock Exam 2 & 3 high-weight scenario drills\n10:00 AM - 10:15 AM: Movement & eye rest\n10:15 AM - 11:30 AM: KodeKloud Ultimate Mock Exam challenges\n11:30 AM - 12:00 PM: Verify allowed documentation bookmarks on kubernetes.io/docs",
     "lfcs_title": "Timed Mock Exam 4 & Final Speed Marathon",
     "lfcs_desc": "03:00 PM - 03:10 PM: Final exam setup\n03:10 PM - 04:25 PM: KodeKloud LFCS Mock Exam 4 (Strict timed conditions)\n04:25 PM - 04:45 PM: Walk break\n04:45 PM - 05:45 PM: 20-Question Rapid Linux Admin Scenario Sprint\n05:45 PM - 06:00 PM: Final Error Ledger consolidation"},
    {"week": 8, "day_name": "Saturday", "offset": 47,
     "cka_title": "Killer.sh Simulator Marathon (Exam Benchmark)",
     "cka_desc": "08:00 AM - 08:15 AM: Grounding, water, and full screen isolation\n08:15 AM - 10:15 AM: Killer.sh CKA Simulator Session (Strict 2-hour uninterrupted simulation)\n10:15 AM - 10:45 AM: Extended walk, fresh air, cognitive recovery\n10:45 AM - 12:00 PM: Killer.sh in-depth question review & explanation study (Target: score >= 80%)\nFinal Milestone Gate cleared!",
     "lfcs_title": "Certification Gate Review & Readiness Audit",
     "lfcs_desc": "03:00 PM - 04:30 PM: Comprehensive review of personal command cheat sheets (LVM, systemd, networking, permissions, regex)\n04:30 PM - 04:45 PM: Movement break\n04:45 PM - 06:00 PM: Final confidence check across all LFCS exam domains\nFinal Milestone Gate cleared!"}
]

# ── 4-Week Intensive Sprint Curriculum (24 Days) ──────────────────────────
CKA_DAYS_4WEEK = [
    {"week": 1, "day_num": 1, "cka_title": "Kubernetes Architecture & Container Runtimes",
     "cka_desc": "08:00-08:20: Sketch control plane from memory\n08:20-09:30: API Server, Controller Manager, Scheduler, Kubelet, Kube-proxy\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: explore cluster components\n11:15-11:30: Eye rest\n11:30-12:00: Inspect static pod manifests in /etc/kubernetes/manifests"},
    {"week": 1, "day_num": 2, "cka_title": "ETCD Fundamentals & Backup/Restore",
     "cka_desc": "08:00-08:20: ETCD role in consensus and HA\n08:20-09:30: etcdctl, snapshot save/restore, endpoint health\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: etcd operations & backup drill\n11:15-11:30: Eye rest\n11:30-12:00: Restore a cluster from etcd snapshot"},
    {"week": 1, "day_num": 3, "cka_title": "RBAC & Cluster Access Control",
     "cka_desc": "08:00-08:20: Role, ClusterRole, RoleBinding, ClusterRoleBinding\n08:20-09:30: ServiceAccount, kubectl auth can-i, impersonation\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: create restrictive RBAC policies\n11:15-11:30: Eye rest\n11:30-12:00: Debug access denied errors with --v=8"},
    {"week": 1, "day_num": 4, "cka_title": "kubeadm Cluster Lifecycle & Upgrades",
     "cka_desc": "08:00-08:20: kubeadm init/join/workflow\n08:20-09:30: Upgrade procedure: control plane then worker nodes\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: kubeadm init, join, upgrade\n11:15-11:30: Eye rest\n11:30-12:00: Practice kubeadm certs and kubeconfig management"},
    {"week": 1, "day_num": 5, "cka_title": "Pod Internals & YAML Architecture",
     "cka_desc": "08:00-08:20: Pod spec from memory drill\n08:20-09:30: Containers, ports, env, volumes layout\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: Pods with YAML\n11:15-11:30: Eye rest\n11:30-12:00: Write 10 pod manifests under 10 minutes"},
    {"week": 1, "day_num": 6, "cka_title": "Storage: PV, PVC, StorageClasses & Dynamic Provisioning",
     "cka_desc": "08:00-08:20: PV lifecycle, access modes, reclaim policies\n08:20-09:30: PVC binding, StorageClass, dynamic provisioner, CSI\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: create PV/PVC, StorageClass, expand PVC\n11:15-11:30: Eye rest\n11:30-12:00: Week 1 integration & speed drill"},
    {"week": 2, "day_num": 1, "cka_title": "Deployments, ReplicaSets & Rollbacks",
     "cka_desc": "08:00-08:20: Deployment/ReplicaSet relationship\n08:20-09:30: Rolling updates, rollout undo, history, scale\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: deployments & rollbacks\n11:15-11:30: Eye rest\n11:30-12:00: Max surge/max unavailable tuning"},
    {"week": 2, "day_num": 2, "cka_title": "ConfigMaps, Secrets & DaemonSets/StatefulSets/Jobs",
     "cka_desc": "08:00-08:20: ConfigMap/Secret creation & injection methods\n08:20-09:30: DaemonSet, StatefulSet, Job, CronJob specs\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: all workload types\n11:15-11:30: Eye rest\n11:30-12:00: Taints, tolerations & node affinity with workloads"},
    {"week": 2, "day_num": 3, "cka_title": "Services: ClusterIP, NodePort, LoadBalancer",
     "cka_desc": "08:00-08:20: Service types and kube-proxy modes\n08:20-09:30: Endpoints, selectors, headless services\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: service creation & troubleshooting\n11:15-11:30: Eye rest\n11:30-12:00: DNS resolution within cluster"},
    {"week": 2, "day_num": 4, "cka_title": "Ingress Controllers & Gateway API",
     "cka_desc": "08:00-08:20: Ingress resource, rules, TLS\n08:20-09:30: Nginx Ingress controller setup, path-based routing\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: Ingress configuration\n11:15-11:30: Eye rest\n11:30-12:00: Gateway API intro & comparison with Ingress"},
    {"week": 2, "day_num": 5, "cka_title": "Network Policies & CNI (Calico)",
     "cka_desc": "08:00-08:20: NetworkPolicy spec, ingress/egress rules\n08:20-09:30: Default deny, label selectors, CIDR blocks\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: apply & test network policies\n11:15-11:30: Eye rest\n11:30-12:00: CNI overview (Calico, Cilium, Flannel)"},
    {"week": 2, "day_num": 6, "cka_title": "Helm, Kustomize & CRDs/Operators",
     "cka_desc": "08:00-08:20: Helm chart structure, values.yaml, templates\n08:20-09:30: Kustomize bases/overlays, helm install/upgrade/rollback\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: Helm & Kustomize\n11:15-11:30: Eye rest\n11:30-12:00: CRD creation & operator basics"},
    {"week": 3, "day_num": 1, "cka_title": "Node & kubelet Troubleshooting",
     "cka_desc": "08:00-08:20: kubelet logs, status, config\n08:20-09:30: Node NotReady diagnosis, container runtime issues\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: node troubleshooting scenarios\n11:15-11:30: Eye rest\n11:30-12:00: kubectl describe node, events, conditions"},
    {"week": 3, "day_num": 2, "cka_title": "Control Plane Troubleshooting",
     "cka_desc": "08:00-08:20: API server down, scheduler not scheduling\n08:20-09:30: Controller manager issues, etcd unreachable\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: control plane failure scenarios\n11:15-11:30: Eye rest\n11:30-12:00: Static pod manifests & self-healing control plane"},
    {"week": 3, "day_num": 3, "cka_title": "Cluster & Network Troubleshooting",
     "cka_desc": "08:00-08:20: Pod networking failures, DNS resolution issues\n08:20-09:30: Service connectivity, CoreDNS debugging, CNI issues\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: network troubleshooting exercises\n11:15-11:30: Eye rest\n11:30-12:00: kubectl exec + wget/curl for connectivity tests"},
    {"week": 3, "day_num": 4, "cka_title": "Application & Container Log Troubleshooting",
     "cka_desc": "08:00-08:20: kubectl logs, --previous, multi-container logs\n08:20-09:30: Events, kubectl describe pod, troubleshooting pending/crashloop pods\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: diagnose 10 different pod failures\n11:15-11:30: Eye rest\n11:30-12:00: Practice: OOMKilled, ImagePullBackOff, CrashLoopBackOff fixes"},
    {"week": 3, "day_num": 5, "cka_title": "Worker Node & etcd Troubleshooting",
     "cka_desc": "08:00-08:20: kubeadm join failure diagnosis\n08:20-09:30: Certificate issues, kubelet bootstrap, networking on new node\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: join & remove nodes, etcd member management\n11:15-11:30: Eye rest\n11:30-12:00: etcd cluster health, defragmentation, alarm handling"},
    {"week": 3, "day_num": 6, "cka_title": "HA Control Plane & Extension Interfaces",
     "cka_desc": "08:00-08:20: HA topologies (stacked vs external etcd)\n08:20-09:30: CNI/CSI/CRI interfaces, cloud provider integration\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: HA cluster design\n11:15-11:30: Eye rest\n11:30-12:00: Week 3 consolidation & speed drill"},
    {"week": 4, "day_num": 1, "cka_title": "Workloads & Scheduling Review",
     "cka_desc": "08:00-08:20: Error recall: ConfigMap, Secret, Pod specs from memory\n08:20-09:30: Deployments, DaemonSets, StatefulSets, Jobs - complete refresher\n09:30-09:45: Break\n09:45-11:00: Speed drill: 15 workload manifests in 15 minutes\n11:00-12:00: Taints, tolerations, affinity, admission controllers review"},
    {"week": 4, "day_num": 2, "cka_title": "Services & Networking Review",
     "cka_desc": "08:00-08:20: Service types, DNS, Endpoints recall drill\n08:20-09:30: NetworkPolicy, Ingress, Gateway API refresher\n09:30-09:45: Break\n09:45-11:00: KodeKloud mock scenarios for networking\n11:00-12:00: CNI debugging, CoreDNS troubleshooting practice"},
    {"week": 4, "day_num": 3, "cka_title": "Architecture & Storage Review",
     "cka_desc": "08:00-08:20: kubeadm, etcd, RBAC refresher from memory\n08:20-09:30: PV/PVC/StorageClass complete drill\n09:30-09:45: Break\n09:45-11:00: Helm, Kustomize, CRDs speed practice\n11:00-12:00: etcd backup/restore final practice"},
    {"week": 4, "day_num": 4, "cka_title": "Timed Mock Exam 1 (Strict 2-Hour Simulation)",
     "cka_desc": "08:00-08:15: Setup & focus\n08:15-10:15: KodeKloud CKA Mock Exam 1 (strict timed)\n10:15-10:30: Walk & reset\n10:30-12:00: Mock 1 review: analyze scoring, optimize slow commands"},
    {"week": 4, "day_num": 5, "cka_title": "Timed Mock Exam 2 & High-Weight Scenarios",
     "cka_desc": "08:00-08:15: Terminal warm-up\n08:15-10:00: Troubleshooting scenario marathon (30% domain focus)\n10:00-10:15: Break\n10:15-11:30: Networking & architecture scenario drills\n11:30-12:00: Bookmark verification on kubernetes.io/docs"},
    {"week": 4, "day_num": 6, "cka_title": "Final Readiness Audit & Confidence Check",
     "cka_desc": "08:00-09:30: Review all error notes and weak areas\n09:30-09:45: Break\n09:45-11:00: 10-question speed sprint across all 5 domains\n11:00-12:00: Certification gate review, finalize exam strategy"}
]

LFCS_DAYS_4WEEK = [
    {"week": 1, "day_num": 1, "lfcs_title": "Process Management & System Services",
     "lfcs_desc": "03:00-03:20: ps, top, htop, pgrep, kill, nice, renice\n03:20-04:20: systemctl, service files, journald logs\n04:20-04:35: Break\n04:35-05:35: Lab: create custom systemd service, troubleshoot failed unit\n05:35-06:00: Cheat sheet & review"},
    {"week": 1, "day_num": 2, "lfcs_title": "Job Scheduling (cron, at, systemd timers)",
     "lfcs_desc": "03:00-03:20: crontab syntax, /etc/cron.d, anacron\n03:20-04:20: at, batch, systemd timers (OnCalendar, OnBootSec)\n04:20-04:35: Break\n04:35-05:35: Lab: schedule backups with systemd timer, validate cron jobs\n05:35-06:00: Review & debug common cron issues"},
    {"week": 1, "day_num": 3, "lfcs_title": "Package Management (dnf/yum & apt)",
     "lfcs_desc": "03:00-03:20: dnf/yum install, remove, update, history\n03:20-04:20: Repo config, GPG keys, module streams, dnf repolist\n04:20-04:35: Break\n04:35-05:35: Lab: add repo, install from local RPM, verify package integrity\n05:35-06:00: Troubleshoot dependency conflicts"},
    {"week": 1, "day_num": 4, "lfcs_title": "Kernel Parameters & System Tuning",
     "lfcs_desc": "03:00-03:20: sysctl -a, /etc/sysctl.conf, sysctl.d drop-ins\n03:20-04:20: Persistent vs non-persistent tuning, /proc filesystem\n04:20-04:35: Break\n04:35-05:35: Lab: tune TCP parameters, vm.swappiness, enable IP forwarding\n05:35-06:00: Verify with sysctl -p and /proc/sys/net/ipv4/*"},
    {"week": 1, "day_num": 5, "lfcs_title": "Hardware Recovery & Emergency Mode",
     "lfcs_desc": "03:00-03:20: GRUB2 bootloader, initramfs, kernel panic\n03:20-04:20: Emergency/rescue mode, root password reset, fsck\n04:20-04:35: Break\n04:35-05:35: Lab: reboot into emergency mode, repair /etc/fstab, reset root pw\n05:35-06:00: Review: backup strategies with rsync and tar"},
    {"week": 1, "day_num": 6, "lfcs_title": "SELinux & Container Engines",
     "lfcs_desc": "03:00-03:20: SELinux modes, contexts, booleans, setsebool\n03:20-04:20: Podman/Docker: run, exec, build, podman generate systemd\n04:20-04:35: Break\n04:35-05:35: Lab: run container with custom SELinux label, troubleshoot AVC denials\n05:35-06:00: Week 1 consolidation & practice questions"},
    {"week": 2, "day_num": 1, "lfcs_title": "IPv4/IPv6 Configuration & Hostname Resolution",
     "lfcs_desc": "03:00-03:20: nmcli, ip addr, /etc/hosts, hostnamectl\n03:20-04:20: Static IP vs DHCP, DNS resolution, resolv.conf, systemd-resolved\n04:20-04:35: Break\n04:35-05:35: Lab: configure static IPv4+IPv6, set hostname, test resolution\n05:35-06:00: Troubleshoot with dig, nslookup, host"},
    {"week": 2, "day_num": 2, "lfcs_title": "Time Synchronization (chrony/NTP)",
     "lfcs_desc": "03:00-03:20: chronyd vs ntpd, /etc/chrony.conf\n03:20-04:20: chronyc sources, time drift, hwclock, timedatectl\n04:20-04:35: Break\n04:35-05:35: Lab: configure chrony server + client, verify drift, force sync\n05:35-06:00: Troubleshoot time skew issues"},
    {"week": 2, "day_num": 3, "lfcs_title": "Network Monitoring & Troubleshooting",
     "lfcs_desc": "03:00-03:20: ss, netstat, ip -s link, ethtool\n03:20-04:20: tcpdump filters, ping, traceroute, mtr, curl/wget diagnostics\n04:20-04:35: Break\n04:35-05:35: Lab: capture traffic on specific port, trace connectivity issues\n05:35-06:00: Review: systematic network troubleshooting methodology"},
    {"week": 2, "day_num": 4, "lfcs_title": "OpenSSH Server & Client Configuration",
     "lfcs_desc": "03:00-03:20: ssh-keygen, ssh-copy-id, agent forwarding\n03:20-04:20: sshd_config hardening: PermitRootLogin, AllowUsers, key-only auth\n04:20-04:35: Break\n04:35-05:35: Lab: harden sshd, set up key-based auth, tunnel (L/R/D), jump host\n05:35-06:00: Verify with ssh -v, audit with sshd -T"},
    {"week": 2, "day_num": 5, "lfcs_title": "Firewall: iptables/nftables & NAT",
     "lfcs_desc": "03:00-03:20: iptables chain/filter/mangle, nftables tables/rulesets\n03:20-04:20: firewalld zones, rich rules, port forwarding, masquerade (SNAT/DNAT)\n04:20-04:35: Break\n04:35-05:35: Lab: create firewall rules, NAT gateway, block/allow specific services\n05:35-06:00: Verify with nft list ruleset, iptables -L -v -n"},
    {"week": 2, "day_num": 6, "lfcs_title": "Static Routing, Bridges, Bonding & Load Balancers",
     "lfcs_desc": "03:00-03:20: ip route add, route persistence, bridge (brctl / ip link add type bridge)\n03:20-04:20: NIC bonding (active-backup, 802.3ad), /etc/nm-dispatcher scripts\n04:20-04:35: Break\n04:35-05:35: Lab: set up bridge for VMs, NIC bonding, static route, nginx reverse proxy\n05:35-06:00: Week 2 consolidation & full networking review"},
    {"week": 3, "day_num": 1, "lfcs_title": "LVM: PV, VG, LV Management",
     "lfcs_desc": "03:00-03:20: pvcreate, vgcreate, lvcreate, pvs/vgs/lvs\n03:20-04:20: Extend/shrink LVs, thin provisioning, snapshots\n04:20-04:35: Break\n04:35-05:35: Lab: create full LVM stack, extend online, create & restore snapshot\n05:35-06:00: Troubleshoot LVM with pvdisplay, vgcfgbackup"},
    {"week": 3, "day_num": 2, "lfcs_title": "Filesystems: create, mount, repair & /etc/fstab",
     "lfcs_desc": "03:00-03:20: mkfs.ext4, mkfs.xfs, mount/umount, /etc/fstab\n03:20-04:20: fsck, xfs_repair, tune2fs, UUID vs LABEL, blkid\n04:20-04:35: Break\n04:35-05:35: Lab: create filesystem, mount by UUID, repair unmountable FS, fix fstab\n05:35-06:00: /proc/mounts analysis & recovery from bad fstab"},
    {"week": 3, "day_num": 3, "lfcs_title": "Remote Filesystems, NFS, iSCSI & Automounters",
     "lfcs_desc": "03:00-03:20: NFS server/client setup, /etc/exports, rpcbind, mount -t nfs\n03:20-04:20: iSCSI target/initiator, autofs /net map, /etc/auto.master\n04:20-04:35: Break\n04:35-05:35: Lab: export NFS share, connect iSCSI LUN, configure autofs for /net\n05:35-06:00: Security: restrict NFS exports, CHAP for iSCSI"},
    {"week": 3, "day_num": 4, "lfcs_title": "Swap Management & Storage Monitoring",
     "lfcs_desc": "03:00-03:20: swapon/swapoff, /swapfile, mkswap, /etc/fstab swap entry\n03:20-04:20: iostat, iotop, blkid, lsblk, df -h, du -sh\n04:20-04:35: Break\n04:35-05:35: Lab: create & activate swapfile, monitor I/O with iostat, troubleshoot disk full\n05:35-06:00: logrotate, find old files, reclaim space"},
    {"week": 3, "day_num": 5, "lfcs_title": "VFS, /proc, /sys & Container Storage",
     "lfcs_desc": "03:00-03:20: /proc/[pid]/, /proc/sys/, sysctl runtime vs persistent\n03:20-04:20: /sys/block/, /sys/fs/, cgroups v1 vs v2, overlay filesystems\n04:20-04:35: Break\n04:35-05:35: Lab: inspect container storage drivers, tune cgroup memory/CPU limits\n05:35-06:00: Week 3 consolidation & storage drill"},
    {"week": 3, "day_num": 6, "lfcs_title": "Essential Commands: Git, SSL/TLS & Disk Troubleshooting",
     "lfcs_desc": "03:00-03:20: git init, add, commit, branch, merge, rebase, stash, diff\n03:20-04:20: openssl req/x509, create self-signed cert, verify with openssl s_client\n04:20-04:35: Break\n04:35-05:35: Lab: solve 20-question speed sprint covering Git, certificates, disk issues\n05:35-06:00: Error ledger review & consolidation"},
    {"week": 4, "day_num": 1, "lfcs_title": "systemd Services Deep Dive & Troubleshooting",
     "lfcs_desc": "03:00-03:20: systemctl (enable/disable/start/stop/mask), unit files\n03:20-04:20: journalctl -u, systemd-analyze, systemctl list-dependencies\n04:20-04:35: Break\n04:35-05:35: Lab: create complex service, troubleshoot 3 broken services, analyze boot\n05:35-06:00: Practice exam scenario"},
    {"week": 4, "day_num": 2, "lfcs_title": "System Performance & Resource Limits",
     "lfcs_desc": "03:00-03:20: ulimit -a, /etc/security/limits.conf, pam_limits.so\n03:20-04:20: nice/renice, cpuset, systemd-run --scope, cgroup v2 delegation\n04:20-04:35: Break\n04:35-05:35: Lab: set per-user limits, restrict container CPU/memory, analyze top processes\n05:35-06:00: vmstat, sar, free -m analysis"},
    {"week": 4, "day_num": 3, "lfcs_title": "User/Group Accounts, Profiles & PAM",
     "lfcs_desc": "03:00-03:20: useradd, usermod, userdel, groupadd, gpasswd, /etc/shadow, pwconv\n03:20-04:20: /etc/profile, ~/.bashrc, ~/.bash_profile, pam_env, pam_wheel\n04:20-04:35: Break\n04:35-05:35: Lab: create user with custom home skeleton, enforce password aging, PAM config\n05:35-06:00: SELinux context for new user home directories"},
    {"week": 4, "day_num": 4, "lfcs_title": "POSIX ACLs & LDAP Integration",
     "lfcs_desc": "03:00-03:20: getfacl, setfacl, -m, -x, default ACLs\n03:20-04:20: LDAP client config (authselect sssd, nslcd), /etc/sssd/sssd.conf\n04:20-04:35: Break\n04:35-05:35: Lab: set ACL on shared dir, test inheritance, verify LDAP user lookup\n05:35-06:00: getent passwd/group verification"},
    {"week": 4, "day_num": 5, "lfcs_title": "LFCS Mock Exam 1 (Strict Timed Conditions)",
     "lfcs_desc": "03:00-03:10: Setup & focus\n03:10-04:25: 20-question LFCS-style mock exam (all domains)\n04:25-04:35: Walk break\n04:35-05:45: Review incorrect answers, document weak areas\n05:45-06:00: Redo missed questions"},
    {"week": 4, "day_num": 6, "lfcs_title": "LFCS Mock Exam 2 & Final Readiness Audit",
     "lfcs_desc": "03:00-03:10: Final exam setup\n03:10-04:25: 20-question rapid-fire LFCS mock (all domains)\n04:25-04:35: Walk break\n04:35-05:30: Final error ledger consolidation\n05:30-06:00: Certification gate review across all LFCS domains"}
]


# ── Date Helpers ──────────────────────────────────────────────────────────
def get_upcoming_monday(ref_date: datetime = None) -> datetime:
    if ref_date is None:
        ref_date = datetime.now()
    days_ahead = (7 - ref_date.weekday()) % 7
    if days_ahead == 0 and ref_date.hour >= 18:
        days_ahead = 7
    elif days_ahead == 0 and ref_date.weekday() != 0:
        days_ahead = 7
    res = ref_date + timedelta(days=days_ahead)
    return res.replace(hour=0, minute=0, second=0, microsecond=0)


def resolve_start_date(input_str: str) -> datetime:
    raw = input_str.strip().lower()
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    if not raw or raw in ("next monday", "monday", "default"):
        return get_upcoming_monday(today)
    if raw == "today":
        return today
    if raw == "tomorrow":
        return today + timedelta(days=1)
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            pass
    raise ValueError(f"Could not parse start date '{input_str}'. Expected YYYY-MM-DD.")


def resolve_duration(input_str: str) -> int:
    raw = input_str.strip().lower()
    if not raw or raw in ("1", "8", "8 weeks", "standard"):
        return 8
    if raw in ("2", "4", "4 weeks", "intensive", "sprint"):
        return 4
    if raw == "3":
        return 8
    try:
        val = int(raw.replace("weeks", "").replace("w", "").strip())
        if 1 <= val <= 24:
            return val
    except ValueError:
        pass
    return 8


def resolve_track(input_str: str) -> str:
    raw = input_str.strip().lower()
    if not raw or raw in ("1", "both", "all", "dual"):
        return "both"
    if raw in ("2", "cka"):
        return "cka"
    if raw in ("3", "lfcs"):
        return "lfcs"
    return "both"


def resolve_pause_weeks(input_str: str) -> list:
    raw = input_str.strip().lower()
    if not raw or raw in ("none", "0", "no", "n"):
        return []
    result = []
    for part in raw.replace(";", ",").split(","):
        p = part.strip().replace("week", "").replace("w", "").strip()
        if p.isdigit():
            result.append(int(p))
    return sorted(list(set(result)))


# ── Study Time Parsing & Formatting ──────────────────────────────────────
def parse_time_str(s: str, default_ampm: str = None):
    s = s.strip().lower()
    m = re.match(r"^(\d{1,2})(?::(\d{2}))?\s*(am|pm)?$", s)
    if not m:
        return None
    h = int(m.group(1))
    minute = int(m.group(2)) if m.group(2) else 0
    ampm = m.group(3) or default_ampm

    if ampm:
        ampm = ampm.lower()
        if ampm == "pm" and h < 12:
            h += 12
        elif ampm == "am" and h == 12:
            h = 0
    return (h, minute)


def parse_time_window(val: str, default_start: str = "08:00 AM", default_end: str = "12:00 PM") -> dict:
    if not val or not val.strip():
        val = f"{default_start} to {default_end}"
    raw = val.strip().replace(" - ", " to ").replace("-", " to ")
    parts = [p.strip() for p in raw.split(" to ") if p.strip()]
    if len(parts) != 2:
        return None

    end_ampm = "pm" if "pm" in parts[1].lower() else ("am" if "am" in parts[1].lower() else None)
    first_has_ampm = "am" in parts[0].lower() or "pm" in parts[0].lower()
    default_first_ampm = None if first_has_ampm else end_ampm

    t1 = parse_time_str(parts[0], default_ampm=default_first_ampm)
    t2 = parse_time_str(parts[1])
    if not t1 or not t2:
        return None

    def format_tuple(t):
        h, m = t
        ampm = "AM" if h < 12 else "PM"
        h12 = h % 12
        if h12 == 0:
            h12 = 12
        csv_str = f"{h12:02d}:{m:02d} {ampm}"
        ics_str = f"{h:02d}{m:02d}00"
        label = f"{h12}{(':' + str(m).zfill(2)) if m else ''}{ampm.lower()}"
        return csv_str, ics_str, label

    c1, i1, l1 = format_tuple(t1)
    c2, i2, l2 = format_tuple(t2)
    return {
        "csv_start": c1,
        "csv_end": c2,
        "ics_start": i1,
        "ics_end": i2,
        "label": f"{l1}-{l2}",
        "t_start": t1,
        "t_end": t2,
    }


def format_event_description(track: str, time_window: dict, topic: str, original_desc: str) -> str:
    start_label = time_window["csv_start"]
    end_label = time_window["csv_end"]

    is_standard = (
        (track == "CKA" and start_label == "08:00 AM" and end_label == "12:00 PM") or
        (track == "LFCS" and start_label == "03:00 PM" and end_label == "06:00 PM")
    )
    if is_standard:
        return f"{track} STUDY BLOCK ({start_label} - {end_label})\nTopic: {topic}\n\nSchedule:\n{original_desc}"

    clean_lines = []
    for line in original_desc.split("\n"):
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^\d{2}:\d{2}\s*[AP]M\s*-\s*\d{2}:\d{2}\s*[AP]M:\s*", "• ", line)
        if not line.startswith("• "):
            line = f"• {line}"
        clean_lines.append(line)

    activities_str = "\n".join(clean_lines)
    return (
        f"{track} STUDY BLOCK ({start_label} - {end_label})\n"
        f"Topic: {topic}\n\n"
        f"Curriculum Focus & Daily Objectives:\n"
        f"{activities_str}"
    )


# ── Interactive Prompting ─────────────────────────────────────────────────
def prompt_user_inputs(default_track: str = None) -> tuple:
    print()
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║          CKA & LFCS Study Calendar & Schedule Generator            ║")
    print("║     Generates calendar-aligned .ics (iCal) and .csv schedules     ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print()

    # 1. Start Date
    default_monday = get_upcoming_monday()
    default_str = default_monday.strftime("%Y-%m-%d")
    print("📅 [Step 1/5] When do you plan to start studying?")
    print("   Options: YYYY-MM-DD, 'today', 'tomorrow', or 'next monday'")
    while True:
        try:
            val = input(f"   Enter start date [Default: upcoming Monday {default_str}]: ").strip()
            start_date = resolve_start_date(val)
            print(f"   ✓ Start date selected: {start_date.strftime('%A, %B %d, %Y')}\n")
            break
        except ValueError as e:
            print(f"   [!] {e}. Please enter a valid date.")

    # 2. Duration / Length
    print("⏱️  [Step 2/5] For how long do you plan to study?")
    print("   [1] 8 Weeks — Standard Comprehensive Track (6 days/week, ~48 days) [Recommended]")
    print("   [2] 4 Weeks — Accelerated Intensive Sprint (condensed double-pace, ~24 days)")
    print("   [3] Custom duration (enter any number of weeks between 1 and 16)")
    while True:
        val = input("   Select duration [1-3 or number of weeks, default: 1]: ").strip()
        if val == "3":
            cust = input("   Enter total number of weeks (1-16): ").strip()
            duration_weeks = resolve_duration(cust)
        else:
            duration_weeks = resolve_duration(val)
        print(f"   ✓ Duration selected: {duration_weeks} Weeks\n")
        break

    # 3. Track selection
    if default_track in ("cka", "lfcs"):
        track = default_track
        print(f"🎯 [Step 3/5] Certification Track: {track.upper()} (Preselected)\n")
    else:
        print("🎯 [Step 3/5] Which certification track are you preparing for?")
        print("   [1] Both CKA & LFCS (Dual Track) [Default]")
        print("   [2] CKA Only (Certified Kubernetes Administrator)")
        print("   [3] LFCS Only (Linux Foundation Certified SysAdmin)")
        val = input("   Select track [1-3, default: 1]: ").strip()
        track = resolve_track(val)
        print(f"   ✓ Track selected: {track.upper()}\n")

    # 4. Scheduled Pauses
    print("⏸️  [Step 4/5] Do you want to schedule any pause or break weeks?")
    print("   (e.g., enter '2' to pause during week 2, 'none' for continuous study)")
    val = input("   Pause weeks [default: none]: ").strip()
    pauses = resolve_pause_weeks(val)
    if pauses:
        print(f"   ✓ Pauses scheduled at week(s): {pauses}\n")
    else:
        print("   ✓ Continuous study with no planned pause weeks.\n")

    # 5. Daily Study Hours
    print("🕐 [Step 5/5] What specific hours of the day do you want to study?")
    cka_time = None
    lfcs_time = None

    if track in ("both", "cka"):
        print("   Enter your preferred CKA daily time window (e.g. '4am to 12pm', '8am to 12pm', '06:00-10:00')")
        while True:
            val = input("   CKA Study Hours [default: 08:00 AM - 12:00 PM]: ").strip()
            cka_time = parse_time_window(val, default_start="08:00 AM", default_end="12:00 PM")
            if cka_time:
                print(f"   ✓ CKA daily study block: {cka_time['csv_start']} - {cka_time['csv_end']} ({cka_time['label']})\n")
                break
            print("   [!] Could not parse time window. Format example: '4am to 12pm' or '08:00 AM - 12:00 PM'.")

    if track in ("both", "lfcs"):
        print("   Enter your preferred LFCS daily time window (e.g. '6pm to 8pm', '3pm to 6pm', '18:00-21:00')")
        while True:
            val = input("   LFCS Study Hours [default: 03:00 PM - 06:00 PM]: ").strip()
            lfcs_time = parse_time_window(val, default_start="03:00 PM", default_end="06:00 PM")
            if lfcs_time:
                print(f"   ✓ LFCS daily study block: {lfcs_time['csv_start']} - {lfcs_time['csv_end']} ({lfcs_time['label']})\n")
                break
            print("   [!] Could not parse time window. Format example: '6pm to 8pm' or '03:00 PM - 06:00 PM'.")

    return start_date, duration_weeks, track, pauses, cka_time, lfcs_time


# ── Schedule Event Builders ───────────────────────────────────────────────
def build_events(start_date: datetime, duration_weeks: int, track: str, pauses: list = None, cka_time: dict = None, lfcs_time: dict = None) -> list:
    if pauses is None:
        pauses = []
    if cka_time is None:
        cka_time = parse_time_window("", "08:00 AM", "12:00 PM")
    if lfcs_time is None:
        lfcs_time = parse_time_window("", "03:00 PM", "06:00 PM")

    events = []
    now_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # Determine pacing mode
    if duration_weeks == 4:
        # 4-Week Sprint (24 study days)
        curr = start_date
        placed = 0
        current_week = 1

        while placed < 24 and current_week <= 6:
            # Handle pause week
            if current_week in pauses:
                for day_idx in range(7):
                    ds = (curr + timedelta(days=day_idx)).strftime("%Y%m%d")
                    csv_date = (curr + timedelta(days=day_idx)).strftime("%m/%d/%Y")
                    events.append({
                        "uid": f"pause-w{current_week}d{day_idx}@{ds}",
                        "subject": f"[PAUSE] Scheduled Break (Week {current_week})",
                        "start_dt": f"{ds}T080000",
                        "end_dt": f"{ds}T180000",
                        "csv_date": csv_date,
                        "csv_start": "08:00 AM",
                        "csv_end": "06:00 PM",
                        "desc": "Scheduled rest and recovery week.\nDetached from terminal to recharge cognitive endurance.",
                        "type": "REST"
                    })
                curr += timedelta(days=7)
                pauses = [p for p in pauses if p != current_week]
                continue

            if curr.weekday() == 6:  # Sunday
                ds = curr.strftime("%Y%m%d")
                csv_date = curr.strftime("%m/%d/%Y")
                events.append({
                    "uid": f"rest-w{current_week}@{ds}",
                    "subject": f"[REST] Full Recovery & Memory Consolidation (Week {current_week})",
                    "start_dt": f"{ds}T080000",
                    "end_dt": f"{ds}T180000",
                    "csv_date": csv_date,
                    "csv_start": "08:00 AM",
                    "csv_end": "06:00 PM",
                    "desc": "Complete detachment from code and terminal.\nPhysical movement, outdoor activities, restorative sleep.",
                    "type": "REST"
                })
                current_week += 1
            else:
                cka = CKA_DAYS_4WEEK[placed]
                lfcs = LFCS_DAYS_4WEEK[placed]
                ds = curr.strftime("%Y%m%d")
                csv_date = curr.strftime("%m/%d/%Y")

                if track in ("both", "cka"):
                    events.append({
                        "uid": f"cka-w{cka['week']}d{cka['day_num']}@{ds}",
                        "subject": f"[CKA] {cka_time['label']}: {cka['cka_title']}",
                        "start_dt": f"{ds}T{cka_time['ics_start']}",
                        "end_dt": f"{ds}T{cka_time['ics_end']}",
                        "csv_date": csv_date,
                        "csv_start": cka_time["csv_start"],
                        "csv_end": cka_time["csv_end"],
                        "desc": format_event_description("CKA", cka_time, cka["cka_title"], cka["cka_desc"]),
                        "type": "CKA"
                    })

                if track == "both":
                    if cka_time["t_end"] <= lfcs_time["t_start"]:
                        gap_minutes = (lfcs_time["t_start"][0]*60 + lfcs_time["t_start"][1]) - (cka_time["t_end"][0]*60 + cka_time["t_end"][1])
                        if gap_minutes >= 45:
                            rec_ics_start = cka_time["ics_end"]
                            rec_ics_end = lfcs_time["ics_start"]
                            rec_csv_start = cka_time["csv_end"]
                            rec_csv_end = lfcs_time["csv_start"]
                            rec_label = f"{cka_time['label'].split('-')[-1]}-{lfcs_time['label'].split('-')[0]}"
                            events.append({
                                "uid": f"rec-w{cka['week']}d{cka['day_num']}@{ds}",
                                "subject": f"[RECOVERY] {rec_label}: Cognitive Reset & Physical Regeneration",
                                "start_dt": f"{ds}T{rec_ics_start}",
                                "end_dt": f"{ds}T{rec_ics_end}",
                                "csv_date": csv_date,
                                "csv_start": rec_csv_start,
                                "csv_end": rec_csv_end,
                                "desc": f"COGNITIVE RECOVERY & INTEGRATION ({rec_csv_start} - {rec_csv_end})\n• Nutritious lunch & total screen detachment\n• Aerobic exercise / brisk walk outside (BDNF boost)\n• Power nap or Non-Sleep Deep Rest (NSDR)\n• Terminal & desk prep for LFCS",
                                "type": "RECOVERY"
                            })

                if track in ("both", "lfcs"):
                    events.append({
                        "uid": f"lfcs-w{lfcs['week']}d{lfcs['day_num']}@{ds}",
                        "subject": f"[LFCS] {lfcs_time['label']}: {lfcs['lfcs_title']}",
                        "start_dt": f"{ds}T{lfcs_time['ics_start']}",
                        "end_dt": f"{ds}T{lfcs_time['ics_end']}",
                        "csv_date": csv_date,
                        "csv_start": lfcs_time["csv_start"],
                        "csv_end": lfcs_time["csv_end"],
                        "desc": format_event_description("LFCS", lfcs_time, lfcs["lfcs_title"], lfcs["lfcs_desc"]),
                        "type": "LFCS"
                    })

                placed += 1

            curr += timedelta(days=1)

    else:
        # 8-Week or Custom Standard Pace (up to 48 study days)
        # 6 study days per week (Monday to Saturday), Sunday rest
        curr = start_date
        placed = 0
        total_days = len(DAYS_CURRICULUM_8WEEK)
        current_week = 1

        while placed < total_days:
            # Check for scheduled pause week
            if current_week in pauses:
                for day_idx in range(7):
                    p_date = curr + timedelta(days=day_idx)
                    ds = p_date.strftime("%Y%m%d")
                    csv_date = p_date.strftime("%m/%d/%Y")
                    events.append({
                        "uid": f"pause-w{current_week}d{day_idx}@{ds}",
                        "subject": f"[PAUSE] Scheduled Break (Week {current_week})",
                        "start_dt": f"{ds}T080000",
                        "end_dt": f"{ds}T180000",
                        "csv_date": csv_date,
                        "csv_start": "08:00 AM",
                        "csv_end": "06:00 PM",
                        "desc": "Scheduled rest and recovery week.\nDetached from terminal to recharge cognitive endurance.",
                        "type": "REST"
                    })
                curr += timedelta(days=7)
                pauses = [p for p in pauses if p != current_week]
                continue

            if curr.weekday() == 6:  # Sunday
                ds = curr.strftime("%Y%m%d")
                csv_date = curr.strftime("%m/%d/%Y")
                label = "Exam Ready! Full Rest & Mental Grounding" if placed >= total_days - 6 else f"Full Recovery & Memory Consolidation (Week {current_week})"
                events.append({
                    "uid": f"rest-w{current_week}@{ds}",
                    "subject": f"[REST] {label}",
                    "start_dt": f"{ds}T080000",
                    "end_dt": f"{ds}T180000",
                    "csv_date": csv_date,
                    "csv_start": "08:00 AM",
                    "csv_end": "06:00 PM",
                    "desc": "Complete detachment from code and terminal.\nEngage in physical movement, outdoor activities, social time, and restorative sleep.\nAllows long-term synaptic consolidation of weekly concepts.",
                    "type": "REST"
                })
                current_week += 1
            else:
                day = DAYS_CURRICULUM_8WEEK[placed]
                ds = curr.strftime("%Y%m%d")
                csv_date = curr.strftime("%m/%d/%Y")

                # CKA Event
                if track in ("both", "cka"):
                    events.append({
                        "uid": f"cka-w{day['week']}d{placed+1}@{ds}",
                        "subject": f"[CKA] {cka_time['label']}: {day['cka_title']}",
                        "start_dt": f"{ds}T{cka_time['ics_start']}",
                        "end_dt": f"{ds}T{cka_time['ics_end']}",
                        "csv_date": csv_date,
                        "csv_start": cka_time["csv_start"],
                        "csv_end": cka_time["csv_end"],
                        "desc": format_event_description("CKA", cka_time, day["cka_title"], day["cka_desc"]),
                        "type": "CKA"
                    })

                # Midday Recovery
                if track == "both":
                    if cka_time["t_end"] <= lfcs_time["t_start"]:
                        gap_minutes = (lfcs_time["t_start"][0]*60 + lfcs_time["t_start"][1]) - (cka_time["t_end"][0]*60 + cka_time["t_end"][1])
                        if gap_minutes >= 45:
                            rec_ics_start = cka_time["ics_end"]
                            rec_ics_end = lfcs_time["ics_start"]
                            rec_csv_start = cka_time["csv_end"]
                            rec_csv_end = lfcs_time["csv_start"]
                            rec_label = f"{cka_time['label'].split('-')[-1]}-{lfcs_time['label'].split('-')[0]}"
                            events.append({
                                "uid": f"recovery-w{day['week']}d{placed+1}@{ds}",
                                "subject": f"[RECOVERY] {rec_label}: Cognitive Reset & Physical Regeneration",
                                "start_dt": f"{ds}T{rec_ics_start}",
                                "end_dt": f"{ds}T{rec_ics_end}",
                                "csv_date": csv_date,
                                "csv_start": rec_csv_start,
                                "csv_end": rec_csv_end,
                                "desc": f"COGNITIVE RECOVERY & INTEGRATION ({rec_csv_start} - {rec_csv_end})\n• Nutritious meal & total screen detachment\n• Aerobic exercise / brisk walk outside (BDNF boost)\n• Power nap or Non-Sleep Deep Rest (NSDR)\n• Terminal & desk prep for LFCS",
                                "type": "RECOVERY"
                            })

                # LFCS Event
                if track in ("both", "lfcs"):
                    events.append({
                        "uid": f"lfcs-w{day['week']}d{placed+1}@{ds}",
                        "subject": f"[LFCS] {lfcs_time['label']}: {day['lfcs_title']}",
                        "start_dt": f"{ds}T{lfcs_time['ics_start']}",
                        "end_dt": f"{ds}T{lfcs_time['ics_end']}",
                        "csv_date": csv_date,
                        "csv_start": lfcs_time["csv_start"],
                        "csv_end": lfcs_time["csv_end"],
                        "desc": format_event_description("LFCS", lfcs_time, day["lfcs_title"], day["lfcs_desc"]),
                        "type": "LFCS"
                    })

                placed += 1

            curr += timedelta(days=1)

    return events


# ── Serializers ───────────────────────────────────────────────────────────
def generate_ics(events: list, output_path: Path, cal_name: str = "CKA & LFCS Study Plan"):
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Antigravity AI//CKA LFCS Schedule Generator//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{cal_name}"
    ]
    now_stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

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

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\r\n".join(lines) + "\r\n")


def generate_csv(events: list, output_path: Path):
    headers = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]
    rows = [",".join(headers)]

    for ev in events:
        safe_desc = '"' + ev['desc'].replace('"', '""') + '"'
        safe_subject = '"' + ev['subject'].replace('"', '""') + '"'
        row = f"{safe_subject},{ev['csv_date']},{ev['csv_start']},{ev['csv_date']},{ev['csv_end']},False,{safe_desc},,False"
        rows.append(row)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(rows) + "\n")


# ── Execution Orchestrator ────────────────────────────────────────────────
def run_generator(start_date: datetime, duration_weeks: int, track: str, pauses: list, output_dir: Path = None, cka_time: dict = None, lfcs_time: dict = None):
    if output_dir is None:
        output_dir = REPO_ROOT
    if cka_time is None:
        cka_time = parse_time_window("", "08:00 AM", "12:00 PM")
    if lfcs_time is None:
        lfcs_time = parse_time_window("", "03:00 PM", "06:00 PM")

    events = build_events(start_date, duration_weeks, track, pauses, cka_time=cka_time, lfcs_time=lfcs_time)
    written_files = []

    track_title = {
        "both": "CKA & LFCS Dual Certification Track",
        "cka": "CKA (Certified Kubernetes Administrator) Study Track",
        "lfcs": "LFCS (Linux Foundation Certified SysAdmin) Study Track"
    }.get(track, "Study Track")

    if track == "both":
        root_ics = output_dir / "cka_lfcs_schedule.ics"
        root_csv = output_dir / "cka_lfcs_schedule.csv"
        generate_ics(events, root_ics, track_title)
        generate_csv(events, root_csv)
        written_files.extend([root_ics, root_csv])

        # Filter and write dedicated track schedules
        cka_evs = [e for e in events if e.get("type") in ("CKA", "REST")]
        cka_ics = output_dir / "cka" / "schedule.ics"
        cka_csv = output_dir / "cka" / "schedule.csv"
        generate_ics(cka_evs, cka_ics, "CKA Certified Kubernetes Administrator Track")
        generate_csv(cka_evs, cka_csv)
        written_files.extend([cka_ics, cka_csv])

        lfcs_evs = [e for e in events if e.get("type") in ("LFCS", "REST")]
        lfcs_ics = output_dir / "lfcs" / "schedule.ics"
        lfcs_csv = output_dir / "lfcs" / "schedule.csv"
        generate_ics(lfcs_evs, lfcs_ics, "LFCS Linux Foundation Certified SysAdmin Track")
        generate_csv(lfcs_evs, lfcs_csv)
        written_files.extend([lfcs_ics, lfcs_csv])

    elif track == "cka":
        cka_ics = output_dir / "cka" / "schedule.ics"
        cka_csv = output_dir / "cka" / "schedule.csv"
        generate_ics(events, cka_ics, track_title)
        generate_csv(events, cka_csv)
        written_files.extend([cka_ics, cka_csv])

    elif track == "lfcs":
        lfcs_ics = output_dir / "lfcs" / "schedule.ics"
        lfcs_csv = output_dir / "lfcs" / "schedule.csv"
        generate_ics(events, lfcs_ics, track_title)
        generate_csv(events, lfcs_csv)
        written_files.extend([lfcs_ics, lfcs_csv])

    # End date calculation
    last_event = events[-1] if events else None
    end_str = last_event["csv_date"] if last_event else "N/A"

    print("══════════════════════════════════════════════════════════════════════")
    print("✅ STUDY SCHEDULE GENERATED SUCCESSFULLY!")
    print("══════════════════════════════════════════════════════════════════════")
    print(f"Certification Track: {track_title}")
    print(f"Start Date:          {start_date.strftime('%A, %B %d, %Y')}")
    print(f"Target Finish:       {end_str}")
    print(f"Duration:            {duration_weeks} Weeks ({len(events)} calendar events)")
    if track in ("both", "cka"):
        print(f"CKA Study Block:     {cka_time['csv_start']} - {cka_time['csv_end']} ({cka_time['label']})")
    if track in ("both", "lfcs"):
        print(f"LFCS Study Block:    {lfcs_time['csv_start']} - {lfcs_time['csv_end']} ({lfcs_time['label']})")
    print()
    print("Exported Files:")
    for f in written_files:
        rel = f.relative_to(output_dir) if output_dir in f.parents or f == output_dir else f
        print(f"  ✓ {rel}")
    print("══════════════════════════════════════════════════════════════════════\n")


def main():
    parser = argparse.ArgumentParser(description="CKA & LFCS Study Calendar Generator")
    parser.add_argument("-s", "--start", "--start-date", dest="start_date", help="Start date (YYYY-MM-DD, 'today', 'tomorrow', 'next monday')")
    parser.add_argument("-w", "--weeks", "--duration", dest="duration_weeks", type=str, help="Duration in weeks (e.g. 8 or 4)")
    parser.add_argument("-t", "--track", choices=["both", "cka", "lfcs"], default=None, help="Certification track")
    parser.add_argument("-p", "--pause", dest="pauses", default="", help="Scheduled pause weeks, comma-separated (e.g. '2,3')")
    parser.add_argument("--cka-time", dest="cka_time", default="", help="Preferred CKA study hours (e.g. '4am to 12pm')")
    parser.add_argument("--lfcs-time", dest="lfcs_time", default="", help="Preferred LFCS study hours (e.g. '6pm to 8pm')")
    parser.add_argument("--time", "--study-time", dest="time_window", default="", help="Preferred daily study hours")
    parser.add_argument("-i", "--interactive", action="store_true", help="Force interactive prompt")
    parser.add_argument("-y", "--yes", "--non-interactive", dest="non_interactive", action="store_true", help="Non-interactive batch mode")

    args = parser.parse_args()

    # Determine if we should prompt interactively
    is_interactive = (sys.stdin.isatty() and not args.non_interactive and not (args.start_date and args.duration_weeks)) or args.interactive

    if is_interactive:
        start_date, duration_weeks, track, pauses, cka_time, lfcs_time = prompt_user_inputs(default_track=args.track)
    else:
        start_date = resolve_start_date(args.start_date or "")
        duration_weeks = resolve_duration(args.duration_weeks or "8")
        track = args.track or "both"
        pauses = resolve_pause_weeks(args.pauses or "")
        cka_val = args.cka_time or (args.time_window if track in ("cka", "both") else "")
        lfcs_val = args.lfcs_time or (args.time_window if track == "lfcs" else "")
        cka_time = parse_time_window(cka_val, "08:00 AM", "12:00 PM")
        lfcs_time = parse_time_window(lfcs_val, "03:00 PM", "06:00 PM")

    run_generator(start_date, duration_weeks, track, pauses, cka_time=cka_time, lfcs_time=lfcs_time)


if __name__ == "__main__":
    main()
