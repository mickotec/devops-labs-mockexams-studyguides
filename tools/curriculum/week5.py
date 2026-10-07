"""
Curriculum Content: Week 5 (Days 1 to 6)
Day 1: Node Maintenance: Cordon, Drain & Uncordon | Local User Management & /etc/passwd
Day 2: Cluster Upgrade: Kubeadm Control Plane | Groups, Sudo Privileges & Visudo
Day 3: Cluster Upgrade: Worker Nodes | Profiles, Templates & User Limits
Day 4: ETCD Snapshot Backup & Disaster Recovery | Kernel Runtime Tuning with Sysctl
Day 5: TLS Basics & PKI in Kubernetes | Mandatory Access Control: SELinux & AppArmor
Day 6: Full Disaster Recovery & Upgrade Drill | Security Audit, Quarantine & Recovery
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1: Node Maintenance & User Management
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "NODE MAINTENANCE WORKFLOW: CORDON, DRAIN & UNCORDON", "Safely Evicting Workloads for Host OS Maintenance", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="170" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. CORDON (Mark Unschedulable)</text>
    <text x="65" y="140" fill="#fde047" font-size="8.8" font-family="monospace">kubectl cordon node01</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Node status becomes <code>SchedulingDisabled</code>.</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Existing running pods remain untouched.</text>
    <text x="65" y="200" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• No new pods can be scheduled here.</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="440" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. DRAIN (Eviction API)</text>
    <text x="325" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">kubectl drain node01 \</text>
    <text x="325" y="155" fill="#fca5a5" font-size="8.5" font-family="monospace">  --ignore-daemonsets \</text>
    <text x="325" y="170" fill="#fca5a5" font-size="8.5" font-family="monospace">  --delete-emptydir-data --force</text>
    <text x="325" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Evicts replica pods (rescheduled elsewhere).</text>
    <text x="325" y="205" fill="#fde047" font-size="8" font-family="sans-serif">DaemonSets are ignored; local emptyDir deleted.</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. UNCORDON (Restore)</text>
    <text x="605" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">kubectl uncordon node01</text>
    <text x="605" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Executed after maintenance/reboot completes.</text>
    <text x="605" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Node status returns to <code>Ready</code>.</text>
    <text x="605" y="200" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Scheduler can assign new workloads.</text>
    """, "Figure 1.1: Kubernetes Node Maintenance Lifecycle: Cordon, Drain & Uncordon")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX USER ACCOUNT ARCHITECTURE & /ETC/PASSWD STRUCTURE", "User Identity, Shell Configuration & Password Hashes", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="450" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="275" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">/etc/passwd SEVEN FIELDS COLUMNS</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">micko : x : 1000 : 1000 : Micko Dev :/home/micko : /bin/bash</text>
    <text x="65" y="155" fill="#fde047" font-size="8" font-family="monospace">  1     2    3      4        5           6           7</text>
    <text x="65" y="170" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">1: Username | 2: Password marker ('x') | 3: UID | 4: GID</text>
    <text x="65" y="188" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">5: GECOS (User info) | 6: Home Directory | 7: Login Shell</text>
    <text x="65" y="208" fill="#fca5a5" font-size="8.5" font-family="monospace">/sbin/nologin or /bin/false (Disable login)</text>

    <rect x="520" y="90" width="330" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="685" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">USER MANAGEMENT COMMANDS</text>
    <text x="535" y="140" fill="#fde047" font-size="8.5" font-family="monospace">useradd -m -s /bin/bash -u 1500 bob</text>
    <text x="535" y="158" fill="#fde047" font-size="8.5" font-family="monospace">usermod -aG sudo,docker bob</text>
    <text x="535" y="176" fill="#fde047" font-size="8.5" font-family="monospace">passwd -l bob  # Lock account</text>
    <text x="535" y="194" fill="#fde047" font-size="8.5" font-family="monospace">userdel -r bob # Delete with home</text>
    <text x="535" y="210" fill="#34d399" font-size="8.5" font-family="monospace">chage -l bob   # Password expiry</text>
    """, "Figure 1.2: Linux User Account Architecture & /etc/passwd Structure")

    cka_theory = """
    <p>
      Node maintenance safely removes workloads before applying OS patches, rebooting, or performing hardware upgrades.
    </p>
    <ul>
      <li><code>--ignore-daemonsets</code> is mandatory because DaemonSets cannot be rescheduled onto other nodes.</li>
      <li><code>--delete-emptydir-data</code> is needed if pods use node-local ephemeral storage.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      User administration is governed by <code>/etc/passwd</code>, <code>/etc/shadow</code>, and <code>/etc/default/useradd</code>.
    </p>
    <ul>
      <li>Default skeleton files are copied from <code>/etc/skel</code> when <code>-m</code> is used with <code>useradd</code>.</li>
      <li>To lock an account: <code>usermod -L &lt;user&gt;</code> or <code>passwd -l &lt;user&gt;</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kdrain='kubectl drain --ignore-daemonsets --delete-emptydir-data --force'",
        "lfcs_aliases": "alias ulist='cut -d: -f1,3 /etc/passwd | sort -t: -k2 -n'",
        "checklist": [
            ("CKA", "Can you drain a node safely and uncordon it after maintenance?", "kubectl drain <node> ... && kubectl uncordon <node>"),
            ("LFCS", "Can you create a user with specific UID, home directory, and bash shell?", "useradd -u 1200 -m -s /bin/bash <user>"),
            ("LFCS", "Can you lock a user account and verify its status in /etc/shadow?", "passwd -l <user> && grep <user> /etc/shadow"),
        ]
    }

def get_day_2():
    # Day 2: Kubeadm Control Plane Upgrade & Sudo/Visudo
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBEADM CONTROL PLANE UPGRADE STATE MACHINE", "Step-by-Step Version Upgrade (e.g. 1.30 -> 1.31)", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. UPGRADE KUBEADM</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">apt-mark unhold kubeadm</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">apt install -y kubeadm=1.31.x</text>
    <text x="65" y="176" fill="#4ade80" font-size="8.5" font-family="monospace">apt-mark hold kubeadm</text>
    <text x="65" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">kubeadm version</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="340" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. PLAN &amp; APPLY</text>
    <text x="265" y="140" fill="#fde047" font-size="8.5" font-family="monospace">kubeadm upgrade plan</text>
    <text x="265" y="160" fill="#94a3b8" font-size="8" font-family="sans-serif">Checks component versions</text>
    <text x="265" y="180" fill="#fde047" font-size="8.5" font-family="monospace">sudo kubeadm upgrade \</text>
    <text x="265" y="195" fill="#fde047" font-size="8.5" font-family="monospace">  apply v1.31.x -y</text>
    <text x="265" y="212" fill="#a7f3d0" font-size="8" font-family="sans-serif">Upgrades static pod manifests</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. DRAIN &amp; KUBELET</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">k drain controlplane ...</text>
    <text x="465" y="158" fill="#e2e8f0" font-size="8.5" font-family="monospace">apt-mark unhold kubelet</text>
    <text x="465" y="176" fill="#e2e8f0" font-size="8.5" font-family="monospace">apt install -y kubelet=1.31.x</text>
    <text x="465" y="194" fill="#e2e8f0" font-size="8.5" font-family="monospace">apt-mark hold kubelet</text>
    <text x="465" y="212" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl restart kubelet</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. UNCORDON &amp; VERIFY</text>
    <text x="665" y="140" fill="#34d399" font-size="8.5" font-family="monospace">k uncordon controlplane</text>
    <text x="665" y="160" fill="#34d399" font-size="8.5" font-family="monospace">kubectl get nodes</text>
    <text x="665" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Controlplane shows new version</text>
    <text x="665" y="200" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Status is Ready</text>
    """, "Figure 2.1: Kubeadm Control Plane Upgrade Lifecycle Sequence")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX SUDO PRIVILEGES & /ETC/SUDOERS GRAMMAR", "Privilege Escalation Rules & Visudo Syntax Verification", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SUDOERS SYNTAX (who where=(as_whom) what)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">root    ALL=(ALL:ALL) ALL</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.8" font-family="monospace">%sudo   ALL=(ALL:ALL) ALL</text>
    <text x="65" y="176" fill="#fde047" font-size="8.8" font-family="monospace">alice   ALL=(ALL) NOPASSWD: /bin/systemctl</text>
    <text x="65" y="194" fill="#fde047" font-size="8.8" font-family="monospace">%devops ALL=(root) /usr/bin/apt, /usr/bin/git</text>
    <text x="65" y="210" fill="#e2e8f0" font-size="8" font-family="sans-serif">% prefix indicates group rule</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">VISUDO SAFETY &amp; DROP-INS</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">sudo visudo</text>
    <text x="465" y="158" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Locks file and verifies syntax before saving.</text>
    <text x="465" y="176" fill="#fde047" font-size="8.5" font-family="monospace">sudo visudo -f /etc/sudoers.d/developers</text>
    <text x="465" y="194" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Drop-in files in <code>/etc/sudoers.d/</code> must have <code>0440</code> permissions!</text>
    <text x="465" y="210" fill="#fca5a5" font-size="8" font-family="sans-serif">Never edit /etc/sudoers with raw vim or nano!</text>
    """, "Figure 2.2: Linux Sudoers Privilege Architecture & Visudo Verification")

    cka_theory = """
    <p>
      Kubernetes upgrades must follow the version skew policy: you cannot skip minor versions (e.g. 1.29 to 1.31 is forbidden; you must go 1.29 -> 1.30 -> 1.31).
    </p>
    <ul>
      <li>Upgrade order: Control plane <code>kubeadm</code> -> <code>kubeadm upgrade apply</code> -> <code>kubelet</code>/<code>kubectl</code> -> Worker nodes.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      The <code>sudoers</code> file governs root delegation.
    </p>
    <ul>
      <li>Always use <code>visudo</code> to prevent locking root out with a syntax typo.</li>
      <li>Drop-in files: <code>/etc/sudoers.d/&lt;filename&gt;</code> must not end in <code>~</code> or contain <code>.</code> in some distros, and must be mode <code>0440</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kup='kubeadm upgrade plan'",
        "lfcs_aliases": "alias vs='sudo visudo -f /etc/sudoers.d/custom'",
        "checklist": [
            ("CKA", "Can you upgrade the control plane node using kubeadm?", "kubeadm upgrade plan && kubeadm upgrade apply"),
            ("CKA", "Do you understand why kubelet is unheld and restarted after kubeadm?", "Kubelet manages node containers matching API version"),
            ("LFCS", "Can you configure passwordless sudo for a specific command?", "user ALL=(ALL) NOPASSWD: /path/to/binary in visudo"),
        ]
    }

def get_day_3():
    # Day 3: Worker Node Upgrade & User Limits
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBEADM WORKER NODE UPGRADE SEQUENCE", "Drain -> Upgrade Kubeadm -> kubeadm upgrade node -> Upgrade Kubelet -> Uncordon", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. DRAIN WORKER</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">k drain node01 \</text>
    <text x="65" y="155" fill="#4ade80" font-size="8.5" font-family="monospace">  --ignore-daemonsets \</text>
    <text x="65" y="170" fill="#4ade80" font-size="8.5" font-family="monospace">  --delete-emptydir-data</text>
    <text x="65" y="195" fill="#94a3b8" font-size="8" font-family="sans-serif">Executed from controlplane</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="340" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. UPGRADE KUBEADM</text>
    <text x="265" y="140" fill="#fde047" font-size="8.5" font-family="monospace">ssh node01</text>
    <text x="265" y="158" fill="#fde047" font-size="8.5" font-family="monospace">apt-mark unhold kubeadm</text>
    <text x="265" y="176" fill="#fde047" font-size="8.5" font-family="monospace">apt install kubeadm=v...</text>
    <text x="265" y="194" fill="#fde047" font-size="8.5" font-family="monospace">apt-mark hold kubeadm</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. UPGRADE NODE</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">sudo kubeadm upgrade node</text>
    <text x="465" y="160" fill="#94a3b8" font-size="8" font-family="sans-serif">Note: <code>node</code>, not <code>apply</code>!</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">apt install kubelet=v...</text>
    <text x="465" y="198" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl restart kubelet</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. UNCORDON</text>
    <text x="665" y="140" fill="#34d399" font-size="8.5" font-family="monospace">k uncordon node01</text>
    <text x="665" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Worker rejoins ready pool</text>
    <text x="665" y="180" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Repeat sequentially for remaining nodes</text>
    """, "Figure 3.1: Worker Node Upgrade Execution Pipeline")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "USER RESOURCE LIMITS & PAM CONFIGURATION", "Security Limits: /etc/security/limits.conf & ulimit", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="450" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="275" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">/etc/security/limits.conf COLUMNS</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">domain    type    item         value</text>
    <text x="65" y="158" fill="#fde047" font-size="8.5" font-family="monospace">*         soft    nofile       4096     # File descriptors</text>
    <text x="65" y="174" fill="#fde047" font-size="8.5" font-family="monospace">*         hard    nofile       65535</text>
    <text x="65" y="190" fill="#fde047" font-size="8.5" font-family="monospace">@devops   hard    nproc        1024     # Max processes</text>
    <text x="65" y="206" fill="#fde047" font-size="8.5" font-family="monospace">bob       hard    maxlogins    2        # Max concurrent logins</text>

    <rect x="520" y="90" width="330" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="685" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">ULIMIT SHELL COMMANDS</text>
    <text x="535" y="140" fill="#fde047" font-size="8.5" font-family="monospace">ulimit -a       # View all limits</text>
    <text x="535" y="160" fill="#fde047" font-size="8.5" font-family="monospace">ulimit -n 8192  # Set open file limit</text>
    <text x="535" y="180" fill="#fde047" font-size="8.5" font-family="monospace">ulimit -u 500   # Max user processes</text>
    <text x="535" y="205" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Hard limits can only be raised by root!</text>
    """, "Figure 3.2: Linux Resource Limits & PAM Security Configuration")

    cka_theory = """
    <p>
      Worker nodes run <code>kubeadm upgrade node</code> rather than <code>kubeadm upgrade apply</code>.
    </p>
    """

    lfcs_theory = """
    <p>
      Process and file descriptor limits prevent fork bombs and file table exhaustion.
    </p>
    <ul>
      <li>Soft limits: Can be modified by user up to hard limit.</li>
      <li>Hard limits: Upper ceiling enforceable by PAM.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias knodeup='kubeadm upgrade node'",
        "lfcs_aliases": "alias ulim='ulimit -a'",
        "checklist": [
            ("CKA", "Can you upgrade worker node kubeadm and kubelet sequentially?", "kubeadm upgrade node && restart kubelet"),
            ("LFCS", "Can you configure max open file descriptors in limits.conf?", "nofile in /etc/security/limits.conf"),
        ]
    }

def get_day_4():
    # Day 4: ETCD Backup/Restore & Sysctl
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "ETCD DISASTER RESTORATION SEQUENCE", "Snapshot Restore to New Data Directory & Static Pod Update", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. SAVE &amp; VERIFY</text>
    <text x="65" y="140" fill="#4ade80" font-size="8" font-family="monospace">ETCDCTL_API=3 etcdctl \</text>
    <text x="65" y="152" fill="#4ade80" font-size="8" font-family="monospace">  --cacert=/etc/.../ca.crt \</text>
    <text x="65" y="164" fill="#4ade80" font-size="8" font-family="monospace">  --cert=/etc/.../server.crt \</text>
    <text x="65" y="176" fill="#4ade80" font-size="8" font-family="monospace">  --key=/etc/.../server.key \</text>
    <text x="65" y="188" fill="#4ade80" font-size="8" font-family="monospace">  snapshot save /tmp/etcd-bkp.db</text>
    <text x="65" y="206" fill="#34d399" font-size="8" font-family="monospace">etcdctl snapshot status ...</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. RESTORE TO NEW DIR</text>
    <text x="325" y="140" fill="#fde047" font-size="8" font-family="monospace">ETCDCTL_API=3 etcdctl \</text>
    <text x="325" y="155" fill="#fde047" font-size="8" font-family="monospace">  snapshot restore /tmp/etcd-bkp.db \</text>
    <text x="325" y="170" fill="#fde047" font-size="8" font-family="monospace">  --data-dir=/var/lib/etcd-from-backup</text>
    <text x="325" y="195" fill="#e2e8f0" font-size="8" font-family="sans-serif">Always restore to a new directory!</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. UPDATE ETCD MANIFEST</text>
    <text x="605" y="140" fill="#e2e8f0" font-size="8" font-family="monospace">vim /etc/kubernetes/manifests/etcd.yaml</text>
    <text x="605" y="160" fill="#34d399" font-size="8" font-family="monospace">hostPath: /var/lib/etcd-from-backup</text>
    <text x="605" y="180" fill="#94a3b8" font-size="8" font-family="sans-serif">Kubelet restarts etcd container</text>
    <text x="605" y="205" fill="#4ade80" font-size="8" font-family="monospace">crictl ps | grep etcd</text>
    """, "Figure 4.1: ETCD Disaster Recovery Restore Pipeline")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KERNEL RUNTIME TUNING: SYSCTL & /PROC/SYS", "Modifying Kernel Behaviour in Memory & On Disk", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">RUNTIME INSPECTION (sysctl / proc)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">sysctl -a | grep ip_forward</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">cat /proc/sys/net/ipv4/ip_forward</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">sysctl -w net.ipv4.ip_forward=1</text>
    <text x="65" y="205" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Immediate change (lost on reboot!)</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">PERSISTENCE (/etc/sysctl.d/)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.5" font-family="monospace">echo "net.ipv4.ip_forward = 1" | \</text>
    <text x="465" y="155" fill="#34d399" font-size="8.5" font-family="monospace">  sudo tee /etc/sysctl.d/99-k8s.conf</text>
    <text x="465" y="175" fill="#fde047" font-size="8.5" font-family="monospace">sudo sysctl --system</text>
    <text x="465" y="195" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Reloads all configs from <code>/etc/sysctl.d/</code></text>
    <text x="465" y="210" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Essential prerequisite for Kubernetes node networking!</text>
    """, "Figure 4.2: Linux Kernel Runtime Parameter Tuning via Sysctl")

    cka_theory = """
    <p>
      ETCD backup and restoration is a guaranteed CKA question.
    </p>
    <ul>
      <li>Save: Pass <code>--cacert</code>, <code>--cert</code>, <code>--key</code>, and <code>--endpoints=https://127.0.0.1:2379</code>.</li>
      <li>Restore: Always restore to a fresh <code>--data-dir</code> and update <code>hostPath</code> in <code>/etc/kubernetes/manifests/etcd.yaml</code>.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Kernel parameters tune memory caching, swap aggressiveness (<code>vm.swappiness</code>), and network routing (<code>net.ipv4.ip_forward</code>).
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias etcdstatus='ETCDCTL_API=3 etcdctl snapshot status'",
        "lfcs_aliases": "alias sysreload='sudo sysctl --system'",
        "checklist": [
            ("CKA", "Can you save and restore an ETCD snapshot end-to-end?", "etcdctl snapshot save && restore to data-dir"),
            ("LFCS", "Can you enable IPv4 forwarding permanently with sysctl?", "/etc/sysctl.d/99-ipforward.conf && sysctl --system"),
        ]
    }

def get_day_5():
    # Day 5: TLS & SELinux/AppArmor
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES PKI & CERTIFICATE AUTHORITY ARCHITECTURE", "Root CAs, Server Certificates & Client Credentials", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">K8s ROOT CA</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">/etc/kubernetes/pki/</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">ca.crt &amp; ca.key</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Signs API server, kubelet,</text>
    <text x="65" y="195" fill="#94a3b8" font-size="8.5" font-family="sans-serif">and admin certificates</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="440" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ETCD CA</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">/etc/kubernetes/pki/etcd/</text>
    <text x="325" y="160" fill="#34d399" font-size="8.5" font-family="monospace">ca.crt &amp; ca.key</text>
    <text x="325" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">Independent PKI hierarchy for</text>
    <text x="325" y="195" fill="#94a3b8" font-size="8.5" font-family="sans-serif">etcd peer &amp; client communication</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="720" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">EXPIRY &amp; VERIFICATION</text>
    <text x="605" y="140" fill="#fde047" font-size="8.5" font-family="monospace">kubeadm certs check-expiration</text>
    <text x="605" y="160" fill="#fde047" font-size="8.5" font-family="monospace">openssl x509 -in cert.crt -text</text>
    <text x="605" y="180" fill="#fde047" font-size="8.5" font-family="monospace">kubeadm certs renew all</text>
    <text x="605" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Certificates expire after 1 year</text>
    """, "Figure 5.1: Kubernetes PKI Hierarchy & Certificate Expiry Management")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "MANDATORY ACCESS CONTROL (MAC): SELINUX & APPARMOR", "Enforcing Process Confinement Beyond Standard DAC", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SELINUX CONTEXTS &amp; MODES</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">getenforce / setenforce [Enforcing|Permissive]</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">ls -Z /var/www/html</text>
    <text x="65" y="175" fill="#fde047" font-size="8" font-family="monospace">system_u:object_r:httpd_sys_content_t:s0</text>
    <text x="65" y="195" fill="#38bdf8" font-size="8.5" font-family="monospace">restorecon -Rv /var/www/html</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Config: /etc/selinux/config</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">APPARMOR PROFILES (Ubuntu / Debian)</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">sudo aa-status</text>
    <text x="465" y="160" fill="#fde047" font-size="8.5" font-family="monospace">sudo aa-enforce /etc/apparmor.d/&lt;profile&gt;</text>
    <text x="465" y="180" fill="#fde047" font-size="8.5" font-family="monospace">sudo aa-complain /etc/apparmor.d/&lt;profile&gt;</text>
    <text x="465" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Restricts binaries by file paths and capabilities</text>
    """, "Figure 5.2: Linux Mandatory Access Control: SELinux & AppArmor")

    cka_theory = """
    <p>
      Kubernetes components authenticate using mutually trusted x509 TLS certificates.
    </p>
    <ul>
      <li>Verify expiry: <code>kubeadm certs check-expiration</code></li>
      <li>Renew: <code>kubeadm certs renew all</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Mandatory Access Control (MAC) enforces security rules even if the root user executes the application.
    </p>
    <ul>
      <li>SELinux: Restore correct context labels on modified directories with <code>restorecon -Rv /path</code>.</li>
      <li>AppArmor: Check status with <code>aa-status</code>.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kcerts='kubeadm certs check-expiration'",
        "lfcs_aliases": "alias se='getenforce'",
        "checklist": [
            ("CKA", "Can you verify certificate expiration dates on the control plane?", "kubeadm certs check-expiration"),
            ("LFCS", "Can you check SELinux mode and restore file security contexts?", "getenforce && restorecon -Rv"),
            ("LFCS", "Can you inspect active AppArmor profiles?", "aa-status"),
        ]
    }

def get_day_6():
    # Day 6: Full Disaster Recovery & User Quarantine
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 5 FULL DISASTER RECOVERY PIPELINE", "Catastrophic Control Plane Reconstruction Flow", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. Crash / Loss</text>
    <text x="140" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">ETCD database wiped</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. Snapshot Restore</text>
    <text x="350" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">etcdctl restore --data-dir</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. Manifest Sync</text>
    <text x="560" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">Point to restored dir</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. Cluster Recovers</text>
    <text x="765" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">All Pods resynced</text>

    {code_box(50, 160, 800, 65, "Total Recovery Drill:\n1. Stop kube-apiserver & etcd\n2. Run etcdctl snapshot restore /backup.db --data-dir=/var/lib/etcd-recovered\n3. Update etcd.yaml volume mount to /var/lib/etcd-recovered\n4. Verify kubectl get nodes & kubectl get pods -A")}
    """, "Figure 6.1: Catastrophic Disaster Recovery & Restoration Workflow")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SECURITY AUDIT & USER QUARANTINE FORENSICS PIPELINE", "Isolating Compromised Accounts & Preserving Evidence", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="170" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. QUARANTINE ACCOUNT</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">passwd -l compromised_user</text>
    <text x="65" y="160" fill="#fca5a5" font-size="8.5" font-family="monospace">usermod -s /sbin/nologin user</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Locks password and revokes shell</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">pkill -KILL -u compromised_user</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. FORENSIC AUDIT</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">last -n 20 compromised_user</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">ausearch -ua &lt;uid&gt;</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">find / -user &lt;uid&gt; -mtime -1</text>
    <text x="325" y="205" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Locates recently modified files</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. CRON &amp; ACCESS PURGE</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">crontab -r -u user  # Purge cron</text>
    <text x="595" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">rm -rf /home/user/.ssh</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">sed -i '/user/d' /etc/sudoers</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">System sanitized and quarantined</text>
    """, "Figure 6.2: Linux Security Forensics & User Quarantine Flowchart")

    cka_theory = """
    <p>
      Week 5 consolidation tests complete disaster readiness: full cluster backup, control plane upgrades, worker node upgrades, and rapid restoration after database loss.
    </p>
    """

    lfcs_theory = """
    <p>
      Week 5 consolidation synthesizes user identity, sudo delegation, MAC policies (SELinux/AppArmor), and incident response containment.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias krecov='echo Check ETCD, Kubelet, and PKI'",
        "lfcs_aliases": "alias qlock='passwd -l'",
        "checklist": [
            ("CKA", "Can you recover from a completely deleted etcd data directory?", "etcdctl snapshot restore to new dir"),
            ("LFCS", "Can you terminate all processes and lock out a compromised user in 30 seconds?", "pkill -u <user> && passwd -l <user>"),
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
