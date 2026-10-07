#!/usr/bin/env python3
"""
4-Week Intensive CKA & LFCS Study Calendar Generator
 - CKA: 08:00 AM - 12:00 PM
 - Recovery: 12:00 PM - 03:00 PM
 - LFCS: 03:00 PM - 06:00 PM
 - Sundays: REST DAY (no study)
"""

import sys
from datetime import datetime, timedelta

# ── LFCS Domain Breakdown (24 days) ────────────────────────
# Operations & Deployment: 25% = 6 days
# Networking:              25% = 6 days
# Storage:                 20% = 5 days
# Essential Commands:      20% = 5 days
# Users & Groups:          10% = 2 days

LFCS_DAYS = [
    # ── WEEK 1: Operations & Deployment (6 days) ──
    {"week": 1, "day_num": 1, "lfcs_title": "Process Management & System Services",
     "lfcs_desc": "03:00-03:20: ps, top, htop, pgrep, kill, nice, renice\n03:20-04:20: systemctl, service files, journald logs\n04:20-04:35: Break\n04:35-05:35: Lab: create custom systemd service, troubleshoot failed unit\n05:35-06:00: Cheat sheet & review"},
    {"week": 1, "day_num": 2, "lfcs_title": "Job Scheduling (cron, at, systemd timers)",
     "lfcs_desc": "03:00-03:20: crontab syntax, /etc/cron.d, anacron\n03:20-04:20: at, batch, systemd timers (OnCalendar, OnBootSec)\n04:20-04:35: Break\n04:35-05:35: Lab: schedule backups with systemd timer, validate cron jobs\n05:35-06:00: Review & debug common cron issues"},
    {"week": 1, "day_num": 3, "lfcs_title": "Package Management (dnf/yum)",
     "lfcs_desc": "03:00-03:20: dnf/yum install, remove, update, history\n03:20-04:20: Repo config, GPG keys, module streams, dnf repolist\n04:20-04:35: Break\n04:35-05:35: Lab: add repo, install from local RPM, verify package integrity\n05:35-06:00: Troubleshoot dependency conflicts"},
    {"week": 1, "day_num": 4, "lfcs_title": "Kernel Parameters & System Tuning",
     "lfcs_desc": "03:00-03:20: sysctl -a, /etc/sysctl.conf, sysctl.d drop-ins\n03:20-04:20: Persistent vs non-persistent tuning, /proc filesystem\n04:20-04:35: Break\n04:35-05:35: Lab: tune TCP parameters, vm.swappiness, enable IP forwarding\n05:35-06:00: Verify with sysctl -p and /proc/sys/net/ipv4/*"},
    {"week": 1, "day_num": 5, "lfcs_title": "Hardware Recovery & Emergency Mode",
     "lfcs_desc": "03:00-03:20: GRUB2 bootloader, initramfs, kernel panic\n03:20-04:20: Emergency/rescue mode, root password reset, fsck\n04:20-04:35: Break\n04:35-05:35: Lab: reboot into emergency mode, repair /etc/fstab, reset root pw\n05:35-06:00: Review: backup strategies with rsync and tar"},
    {"week": 1, "day_num": 6, "lfcs_title": "SELinux & Container Engines",
     "lfcs_desc": "03:00-03:20: SELinux modes, contexts, booleans, setsebool\n03:20-04:20: Podman/Docker: run, exec, build, podman generate systemd\n04:20-04:35: Break\n04:35-05:35: Lab: run container with custom SELinux label, troubleshoot AVC denials\n05:35-06:00: Week 1 consolidation & practice questions"},

    # ── WEEK 2: Networking (6 days) ──
    {"week": 2, "day_num": 1, "lfcs_title": "IPv4/IPv6 Configuration & Hostname Resolution",
     "lfcs_desc": "03:00-03:20: nmcli, ip addr, /etc/hosts, hostnamectl\n03:20-04:20: Static IP vs DHCP, DNS resolution, resolv.conf, systemd-resolved\n04:20-04:35: Break\n04:35-05:35: Lab: configure static IPv4+IPv6, set hostname, test resolution\n05:35-06:00: Troubleshoot with dig, nslookup, host"},
    {"week": 2, "day_num": 2, "lfcs_title": "Time Synchronization (chrony/NTP)",
     "lfcs_desc": "03:00-03:20: chronyd vs ntpd, /etc/chrony.conf\n03:20-04:20: chronyc sources, time同步, hwclock, timedatectl\n04:20-04:35: Break\n04:35-05:35: Lab: configure chrony server + client, verify drift, force sync\n05:35-06:00: Troubleshoot time skew issues"},
    {"week": 2, "day_num": 3, "lfcs_title": "Network Monitoring & Troubleshooting",
     "lfcs_desc": "03:00-03:20: ss, netstat, ip -s link, ethtool\n03:20-04:20: tcpdump filters, ping, traceroute, mtr, curl/wget diagnostics\n04:20-04:35: Break\n04:35-05:35: Lab: capture traffic on specific port, trace connectivity issues\n05:35-06:00: Review: systematic network troubleshooting methodology"},
    {"week": 2, "day_num": 4, "lfcs_title": "OpenSSH Server & Client Configuration",
     "lfcs_desc": "03:00-03:20: ssh-keygen, ssh-copy-id, agent forwarding\n03:20-04:20: sshd_config hardening: PermitRootLogin, AllowUsers, key-only auth\n04:20-04:35: Break\n04:35-05:35: Lab: harden sshd, set up key-based auth, tunnel (L/R/D), jump host\n05:35-06:00: Verify with ssh -v, audit with sshd -T"},
    {"week": 2, "day_num": 5, "lfcs_title": "Firewall: iptables/nftables & NAT",
     "lfcs_desc": "03:00-03:20: iptables chain/filter/mangle, nftables tables/rulesets\n03:20-04:20: firewalld zones, rich rules, port forwarding, masquerade (SNAT/DNAT)\n04:20-04:35: Break\n04:35-05:35: Lab: create firewall rules, NAT gateway, block/allow specific services\n05:35-06:00: Verify with nft list ruleset, iptables -L -v -n"},
    {"week": 2, "day_num": 6, "lfcs_title": "Static Routing, Bridges, Bonding & Load Balancers",
     "lfcs_desc": "03:00-03:20: ip route add, route persistence, bridge (brctl / ip link add type bridge)\n03:20-04:20: NIC bonding (active-backup, 802.3ad), /etc/nm-dispatcher scripts\n04:20-04:35: Break\n04:35-05:35: Lab: set up bridge for VMs, NIC bonding, static route, nginx reverse proxy\n05:35-06:00: Week 2 consolidation & full networking review"},

    # ── WEEK 3: Storage (5 days) + Essential Commands (1 day) ──
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

    # ── WEEK 4: Essential Commands (4 days) + Users & Groups (2 days) ──
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
     "lfcs_desc": "03:00-03:10: Final exam setup\n03:10-04:25: 20-question rapid-fire LFCS mock (all domains)\n04:25-04:35: Walk break\n04:35-05:30: Final error ledger consolidation\n05:30-06:00: Certification gate review across all LFCS domains"},
]

# ── CKA Domain Breakdown (24 days) ────────────────────────
# Storage:                   10% = 2.5 → 2 days
# Workloads & Scheduling:    15% = 3.6 → 4 days
# Services & Networking:     20% = 4.8 → 5 days
# Cluster Architecture:      25% = 6.0 → 6 days
# Troubleshooting:           30% = 7.2 → 7 days

CKA_DAYS = [
    # ── WEEK 1: Cluster Architecture (3 days) + Workloads (2 days) + Storage (1 day) ──
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

    # ── WEEK 2: Workloads (2 days) + Networking (3 days) + Architecture (1 day) ──
    {"week": 2, "day_num": 1, "cka_title": "Deployments, ReplicaSets & Rollbacks",
     "cka_desc": "08:00-08:20: Deployment/ReplicaSet relationship\n08:20-09:30: Rolling updates, rollout undo, history, scale\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: deployments & rollbacks\n11:15-11:30: Eye rest\n11:30-12:00: Max surge/max unavailable tuning"},
    {"week": 2, "day_num": 2, "cka_title": "ConfigMaps, Secrets & DaemonSets/StatefulSets/Jobs",
     "cka_desc": "08:00-08:20: ConfigMap/Secret creation & injection methods\n08:20-09:30: DaemonSet, StatefulSet, Job, CronJob specs\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: all workload types\n11:15-11:30: Eye rest\n11:30-12:00: Taints, tolerations & node affinity with workloads"},
    {"week": 2, "day_num": 3, "cka_title": "Services: ClusterIP, NodePort, LoadBalancer",
     "cka_desc": "08:00-08:20: Service types and kube-proxy modes\n08:20-09:30: Endpoints, selectors, headless services\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: service creation & troubleshooting\n11:15-11:30: Eye rest\n11:30-12:00: DNS resolution within cluster"},
    {"week": 2, "day_num": 4, "cka_title": "Ingress Controllers & Gateway API",
     "cka_desc": "08:00-08:20: Ingress resource, rules, TLS\n08:20-09:30: Nginx Ingress controller setup, path-based routing\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: Ingress configuration\n11:15-11:30: Eye rest\n11:30-12:00: Gateway API intro & comparison with Ingress"},
    {"week": 2, "day_num": 5, "cka_title": "Network Policies & CNI",
     "cka_desc": "08:00-08:20: NetworkPolicy spec, ingress/egress rules\n08:20-09:30: Default deny, label selectors, CIDR blocks\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: apply & test network policies\n11:15-11:30: Eye rest\n11:30-12:00: CNI overview (Calico, Cilium, Flannel)"},
    {"week": 2, "day_num": 6, "cka_title": "Helm, Kustomize & CRDs/Operators",
     "cka_desc": "08:00-08:20: Helm chart structure, values.yaml, templates\n08:20-09:30: Kustomize bases/overlays, helm install/upgrade/rollback\n09:30-09:45: Break\n09:45-11:15: KodeKloud labs: Helm & Kustomize\n11:15-11:30: Eye rest\n11:30-12:00: CRD creation & operator basics"},

    # ── WEEK 3: Troubleshooting (5 days) + Architecture (1 day) ──
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

    # ── WEEK 4: Troubleshooting (2 days) + Review (4 days) ──
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
     "cka_desc": "08:00-09:30: Review all error notes and weak areas\n09:30-09:45: Break\n09:45-11:00: 10-question speed sprint across all 5 domains\n11:00-12:00: Certification gate review, finalize exam strategy"},
]


def build_events(start_monday_str="2026-09-14"):
    start_monday = datetime.strptime(start_monday_str, "%Y-%m-%d")
    events = []

    # Map each curriculum day to actual dates, skipping Sundays
    curr = start_monday
    study_idx = 0

    # Process all days until we've placed all 24 study days + the trailing Sunday
    placed = 0
    while placed < 24:
        if curr.weekday() == 6:  # Sunday — REST
            events.append({
                "uid": f"rest-{placed}-{curr.strftime('%Y%m%d')}",
                "subject": "[REST] Full Recovery & Memory Consolidation",
                "start_dt": f"{curr.strftime('%Y%m%d')}T080000",
                "end_dt": f"{curr.strftime('%Y%m%d')}T180000",
                "desc": "Complete detachment from code and terminal.\nPhysical movement, outdoor activities, social time, restorative sleep.",
                "type": "REST"
            })
        else:
            cka = CKA_DAYS[placed]
            lfcs = LFCS_DAYS[placed]
            ds = curr.strftime("%Y%m%d")

            # CKA block
            events.append({
                "uid": f"cka-w{cka['week']}d{cka['day_num']}@{ds}",
                "subject": f"[CKA] 8am-12pm: {cka['cka_title']}",
                "start_dt": f"{ds}T080000",
                "end_dt": f"{ds}T120000",
                "desc": f"CKA STUDY BLOCK (8:00 AM - 12:00 PM)\nTopic: {cka['cka_title']}\n\nSchedule:\n{cka['cka_desc']}",
                "type": "CKA"
            })
            # Recovery
            events.append({
                "uid": f"rec-w{placed+1}@{ds}",
                "subject": "[RECOVERY] 12pm-3pm: Cognitive Reset",
                "start_dt": f"{ds}T120000",
                "end_dt": f"{ds}T150000",
                "desc": "COGNITIVE RECOVERY & INTEGRATION\n12:00-01:00 Lunch & screen detachment\n01:00-02:00 Exercise / walk\n02:00-02:45 Power nap or NSDR\n02:45-03:00 Terminal & desk prep for LFCS",
                "type": "RECOVERY"
            })
            # LFCS block
            events.append({
                "uid": f"lfcs-w{lfcs['week']}d{lfcs['day_num']}@{ds}",
                "subject": f"[LFCS] 3pm-6pm: {lfcs['lfcs_title']}",
                "start_dt": f"{ds}T150000",
                "end_dt": f"{ds}T180000",
                "desc": f"LFCS STUDY BLOCK (3:00 PM - 6:00 PM)\nTopic: {lfcs['lfcs_title']}\n\nSchedule:\n{lfcs['lfcs_desc']}",
                "type": "LFCS"
            })
            placed += 1

        curr += timedelta(days=1)

    # Add trailing Sunday if it exists
    if curr.weekday() == 6:
        events.append({
            "uid": f"rest-final-{curr.strftime('%Y%m%d')}",
            "subject": "[REST] Final Sunday — Exam Prep Rest",
            "start_dt": f"{curr.strftime('%Y%m%d')}T080000",
            "end_dt": f"{curr.strftime('%Y%m%d')}T180000",
            "desc": "Complete detachment from code and terminal.\nPhysical movement, outdoor activities, social time, restorative sleep.",
            "type": "REST"
        })

    return events


def generate_ics(events, output_path="cka_lfcs_4week.ics"):
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//StudyPlan//CKA LFCS 4-Week Intensive//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:CKA & LFCS 4-Week Intensive Study Plan"
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
    print(f"Generated: {output_path} ({len(events)} events)")


if __name__ == "__main__":
    start_date = sys.argv[1] if len(sys.argv) > 1 else "2026-09-14"
    print(f"Building 4-Week schedule starting Monday: {start_date}")
    evs = build_events(start_date)
    generate_ics(evs, "cka_lfcs_4week.ics")
