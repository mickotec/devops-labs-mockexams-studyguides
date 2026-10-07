"""
Curriculum Content: Week 1 (Days 1 to 6)
Day 1: K8s Architecture & Container Runtimes | Consoles, Navigation & Docs
Day 2: ETCD Fundamentals & Cluster State Store | Hard & Soft Links
Day 3: Pod Internals & YAML Architecture | Standard Linux File Permissions
Day 4: Multi-Container Pod Patterns & Init Containers | Special Permissions (SUID/SGID/Sticky)
Day 5: Fast Imperative CLI Mastery with Kubectl | Pagers, Vim Mastery & Terminal Editing
Day 6: Week 1 Integration & Speedrun Drill | Week 1 Consolidation & Permission Auditing
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1 SVG CKA
    svg_cka = wrap_svg(900, 310, f"""
    {card(30, 50, 400, 240, "CONTROL PLANE NODE (controlplane)", "Core Cluster Brain", "cardDark", "#38bdf8", "#38bdf8")}
    <rect x="50" y="90" width="160" height="70" rx="6" fill="#0284c7" stroke="#38bdf8"/>
    <text x="130" y="118" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="sans-serif">kube-apiserver</text>
    <text x="130" y="136" fill="#bae6fd" font-size="8.8" text-anchor="middle" font-family="sans-serif">REST API &amp; Auth (:6443)</text>

    <rect x="240" y="90" width="165" height="70" rx="6" fill="#059669" stroke="#34d399"/>
    <text x="322" y="118" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="sans-serif">etcd (Raft KV)</text>
    <text x="322" y="136" fill="#a7f3d0" font-size="8.8" text-anchor="middle" font-family="sans-serif">Cluster State (:2379)</text>

    <rect x="50" y="180" width="160" height="90" rx="6" fill="#7c3aed" stroke="#c084fc"/>
    <text x="130" y="205" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">kube-scheduler</text>
    <text x="130" y="224" fill="#e9d5ff" font-size="8.5" text-anchor="middle" font-family="sans-serif">1. Filter (Predicates)</text>
    <text x="130" y="240" fill="#e9d5ff" font-size="8.5" text-anchor="middle" font-family="sans-serif">2. Score (Priorities)</text>

    <rect x="240" y="180" width="165" height="90" rx="6" fill="#d97706" stroke="#fbbf24"/>
    <text x="322" y="205" fill="#ffffff" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">kube-controller-mgr</text>
    <text x="322" y="224" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="sans-serif">Node, ReplicaSet, Endpoints</text>
    <text x="322" y="240" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="sans-serif">Reconciliation Loops</text>

    {card(470, 50, 400, 240, "WORKER NODE (node01)", "Workload Execution Host", "cardDark", "#10b981", "#34d399")}
    <rect x="495" y="90" width="350" height="50" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="670" y="112" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="sans-serif">kubelet (Node Agent)</text>
    <text x="670" y="128" fill="#bfdbfe" font-size="8.5" text-anchor="middle" font-family="sans-serif">PLEG Loop &amp; Pod Lifecycle Sync</text>

    <rect x="495" y="155" width="350" height="50" rx="6" fill="#0e7490" stroke="#22d3ee"/>
    <text x="670" y="177" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="sans-serif">CRI Runtime (containerd)</text>
    <text x="670" y="193" fill="#a5f3fc" font-size="8.5" text-anchor="middle" font-family="sans-serif">gRPC Socket: /run/containerd/containerd.sock</text>

    <rect x="495" y="220" width="165" height="50" rx="6" fill="#065f46" stroke="#34d399"/>
    <text x="577" y="244" fill="#ffffff" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">App Container</text>
    <text x="577" y="258" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="sans-serif">Target Process</text>

    <rect x="680" y="220" width="165" height="50" rx="6" fill="#065f46" stroke="#34d399"/>
    <text x="762" y="244" fill="#ffffff" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">Pause Container</text>
    <text x="762" y="258" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="sans-serif">Network &amp; IPC NS</text>

    {arrow(210, 125, 238, 125, "arrowGreen", "#34d399", 2, "")}
    {arrow(430, 115, 493, 115, "arrowSky", "#38bdf8", 2, "HTTPS")}
    {arrow(670, 140, 670, 153, "arrowSky", "#38bdf8", 2, "gRPC")}
    {arrow(670, 205, 670, 218, "arrowGreen", "#34d399", 2, "runc")}
    """, "Figure 1.1: Kubernetes Control Plane Architecture & CRI Node Execution Pipeline")

    # Day 1 SVG LFCS
    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 260, 190, "MAN SECTION 1", "User Executables", "cardDark", "#3b82f6", "#60a5fa")}
    <text x="45" y="100" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Commands for normal users</text>
    <text x="45" y="120" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Examples: passwd, ls, cp, tar</text>
    {code_box(45, 145, 230, 75, "man passwd\n# Changes user password\nman 1 ls")}

    {card(320, 50, 260, 190, "MAN SECTION 5", "File Formats & Config", "cardDark", "#10b981", "#34d399")}
    <text x="335" y="100" fill="#e2e8f0" font-size="9" font-family="sans-serif">• System file layouts &amp; columns</text>
    <text x="335" y="120" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Examples: /etc/fstab, crontab</text>
    {code_box(335, 145, 230, 75, "man 5 fstab\n# Explains mount fields\nman 5 passwd")}

    {card(610, 50, 260, 190, "MAN SECTION 8", "System Admin Daemons", "cardDark", "#f59e0b", "#fbbf24")}
    <text x="625" y="100" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Privileged root tools &amp; init</text>
    <text x="625" y="120" fill="#e2e8f0" font-size="9" font-family="sans-serif">• Examples: useradd, fdisk, iptables</text>
    {code_box(625, 145, 230, 75, "man 8 useradd\n# Explains useradd flags\nman 8 fdisk")}
    """, "Figure 1.2: Linux Manual Hierarchy (Sections 1, 5, 8) & Offline Examination Querying")

    cka_theory = """
    <p>
      The Certified Kubernetes Administrator (CKA) exam heavily tests <strong>Cluster Architecture, Installation &amp; Configuration</strong>. Real-world troubleshooting requires mastering how control plane static pods coordinate, how <code>kube-scheduler</code> assigns unscheduled pods, and how the node agent (<code>kubelet</code>) manages container runtimes via the Container Runtime Interface (CRI).
    </p>
    <ul>
      <li><strong>kube-apiserver:</strong> The central REST hub. All reads and mutations pass through Authn, Authz (RBAC/Node), and Admission Control. Only the apiserver connects directly to etcd.</li>
      <li><strong>etcd:</strong> Distributed Raft key-value database storing all cluster state under <code>/registry/</code>. Listens on <code>2379</code> (clients) and <code>2380</code> (peers).</li>
      <li><strong>kube-scheduler:</strong> Watches for pods with empty <code>spec.nodeName</code>. Uses Filter (Predicates) and Score (Priorities) to bind pods to optimal nodes.</li>
      <li><strong>kubelet &amp; Static Pods:</strong> Kubelet scans <code>/etc/kubernetes/manifests</code> via Linux <code>inotify</code>. It launches static pods autonomously and creates read-only Mirror Pods in the API server.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      The Linux Foundation Certified System Administrator (LFCS) exam is conducted in a strictly <strong>air-gapped environment</strong>. Fast offline navigation and man section mastery are vital.
    </p>
    <ul>
      <li><strong>Section 1:</strong> User commands (e.g. <code>passwd</code>, <code>chmod</code>, <code>tar</code>).</li>
      <li><strong>Section 5:</strong> File formats and configurations (e.g. <code>man 5 fstab</code>, <code>man 5 shadow</code>). Always check Section 5 when you forget column syntax!</li>
      <li><strong>Section 8:</strong> System administration tools (e.g. <code>man 8 useradd</code>, <code>man 8 mkfs</code>).</li>
      <li><strong>Directory Stacks:</strong> <code>pushd &lt;dir&gt;</code>, <code>popd</code>, and <code>dirs -v</code> provide a LIFO stack to jump between configuration paths without losing context.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias k='kubectl'\nexport do='--dry-run=client -o yaml'\nexport now='--grace-period=0 --force'",
        "lfcs_aliases": "alias ll='ls -laF --time-style=long-iso'\nman 5 fstab | grep -A5 defaults",
        "checklist": [
            ("CKA", "Can you identify why a static pod is failing on a control plane node?", "crictl ps -a && crictl logs <id>"),
            ("CKA", "Do you understand why kubectl delete pod won't terminate a static pod?", "kubectl delete pod <name> (kubelet recreates it)"),
            ("CKA", "Can you terminate unmanaged containers directly via CRI/containerd?", "sudo ctr -n k8s.io tasks kill <id>"),
            ("LFCS", "Can you query the exact field structure of /etc/fstab without internet?", "man 5 fstab"),
            ("LFCS", "Can you traverse and return from deep directory trees using directory stacks?", "pushd /path && popd"),
            ("LFCS", "Can you extract man documentation non-interactively in shell scripts?", "man <cmd> | col -b | awk ..."),
        ]
    }

def get_day_2():
    # Day 2 SVG CKA: ETCD Quorum & Raft
    svg_cka = wrap_svg(900, 290, f"""
    {card(30, 50, 400, 220, "ETCD CLUSTER QUORUM & RAFT", "Consensus: N/2 + 1 Nodes Required", "cardDark", "#059669", "#34d399")}
    <rect x="50" y="90" width="105" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="102" y="116" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Node 1 (Leader)</text>
    <text x="102" y="134" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">:2379 / :2380</text>

    <rect x="175" y="90" width="105" height="60" rx="6" fill="#064e3b" stroke="#6ee7b7"/>
    <text x="227" y="116" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Node 2 (Follower)</text>
    <text x="227" y="134" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">:2379 / :2380</text>

    <rect x="300" y="90" width="110" height="60" rx="6" fill="#064e3b" stroke="#6ee7b7"/>
    <text x="355" y="116" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Node 3 (Follower)</text>
    <text x="355" y="134" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">:2379 / :2380</text>

    {code_box(50, 165, 360, 90, "Quorum Formula: Q = floor(N/2) + 1\n• 3 nodes -> Quorum = 2 (Tolerates 1 failure)\n• 5 nodes -> Quorum = 3 (Tolerates 2 failures)\nTLS Required: --cacert, --cert, --key")}

    {card(470, 50, 400, 220, "ETCD SNAPSHOT & DISASTER RESTORE", "Point-in-Time Database Backup", "cardDark", "#0284c7", "#38bdf8")}
    <rect x="490" y="90" width="360" height="42" rx="5" fill="#1e293b" stroke="#38bdf8"/>
    <text x="505" y="110" fill="#38bdf8" font-size="9" font-weight="bold" font-family="monospace">1. Save: etcdctl snapshot save /path/backup.db</text>
    <text x="505" y="123" fill="#94a3b8" font-size="7.8" font-family="sans-serif">Requires TLS cert flags pointing to /etc/kubernetes/pki/etcd/</text>

    <rect x="490" y="140" width="360" height="42" rx="5" fill="#1e293b" stroke="#34d399"/>
    <text x="505" y="160" fill="#34d399" font-size="9" font-weight="bold" font-family="monospace">2. Status: etcdctl snapshot status backup.db</text>
    <text x="505" y="173" fill="#94a3b8" font-size="7.8" font-family="sans-serif">Validates integrity, hash, revision, and total keys</text>

    <rect x="490" y="190" width="360" height="65" rx="5" fill="#1e293b" stroke="#f59e0b"/>
    <text x="505" y="210" fill="#fbbf24" font-size="9" font-weight="bold" font-family="monospace">3. Restore: etcdctl snapshot restore backup.db</text>
    <text x="505" y="225" fill="#e2e8f0" font-size="8" font-family="monospace">--data-dir=/var/lib/etcd-restored</text>
    <text x="505" y="240" fill="#94a3b8" font-size="7.8" font-family="sans-serif">Update static pod hostPath in /etc/kubernetes/manifests/etcd.yaml</text>
    """, "Figure 2.1: ETCD Quorum Architecture, TLS Mutual Auth & Snapshot Flow")

    # Day 2 SVG LFCS: Inodes & Links
    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 400, 190, "HARD LINK ARCHITECTURE", "Direct Pointer to Same Inode", "cardDark", "#3b82f6", "#60a5fa")}
    <rect x="50" y="90" width="160" height="45" rx="5" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="130" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">file.txt (Name 1)</text>
    <text x="130" y="125" fill="#93c5fd" font-size="8" text-anchor="middle" font-family="monospace">Points to Inode #84920</text>

    <rect x="250" y="90" width="160" height="45" rx="5" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="330" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">hardlink.txt (Name 2)</text>
    <text x="330" y="125" fill="#93c5fd" font-size="8" text-anchor="middle" font-family="monospace">Points to Inode #84920</text>

    <rect x="150" y="150" width="160" height="70" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="230" y="172" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Inode #84920</text>
    <text x="230" y="190" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="sans-serif">Link Count: 2</text>
    <text x="230" y="206" fill="#ecfdf5" font-size="8" text-anchor="middle" font-family="monospace">Disk Blocks: [B42, B43]</text>

    {arrow(130, 135, 180, 150, "arrowGreen", "#34d399", 2)}
    {arrow(330, 135, 280, 150, "arrowGreen", "#34d399", 2)}

    {card(470, 50, 400, 190, "SYMBOLIC (SOFT) LINK ARCHITECTURE", "Pointer to Target Path", "cardDark", "#f59e0b", "#fbbf24")}
    <rect x="490" y="90" width="170" height="45" rx="5" fill="#78350f" stroke="#fbbf24"/>
    <text x="575" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">symlink.txt</text>
    <text x="575" y="125" fill="#fef3c7" font-size="8" text-anchor="middle" font-family="monospace">Own Inode #91144</text>

    <rect x="680" y="90" width="170" height="45" rx="5" fill="#064e3b" stroke="#34d399"/>
    <text x="765" y="110" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="sans-serif">target.txt</text>
    <text x="765" y="125" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">Target Inode #84920</text>

    <rect x="490" y="150" width="360" height="70" rx="6" fill="#1e293b" stroke="#64748b"/>
    <text x="505" y="172" fill="#38bdf8" font-size="9" font-weight="bold" font-family="monospace">ln -s ../path/target symlink</text>
    <text x="505" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Relative symlinks stay valid across chroot or root moves.</text>
    <text x="505" y="206" fill="#fca5a5" font-size="8" font-family="sans-serif">• If target.txt is deleted, symlink.txt becomes broken (dangling)!</text>
    {arrow(660, 112, 678, 112, "arrowAmber", "#fbbf24", 2, "points to")}
    """, "Figure 2.2: Linux File System Inodes, Hard Links vs Symbolic Link Resolution")

    cka_theory = """
    <p>
      ETCD is Kubernetes' distributed state database. In the CKA exam, tasks testing ETCD health inspection, member list queries, and snapshot backups occur frequently.
    </p>
    <ul>
      <li><strong>TLS Flag Triad:</strong> <code>etcdctl</code> requires three certificate parameters: <code>--cacert</code>, <code>--cert</code>, and <code>--key</code> found in <code>/etc/kubernetes/manifests/etcd.yaml</code>.</li>
      <li><strong>Snapshot Save:</strong> <code>ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 &lt;certs&gt; snapshot save /path/to/backup.db</code></li>
      <li><strong>Quorum:</strong> Needs $Q = \lfloor N/2 \rfloor + 1$ alive members. A 3-node cluster tolerates 1 node failure.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Linux filesystems separate file metadata (Inodes) from directory entries (Names).
    </p>
    <ul>
      <li><strong>Inodes:</strong> Contain permissions, owner, timestamps, and data block pointers, but <em>not the file name</em>!</li>
      <li><strong>Hard Links (<code>ln src dst</code>):</strong> Creates a new directory entry pointing to the <em>same inode</em>. Deleting the source file does not lose data because the inode link count remains $>0$. Cannot span across different filesystems.</li>
      <li><strong>Soft Links (<code>ln -s src dst</code>):</strong> A distinct file containing the pathname to another file. Can span filesystems. Relative paths are essential for portability.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "export ETCDCTL_API=3\nalias etcdctl='etcdctl --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key'",
        "lfcs_aliases": "alias lsl='ls -lhi'\nfind / -samefile /path/to/target 2>/dev/null",
        "checklist": [
            ("CKA", "Can you locate ETCD client certificates in /etc/kubernetes/manifests/etcd.yaml?", "grep -E 'cert-file|key-file|trusted-ca-file' /etc/kubernetes/manifests/etcd.yaml"),
            ("CKA", "Can you save and verify an ETCD snapshot with etcdctl?", "etcdctl snapshot save test.db && etcdctl snapshot status test.db"),
            ("CKA", "Do you know how to query raw keys with prefix in ETCD v3?", "etcdctl get /registry/namespaces --prefix --keys-only"),
            ("LFCS", "Can you identify files sharing the same inode number?", "ls -li file1 file2"),
            ("LFCS", "Can you create a relative symbolic link that won't break if directory is moved?", "ln -sf ../target symlink"),
            ("LFCS", "Can you find all files with hard link count greater than 1?", "find /dir -type f -links +1"),
        ]
    }

def get_day_3():
    # Day 3: Pod Internals & YAML Architecture | Standard Linux File Permissions
    svg_cka = wrap_svg(900, 270, f"""
    {card(30, 50, 840, 200, "POD ANATOMY & SHARED NAMESPACE ARCHITECTURE", "Pause Container holds Network & IPC Namespaces", "cardDark", "#6366f1", "#818cf8")}
    <rect x="50" y="90" width="220" height="140" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-dasharray="4,3"/>
    <text x="160" y="115" fill="#c7d2fe" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">POD BOUNDARY (10.244.1.15)</text>
    <rect x="65" y="130" width="190" height="40" rx="5" fill="#312e81" stroke="#a5b4fc"/>
    <text x="160" y="155" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" font-family="monospace">Pause Container (k8s.gcr.io/pause)</text>
    <text x="160" y="195" fill="#94a3b8" font-size="8.5" text-anchor="middle" font-family="sans-serif">Holds Net, IPC, UTS Namespaces</text>

    <rect x="300" y="90" width="260" height="140" rx="8" fill="#064e3b" stroke="#34d399"/>
    <text x="430" y="115" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Container 1 (Web App)</text>
    <text x="320" y="145" fill="#ffffff" font-size="9" font-family="monospace">Port: 8080</text>
    <text x="320" y="165" fill="#ecfdf5" font-size="8.5" font-family="sans-serif">• Shares localhost with Container 2</text>
    <text x="320" y="185" fill="#ecfdf5" font-size="8.5" font-family="sans-serif">• Mounts shared Volume at /var/log</text>

    <rect x="580" y="90" width="270" height="140" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="715" y="115" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Shared emptyDir Volume</text>
    <text x="600" y="145" fill="#e2e8f0" font-size="9" font-family="monospace">mountPath: /shared-data</text>
    <text x="600" y="165" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Backed by node RAM or disk</text>
    <text x="600" y="185" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Lifetime tied directly to the Pod</text>
    """, "Figure 3.1: Pod Multi-Container Shared Resources, Namespaces & Pause Container")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX FILE PERMISSIONS (OCTAL BITMASK & UMASK)", "Permission Triad: User (Owner) | Group | Others", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">USER (Owner): rwx (4+2+1=7)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">r = 4 (Read: view contents)</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">w = 2 (Write: modify contents)</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">x = 1 (Execute: run / cd into dir)</text>
    <text x="65" y="205" fill="#fde047" font-size="9" font-family="monospace">chmod 755 script.sh</text>

    <rect x="310" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="430" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">GROUP: r-x (4+0+1=5)</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Applies to users in the group</text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">chown owner:group file</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">chgrp devops /var/www</text>
    <text x="325" y="205" fill="#a7f3d0" font-size="9" font-family="monospace">chmod g+w,o-rwx file</text>

    <rect x="570" y="90" width="280" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="710" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">UMASK CALCULATION</text>
    <text x="585" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">Base Files: 666 (rw-rw-rw-)</text>
    <text x="585" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">Base Dirs:  777 (rwxrwxrwx)</text>
    <text x="585" y="180" fill="#fbbf24" font-size="8.5" font-family="monospace">Default Umask 022 -> File: 644, Dir: 755</text>
    <text x="585" y="205" fill="#fca5a5" font-size="8.5" font-family="monospace">Umask 027 -> File: 640, Dir: 750</text>
    """, "Figure 3.2: Linux Standard File Permission Triad, Octal Mapping & Umask Logic")

    cka_theory = """
    <p>
      A <strong>Pod</strong> is the smallest deployable computing unit in Kubernetes. Containers within a Pod share the network namespace (IP address and port space) and storage volumes.
    </p>
    <ul>
      <li><strong>Pause Container:</strong> Creates and holds the network and IPC namespaces. If an application container crashes and restarts, the IP address is preserved.</li>
      <li><strong>Inter-Container Communication:</strong> Containers in the same Pod communicate over <code>localhost</code>. They must not bind to the same network port.</li>
      <li><strong>RestartPolicy:</strong> <code>Always</code> (default for Pods/Deployments), <code>OnFailure</code> (Jobs), <code>Never</code>.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Linux file permissions govern access for Owner, Group, and Other. Permissions are represented symbolically (<code>rwxr-xr-x</code>) or in octal notation (<code>755</code>).
    </p>
    <ul>
      <li><strong>Directory Permissions:</strong> <code>r</code> allows listing files (<code>ls</code>); <code>w</code> allows creating/deleting files inside the directory; <code>x</code> allows traversing into the directory (<code>cd</code>) and accessing inodes.</li>
      <li><strong>Umask:</strong> Subtracts bits from default maximums (666 for regular files, 777 for directories). A umask of <code>027</code> yields <code>640</code> for files and <code>750</code> for directories.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias krun='kubectl run --dry-run=client -o yaml'",
        "lfcs_aliases": "alias perm='stat -c \"%a %n\" *'\numask 027",
        "checklist": [
            ("CKA", "Can you generate a Pod YAML quickly with --dry-run=client -o yaml?", "kubectl run nginx --image=nginx --dry-run=client -o yaml"),
            ("CKA", "Can you configure multi-port pods without port collision?", "Check containerPort uniqueness"),
            ("CKA", "Do you know how to share storage volumes between pod containers?", "spec.volumes emptyDir + volumeMounts"),
            ("LFCS", "Can you calculate octal permissions and apply them with chmod?", "chmod 640 file && stat -c %a file"),
            ("LFCS", "Can you configure umask in /etc/profile or ~/.bashrc?", "umask 027"),
            ("LFCS", "Can you change both owner and group recursively?", "chown -R user:group /target"),
        ]
    }

def get_day_4():
    # Day 4: Multi-Container Pod Patterns & Init Containers | Special Permissions
    svg_cka = wrap_svg(900, 270, f"""
    {card(30, 50, 840, 200, "MULTI-CONTAINER POD DESIGN PATTERNS", "Sidecar, Adapter & Ambassador", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="250" height="140" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="175" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. SIDECAR PATTERN</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Enhances primary container</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Example: Log shipper (Fluentbit)</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Reads log file from emptyDir volume</text>
    <text x="65" y="200" fill="#34d399" font-size="8.5" font-family="monospace">k8s 1.28+: initContainers restartPolicy: Always</text>

    <rect x="325" y="90" width="250" height="140" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="450" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. ADAPTER PATTERN</text>
    <text x="340" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Normalizes output format</text>
    <text x="340" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Example: Metrics converter</text>
    <text x="340" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Converts custom logs to Prometheus</text>
    <text x="340" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">Exposes /metrics on localhost</text>

    <rect x="600" y="90" width="250" height="140" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="725" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. AMBASSADOR PATTERN</text>
    <text x="615" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Proxies external connections</text>
    <text x="615" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Example: Local Redis proxy</text>
    <text x="615" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• App connects to localhost:6379</text>
    <text x="615" y="200" fill="#fef3c7" font-size="8.5" font-family="monospace">Ambassador handles DB cluster routing</text>
    """, "Figure 4.1: Kubernetes Multi-Container Architectural Patterns")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SPECIAL PERMISSIONS: SUID, SGID & STICKY BIT", "Octal 4000, 2000, 1000 Bitmasks", "cardDark", "#0f172a", "#f43f5e")}
    <rect x="50" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="175" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SUID (Set User ID: 4000)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Executes with file owner's privileges</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Example: <code>/usr/bin/passwd</code> (rwsr-xr-x)</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">chmod u+s /path/to/binary</text>
    <text x="65" y="205" fill="#cbd5e1" font-size="8" font-family="sans-serif">Symbol: 's' (or 'S' if owner not executable)</text>

    <rect x="325" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="450" y="115" fill="#fde047" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SGID (Set Group ID: 2000)</text>
    <text x="340" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• On directory: new files inherit dir group</text>
    <text x="340" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Crucial for shared team folders!</text>
    <text x="340" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">chmod g+s /shared/team</text>
    <text x="340" y="205" fill="#cbd5e1" font-size="8" font-family="sans-serif">Octal: <code>chmod 2775 /shared/team</code></text>

    <rect x="600" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="725" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">STICKY BIT (1000)</text>
    <text x="615" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Prevents users from deleting others' files</text>
    <text x="615" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Only file owner or root can remove</text>
    <text x="615" y="180" fill="#34d399" font-size="8.5" font-family="monospace">chmod +t /tmp</text>
    <text x="615" y="205" fill="#cbd5e1" font-size="8" font-family="sans-serif">Representation: <code>drwxrwxrwt</code> (1777)</text>
    """, "Figure 4.2: Linux Special Permissions (SUID, SGID, Sticky Bit) Mechanics")

    cka_theory = """
    <p>
      Multi-container Pods allow tightly coupled helper processes to run alongside the main application.
    </p>
    <ul>
      <li><strong>Init Containers:</strong> Run sequentially to completion before app containers start. If an init container fails, Kubernetes restarts the Pod until it succeeds (unless restartPolicy=Never).</li>
      <li><strong>Sidecar Containers:</strong> Extend or enhance the primary container (e.g. log streaming, synchronization). In Kubernetes 1.28+, native sidecars use <code>initContainers</code> with <code>restartPolicy: Always</code>.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Special permissions extend the standard DAC permissions for specific operational security patterns.
    </p>
    <ul>
      <li><strong>SUID (4000):</strong> Executes as the file owner rather than the calling user (e.g. <code>passwd</code> writing to <code>/etc/shadow</code>).</li>
      <li><strong>SGID (2000):</strong> On files, executes with group privileges. On directories, newly created files automatically inherit the parent directory's group.</li>
      <li><strong>Sticky Bit (1000):</strong> Appended to shared directories like <code>/tmp</code> so users cannot delete or rename each other's files.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias klogs='kubectl logs -f'",
        "lfcs_aliases": "find / -perm -4000 -type f 2>/dev/null # Find SUID binaries",
        "checklist": [
            ("CKA", "Can you write an init container that blocks until a service is available?", "initContainers with curl or nc probe"),
            ("CKA", "Can you stream logs from a sidecar sharing an emptyDir volume?", "kubectl logs -c sidecar"),
            ("LFCS", "Can you configure SGID on a directory for team collaboration?", "chmod 2775 /dir && chgrp team /dir"),
            ("LFCS", "Can you audit all SUID binaries on the filesystem?", "find / -perm -4000 2>/dev/null"),
            ("LFCS", "Can you explain the difference between 's' and 'S' in permission strings?", "'s' means executable bit was set; 'S' means it was not"),
        ]
    }

def get_day_5():
    # Day 5: Fast Imperative CLI Mastery with Kubectl | Pagers & Vim Mastery
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBECTL IMPERATIVE GENERATION WORKFLOW", "Speed Strategy for 100% CKA Exam Completion", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">RESOURCE GENERATION SHORTCUTS</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">k run nginx --image=nginx $do &gt; pod.yaml</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.8" font-family="monospace">k create deploy web --image=nginx --replicas=3 $do &gt; dep.yaml</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.8" font-family="monospace">k expose deploy web --port=80 --target-port=80 $do &gt; svc.yaml</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.8" font-family="monospace">k create cm app-cfg --from-literal=KEY=val $do &gt; cm.yaml</text>

    <rect x="440" y="90" width="410" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="645" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">EXAM SPEED MULTIPLIERS</text>
    <text x="455" y="140" fill="#fde047" font-size="8.8" font-family="monospace">export do='--dry-run=client -o yaml'</text>
    <text x="455" y="160" fill="#fde047" font-size="8.8" font-family="monospace">export now='--force --grace-period=0'</text>
    <text x="455" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Never write YAML from scratch! Always generate baseline.</text>
    <text x="455" y="200" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Switch contexts rapidly: <code>k config set-context --current --namespace=&lt;ns&gt;</code></text>
    """, "Figure 5.1: Kubectl Imperative Object Generation Engine & Exam Execution Shortcuts")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "VIM MODAL ARCHITECTURE & TERMINAL NAVIGATION", "Modes, Motion Vectors & Productivity Shortcuts", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">NORMAL MODE</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">dd: delete line</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">yy / p: yank / paste</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">u / Ctrl-r: undo / redo</text>
    <text x="65" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">/pattern: search</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="340" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">INSERT MODE</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">i: insert before cursor</text>
    <text x="265" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">a: append after cursor</text>
    <text x="265" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">o: open new line below</text>
    <text x="265" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">Esc: return to Normal</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">VISUAL MODE</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">v: character selection</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">V: line selection</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">Ctrl-v: block select</text>
    <text x="465" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">&gt; / &lt;: indent / unindent</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="750" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">COMMAND MODE (:)</text>
    <text x="665" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">:w / :q!: save / quit</text>
    <text x="665" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">:%s/old/new/g: replace</text>
    <text x="665" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">:set tabstop=2 shiftwidth=2 expandtab</text>
    <text x="665" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">:set nu: line numbers</text>
    """, "Figure 5.2: Vim Modal State Architecture & High-Speed Keyboard Navigation")

    cka_theory = """
    <p>
      Time management is the number one failure point in CKA. Candidates who hand-type YAML run out of time. Master imperative generators:
    </p>
    <ul>
      <li>Generate base Pod: <code>kubectl run my-pod --image=nginx --dry-run=client -o yaml > pod.yaml</code></li>
      <li>Generate Service: <code>kubectl expose pod my-pod --port=80 --name=my-svc --dry-run=client -o yaml > svc.yaml</code></li>
      <li>Instant deletion: <code>kubectl delete pod &lt;name&gt; --force --grace-period=0</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Efficient terminal editing using Vim and pager mastery (<code>less</code>) prevents getting bogged down when reviewing config files:
    </p>
    <ul>
      <li>Set YAML formatting in <code>~/.vimrc</code>: <code>set tabstop=2 shiftwidth=2 expandtab</code>.</li>
      <li>In <code>less</code>: <code>/keyword</code> searches forward; <code>?keyword</code> searches backward; <code>n</code> / <code>N</code> cycles matches; <code>G</code> goes to EOF.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias k='kubectl'\nexport do='--dry-run=client -o yaml'\nexport now='--force --grace-period=0'",
        "lfcs_aliases": "echo 'set ts=2 sw=2 et' >> ~/.vimrc",
        "checklist": [
            ("CKA", "Can you generate and edit a Pod YAML in under 30 seconds?", "kubectl run test --image=busybox $do > test.yaml"),
            ("CKA", "Can you change default kubectl namespace permanently for the current context?", "kubectl config set-context --current --namespace=<ns>"),
            ("LFCS", "Can you configure ~/.vimrc for optimal 2-space YAML editing?", "set tabstop=2 shiftwidth=2 expandtab"),
            ("LFCS", "Can you execute search and replace globally across an open file in vim?", ":%s/foo/bar/g"),
        ]
    }

def get_day_6():
    # Day 6: Week 1 Integration & Speedrun Drill | Week 1 Consolidation
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 1 CONTROL PLANE & WORKLOAD TRIAGE PIPELINE", "Incident Diagnosis Decision Tree", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. Pods Pending?</text>
    <text x="140" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">Check kube-scheduler</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. API Server Down?</text>
    <text x="350" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">Check etcd / certs</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. Node NotReady?</text>
    <text x="560" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">Check kubelet status</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. ImagePullBackOff?</text>
    <text x="765" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">Check image name / tag</text>

    {code_box(50, 160, 800, 65, "Fast Triage Flow:\n1. kubectl get nodes -> check Ready state\n2. kubectl get pods -A -o wide -> identify non-Running pods\n3. crictl ps -a & crictl logs <id> -> inspect static pods on controlplane")}
    """, "Figure 6.1: Week 1 Integration: Incident Triage & Root Cause Discovery Flowchart")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 1 CONSOLIDATION & PERMISSION AUDIT FLOW", "Security Verification Matrix", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">AUDIT SUID / SGID</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -perm /6000 -type f</text>
    <text x="65" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Finds all binaries with SUID or SGID</text>
    <text x="65" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">chmod -s /untrusted/binary</text>
    <text x="65" y="205" fill="#fca5a5" font-size="8.5" font-family="sans-serif">Strips special execution privileges</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">AUDIT PERMISSIONS</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">find /dir -perm 777 -type f</text>
    <text x="325" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Locates dangerous world-writable files</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -nouser -o -nogroup</text>
    <text x="325" y="205" fill="#fef3c7" font-size="8.5" font-family="sans-serif">Finds orphaned files from deleted users</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">INODE &amp; LINK INTEGRITY</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -xtype l 2>/dev/null</text>
    <text x="595" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Discovers broken symbolic links</text>
    <text x="595" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">df -i</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Verifies filesystem inode availability</text>
    """, "Figure 6.2: Linux Security & Permission Auditing Framework")

    cka_theory = """
    <p>
      Week 1 consolidation integrates the full control plane stack: diagnosing crashed static pods, fixing API communication, managing pods with init containers, and rapid imperative commands under time pressure.
    </p>
    """

    lfcs_theory = """
    <p>
      Week 1 consolidation synthesizes file hierarchies, inode links, standard and special permissions, umask calculations, and security auditing to ensure total confidence on the Linux CLI.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias k='kubectl'\nalias kgp='kubectl get pods -o wide'",
        "lfcs_aliases": "alias audit_perm='find . -perm /002 -type f'",
        "checklist": [
            ("CKA", "Can you troubleshoot an entire cluster startup failure in under 10 minutes?", "crictl ps -a & journalctl -u kubelet"),
            ("CKA", "Can you build a multi-container pod with shared volume in 3 minutes?", "kubectl run multi-pod with YAML edit"),
            ("LFCS", "Can you audit and remediate world-writable files across a directory tree?", "find /target -perm -002 -exec chmod o-w {} +"),
            ("LFCS", "Can you identify and prune broken symlinks across a filesystem?", "find . -xtype l -delete"),
        ]
    }

def get_day_content(day: int) -> dict:
    dispatch = {
        1: get_day_1,
        2: get_day_2,
        3: get_day_3,
        4: get_day_4,
        5: get_day_5,
        6: get_day_6,
    }
    return dispatch.get(day, get_day_1)()
