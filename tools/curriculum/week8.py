"""
Curriculum Content: Week 8 (Days 1 to 6)
Day 1: Troubleshooting: Control Plane & Applications | Containers & VMs on Linux
Day 2: Troubleshooting: Worker Nodes & Network Failure | Timed Mock Exam 1
Day 3: JSONPath Queries & Lightning Labs 1 & 2 | Timed Mock Exam 2
Day 4: Timed Mock Exam 1 & Step-by-Step Review | Timed Mock Exam 3
Day 5: Timed Mock Exam 2 & 3 Marathon | Timed Mock Exam 4 & Final Speed Marathon
Day 6: Killer.sh Simulator Marathon (Exam Benchmark) | Certification Gate Review & Readiness Audit
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1: Control Plane Troubleshooting & Podman/Containers
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "CONTROL PLANE & APPLICATION TROUBLESHOOTING FLOWCHART", "Systematic Root Cause Discovery for Kubernetes Clusters", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. APISERVER DOWN?</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">crictl ps -a | grep api</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">crictl logs &lt;id&gt;</text>
    <text x="65" y="176" fill="#94a3b8" font-size="8" font-family="sans-serif">Check static manifests:</text>
    <text x="65" y="192" fill="#fde047" font-size="8" font-family="monospace">/etc/kubernetes/manifests/</text>
    <text x="65" y="210" fill="#fca5a5" font-size="8" font-family="sans-serif">Look for typo in flags/paths</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="340" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. ETCD FAILURE?</text>
    <text x="265" y="140" fill="#fde047" font-size="8.5" font-family="monospace">crictl logs &lt;etcd-id&gt;</text>
    <text x="265" y="158" fill="#e2e8f0" font-size="8.5" font-family="monospace">etcdctl endpoint health</text>
    <text x="265" y="176" fill="#fca5a5" font-size="8" font-family="sans-serif">Common traps:</text>
    <text x="265" y="192" fill="#fca5a5" font-size="8" font-family="sans-serif">• Data disk full (df -h)</text>
    <text x="265" y="208" fill="#fca5a5" font-size="8" font-family="sans-serif">• Expired certs in /pki/etcd</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. SCHEDULER / CTRL</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">kubectl get pods -n kube-system</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Leader election error</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Pod pending indefinitely</text>
    <text x="465" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">k describe pod &lt;pending&gt;</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. APP CRASHLOOP</text>
    <text x="665" y="140" fill="#fca5a5" font-size="8.5" font-family="monospace">k logs &lt;pod&gt; --previous</text>
    <text x="665" y="160" fill="#fde047" font-size="8.5" font-family="monospace">k describe pod &lt;pod&gt;</text>
    <text x="665" y="180" fill="#a7f3d0" font-size="8" font-family="sans-serif">• Check Liveness Probe failure</text>
    <text x="665" y="196" fill="#a7f3d0" font-size="8" font-family="sans-serif">• Check Exit Code 137 (OOM)</text>
    <text x="665" y="212" fill="#a7f3d0" font-size="8" font-family="sans-serif">• Check Exit Code 1 / 127</text>
    """, "Figure 1.1: Kubernetes Control Plane & Application Triage Tree")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "CONTAINERS & VIRTUAL MACHINES ON LINUX", "Podman OCI Engine & KVM/QEMU Virtualization Stack", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">PODMAN (Daemonless &amp; Rootless OCI)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">podman run -d --name web -p 8080:80 nginx</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">podman ps -a</text>
    <text x="65" y="176" fill="#4ade80" font-size="8.5" font-family="monospace">podman generate systemd --name web --files</text>
    <text x="65" y="194" fill="#38bdf8" font-size="8.5" font-family="monospace">podman generate kube web > pod.yaml</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Generates systemd units or K8s pod YAML!</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">KVM / QEMU / LIBVIRT</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">virsh list --all</text>
    <text x="465" y="158" fill="#fde047" font-size="8.5" font-family="monospace">virsh start &lt;vm-name&gt;</text>
    <text x="465" y="176" fill="#fde047" font-size="8.5" font-family="monospace">virsh shutdown &lt;vm-name&gt;</text>
    <text x="465" y="194" fill="#fde047" font-size="8.5" font-family="monospace">virsh console &lt;vm-name&gt;</text>
    <text x="465" y="210" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Kernel-based Virtual Machine management</text>
    """, "Figure 1.2: Linux Container Runtimes (Podman) & Virtual Machine Architecture")

    cka_theory = """
    <p>
      Mastering the triage sequence: If <code>kubectl</code> commands hang, check <code>crictl ps -a</code> on the control plane for dead API server or etcd containers. If pods are failing, use <code>kubectl logs &lt;pod&gt; --previous</code>.
    </p>
    """

    lfcs_theory = """
    <p>
      Modern Linux administration features container management via Podman (an OCI daemonless runtime) and virtualization management via <code>virsh</code> (libvirt).
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias klogsp='kubectl logs --previous'",
        "lfcs_aliases": "alias pman='podman'",
        "checklist": [
            ("CKA", "Can you diagnose a dead API server static pod in under 2 minutes?", "crictl ps -a and crictl logs on controlplane"),
            ("LFCS", "Can you run a rootless container with Podman and manage it with systemd?", "podman generate systemd"),
        ]
    }

def get_day_2():
    # Day 2: Worker Node Troubleshooting & Timed Mock Exam 1
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WORKER NODE NOTREADY TROUBLESHOOTING PIPELINE", "Kubelet Daemon -> Container Runtime -> CNI Configuration", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. KUBELET SERVICE</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">systemctl status kubelet</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">journalctl -u kubelet -e</text>
    <text x="65" y="180" fill="#fca5a5" font-size="8" font-family="sans-serif">• Certificate expired?</text>
    <text x="65" y="195" fill="#fca5a5" font-size="8" font-family="sans-serif">• Missing kubelet config.yaml?</text>
    <text x="65" y="210" fill="#34d399" font-size="8.5" font-family="monospace">systemctl restart kubelet</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. CONTAINER RUNTIME</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">systemctl status containerd</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">crictl info</text>
    <text x="325" y="180" fill="#fca5a5" font-size="8" font-family="sans-serif">• Socket unreachable?</text>
    <text x="325" y="195" fill="#e2e8f0" font-size="8" font-family="monospace">/run/containerd/containerd.sock</text>
    <text x="325" y="210" fill="#a7f3d0" font-size="8" font-family="sans-serif">Verify /etc/crictl.yaml</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. CNI PLUGIN NETWORKING</text>
    <text x="605" y="140" fill="#34d399" font-size="8.5" font-family="monospace">ls -la /etc/cni/net.d/</text>
    <text x="605" y="160" fill="#e2e8f0" font-size="8" font-family="sans-serif">• 10-flannel.conflist or calico</text>
    <text x="605" y="180" fill="#fca5a5" font-size="8" font-family="sans-serif">If empty -> NetworkPluginNotReady</text>
    <text x="605" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">kubectl get nodes</text>
    <text x="605" y="214" fill="#38bdf8" font-size="8" font-family="sans-serif">Transitions to Ready!</text>
    """, "Figure 2.1: Worker Node NotReady Diagnosis & Recovery Sequence")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LFCS TIMED MOCK EXAM 1 STRATEGY MATRIX", "Time Budgeting & Systematic Domain Execution Framework", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TIME ALLOCATION</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• 120 Minutes / ~20 Questions</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Target: 5.5 min per question</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="sans-serif">• If stuck > 7 min: Flag &amp; skip!</text>
    <text x="65" y="205" fill="#38bdf8" font-size="8.5" font-family="sans-serif">Save 20 min for end verification.</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">VERIFICATION DRILL</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">systemctl status &lt;svc&gt;</text>
    <text x="325" y="158" fill="#fde047" font-size="8.5" font-family="monospace">mount -a  # Test fstab before reboot!</text>
    <text x="325" y="176" fill="#fde047" font-size="8.5" font-family="monospace">id &lt;user&gt; # Check UID and groups</text>
    <text x="325" y="194" fill="#fde047" font-size="8.5" font-family="monospace">ip -br a  # Check IP assignments</text>
    <text x="325" y="210" fill="#a7f3d0" font-size="8" font-family="sans-serif">Never assume it worked without testing!</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PASSING THRESHOLD</text>
    <text x="605" y="140" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Pass score: ~66%</text>
    <text x="605" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Easy questions: Useradd, cron, links</text>
    <text x="605" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Medium questions: LVM, systemd, tar</text>
    <text x="605" y="205" fill="#34d399" font-size="8.5" font-family="sans-serif">Secure 100% on easy &amp; medium!</text>
    """, "Figure 2.2: LFCS Timed Mock Exam Strategy & Time Budgeting Matrix")

    cka_theory = """
    <p>
      Worker node troubleshooting requires checking: (1) <code>systemctl status kubelet</code>, (2) <code>journalctl -u kubelet -e</code>, (3) <code>containerd</code> socket connectivity, and (4) CNI configuration files in <code>/etc/cni/net.d/</code>.
    </p>
    """

    lfcs_theory = """
    <p>
      Timed mock exams simulate real test conditions: strictly air-gapped, high-tempo, with precise grading requirements.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kj='journalctl -u kubelet -e --no-pager'",
        "lfcs_aliases": "alias timer='echo Mock Exam In Progress'",
        "checklist": [
            ("CKA", "Can you fix a worker node with crashed kubelet and restore Ready state?", "journalctl -u kubelet and fix config.yaml"),
            ("LFCS", "Can you complete a full 5-task administrative drill in under 25 minutes?", "Timed execution"),
        ]
    }

def get_day_3():
    # Day 3: JSONPath Queries & Mock Exam 2
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES JSONPATH QUERY ENGINE", "High-Speed Data Extraction & Custom Column Formatting", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">JSONPATH QUERY SYNTAX</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">k get nodes -o jsonpath='{{.items[*].status.addresses[0].address}}'</text>
    <text x="65" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">k get pods -o jsonpath='{{range .items[*]}}{{.metadata.name}}{{"\\t"}}{{.status.podIP}}{{"\\n"}}{{end}}'</text>
    <text x="65" y="176" fill="#fde047" font-size="8.5" font-family="monospace">k get pv --sort-by=.spec.capacity.storage</text>
    <text x="65" y="194" fill="#38bdf8" font-size="8.5" font-family="monospace">k get nodes -o custom-columns=NAME:.metadata.name,OS:.status.nodeInfo.osImage</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">LIGHTNING LAB SPEED TRICKS</text>
    <text x="465" y="140" fill="#fde047" font-size="8.5" font-family="monospace">jq</text>
    <text x="465" y="158" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• If JSONPath gets complex, pipe to <code>jq</code>:</text>
    <text x="465" y="176" fill="#34d399" font-size="8.5" font-family="monospace">k get pods -o json | jq -r '.items[] | .metadata.name'</text>
    <text x="465" y="196" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Custom columns: <code>-o custom-columns=NAME:.metadata.name</code></text>
    """, "Figure 3.1: Kubernetes JSONPath Query Syntax & Custom Column Parsing")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LFCS TIMED MOCK EXAM 2: STORAGE & FILESYSTEM OPERATIONS", "Rapid Partitioning, LVM Sizing & Mount Configuration", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TASK 1: LVM CREATION</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">pvcreate /dev/sdb1</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">vgcreate web_vg /dev/sdb1</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">lvcreate -L 2G -n web_lv web_vg</text>
    <text x="65" y="200" fill="#4ade80" font-size="8.5" font-family="monospace">mkfs.ext4 /dev/web_vg/web_lv</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TASK 2: PERSISTENT MOUNT</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">mkdir -p /srv/web</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">blkid /dev/web_vg/web_lv</text>
    <text x="325" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">UUID=... /srv/web ext4 defaults 0 2</text>
    <text x="325" y="200" fill="#34d399" font-size="8.5" font-family="monospace">mount -a &amp;&amp; df -h /srv/web</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TASK 3: ONLINE RESIZE</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">lvextend -L +1G /dev/web_vg/web_lv</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">resize2fs /dev/web_vg/web_lv</text>
    <text x="595" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">df -h /srv/web (Verify 3GB!)</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Completed in under 6 minutes!</text>
    """, "Figure 3.2: LFCS Rapid Storage & Filesystem Execution Pipeline")

    cka_theory = """
    <p>
      JSONPath queries extract precise fields without manual parsing.
    </p>
    <ul>
      <li>Print node internal IPs: <code>kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="InternalIP")].address}'</code></li>
      <li>Sort resources: <code>kubectl get pods --sort-by=.metadata.creationTimestamp</code></li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Storage speed drills test fluent execution of LVM partitioning, UUID fstab entries, and filesystem resizing without hesitation.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kips='kubectl get nodes -o jsonpath=\"{.items[*].status.addresses[0].address}\"'",
        "lfcs_aliases": "alias blk='lsblk -f'",
        "checklist": [
            ("CKA", "Can you extract pod names and IPs with JSONPath range loops?", "jsonpath range loop syntax"),
            ("LFCS", "Can you format and mount an LVM partition in fstab in under 4 minutes?", "End-to-end storage speed run"),
        ]
    }

def get_day_4():
    # Day 4: Timed CKA Mock Exam 1 & Timed LFCS Mock Exam 3
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "CKA TIMED MOCK EXAM STRATEGY MATRIX", "17 Questions / 120 Minutes (~7 Minutes per Question)", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">HIGH-VALUE QUESTIONS (First)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Cluster Upgrade (kubeadm): 8-10%</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="sans-serif">• ETCD Backup/Restore: 7-9%</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="sans-serif">• NetworkPolicy: 7%</text>
    <text x="65" y="200" fill="#fde047" font-size="8.5" font-family="sans-serif">Score 30%+ in first 25 minutes!</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TACTICAL EXECUTION</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">alias k='kubectl'</text>
    <text x="325" y="155" fill="#fde047" font-size="8.5" font-family="monospace">export do='--dry-run=client -o yaml'</text>
    <text x="325" y="170" fill="#fde047" font-size="8.5" font-family="monospace">export now='--force --grace-period=0'</text>
    <text x="325" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Switch context command given in question:</text>
    <text x="325" y="205" fill="#38bdf8" font-size="8.5" font-family="monospace">kubectl config use-context &lt;ctx&gt;</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">VERIFICATION HABITS</text>
    <text x="605" y="140" fill="#34d399" font-size="8.5" font-family="monospace">kubectl get ... -n &lt;namespace&gt;</text>
    <text x="605" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Verify pods are Running (not Pending/Crash)</text>
    <text x="605" y="180" fill="#34d399" font-size="8.5" font-family="monospace">kubectl describe ...</text>
    <text x="605" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Double-check resource names!</text>
    """, "Figure 4.1: CKA Exam Execution Strategy & High-Weight Question Order")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LFCS TIMED MOCK EXAM 3: NETWORKING & SECURITY TRIAGE", "Rapid IP Routing, Firewalls, Users & SSH Hardening", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">NETWORKING TRIAGE</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">ip addr add ... dev eth0</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">ip route add default via ...</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">firewall-cmd --add-port=443/tcp --permanent</text>
    <text x="65" y="200" fill="#34d399" font-size="8.5" font-family="monospace">firewall-cmd --reload</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SECURITY DELEGATION</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">visudo -f /etc/sudoers.d/ops</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">chmod 0440 /etc/sudoers.d/ops</text>
    <text x="325" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">chmod 2775 /shared/dev</text>
    <text x="325" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">restorecon -Rv /var/www</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SERVICE ORCHESTRATION</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">systemctl daemon-reload</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">systemctl enable --now myapp</text>
    <text x="595" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">systemctl is-active myapp</text>
    <text x="595" y="205" fill="#4ade80" font-size="8.5" font-family="sans-serif">All tasks verified active!</text>
    """, "Figure 4.2: LFCS Networking & Security Triage Workflow")

    cka_theory = """
    <p>
      Mock Exam 1 establishes exam rhythm: always copy the <code>kubectl config use-context</code> line first, use imperative commands with <code>$do</code>, and verify resource names and namespaces.
    </p>
    """

    lfcs_theory = """
    <p>
      Mock Exam 3 tests rapid response across networking, sudo permissions, systemd service creation, and security hardening.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kctx='kubectl config get-contexts'",
        "lfcs_aliases": "alias chk='systemctl is-active'",
        "checklist": [
            ("CKA", "Can you complete a full 17-question mock simulation in under 110 minutes?", "Strict timed conditions"),
            ("LFCS", "Can you complete Mock Exam 3 with zero syntax errors in sudoers or fstab?", "Tested with visudo and mount -a"),
        ]
    }

def get_day_5():
    # Day 5: Timed Mock Exam Marathons
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "MULTI-CLUSTER CONTEXT SWITCHING ARCHITECTURE", "Navigating 4-6 Independent Exam Clusters via KubeConfig", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="235" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">⚠️ #1 CKA EXAM FAILURE TRAP</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.5" font-family="sans-serif">Working in the WRONG cluster context gives 0 marks!</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">Every question begins with an explicit context command:</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="monospace">kubectl config use-context k8s-prod</text>
    <text x="65" y="205" fill="#4ade80" font-size="8.5" font-family="sans-serif">Always execute this command FIRST before reading the task!</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">MULTI-CLUSTER ARCHITECTURE</text>
    <text x="465" y="140" fill="#38bdf8" font-size="8.5" font-family="monospace">cluster1: k8s (Main multi-node cluster)</text>
    <text x="465" y="158" fill="#38bdf8" font-size="8.5" font-family="monospace">cluster2: hk8s (High-availability control plane)</text>
    <text x="465" y="176" fill="#38bdf8" font-size="8.5" font-family="monospace">cluster3: bk8s (Storage / backup cluster)</text>
    <text x="465" y="194" fill="#38bdf8" font-size="8.5" font-family="monospace">cluster4: wk8s (Worker node upgrade cluster)</text>
    <text x="465" y="210" fill="#a7f3d0" font-size="8" font-family="sans-serif">KubeConfig maps all clusters, users, and contexts cleanly.</text>
    """, "Figure 5.1: Multi-Cluster Context Switching Architecture & Failure Traps")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LFCS FINAL SPEED MARATHON TACTICS", "Rapid Automation, Text Processing & System Triage", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">TEXT EXTRACTION</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">awk -F: '$3>=1000 {{print $1}}'</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">sed -i '/DEBUG/d' file.log</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">grep -oE '[0-9]+\.[0-9]+...'</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">sort -n | uniq -c</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">STORAGE &amp; ARCHIVE</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">tar -czf /bkp/data.tar.gz /dir</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">lvextend -r -L +2G /dev/vg/lv</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">swapon /dev/sdb3</text>
    <text x="325" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">find / -size +100M</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SECURITY &amp; SYSTEMD</text>
    <text x="595" y="140" fill="#34d399" font-size="8.5" font-family="monospace">chmod 2775 /shared</text>
    <text x="595" y="160" fill="#34d399" font-size="8.5" font-family="monospace">systemctl isolate rescue</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">journalctl -u app -p err</text>
    <text x="595" y="205" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Full domain mastery verified!</text>
    """, "Figure 5.2: LFCS Final Speed Marathon Tactics Across All 5 Exam Domains")

    cka_theory = """
    <p>
      Multi-cluster exam strategy: Always check the active context with <code>kubectl config current-context</code> before modifying resources.
    </p>
    """

    lfcs_theory = """
    <p>
      The final speed marathon reinforces rapid terminal instincts across text parsing, storage, security, and process management.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kctx='kubectl config current-context'",
        "lfcs_aliases": "alias fast='echo Speed Marathon Ready'",
        "checklist": [
            ("CKA", "Do you consistently run the context switch command at the start of every question?", "kubectl config use-context <ctx>"),
            ("LFCS", "Can you solve any standard LFCS question in under 4 minutes?", "Motor skill fluency"),
        ]
    }

def get_day_6():
    # Day 6: Killer.sh Simulator Benchmark & Certification Gate Review
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KILLER.SH SIMULATOR BENCHMARK & FINAL CKA CERTIFICATION GATE", "Calibrated for 120%+ Exam Difficulty to Ensure a Confident Pass", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">DIAGNOSTIC RIGOR</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• 25 Extremely Difficult Scenarios</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="sans-serif">• Harder than real CKA exam!</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="sans-serif">• Score Target: &gt; 80%</text>
    <text x="65" y="200" fill="#34d399" font-size="8.5" font-family="sans-serif">Guarantees real exam passing (>66%)</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="440" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">CORE EXAM DOMAINS</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="sans-serif">1. Storage: 10%</text>
    <text x="325" y="156" fill="#fde047" font-size="8.5" font-family="sans-serif">2. Troubleshooting: 30%</text>
    <text x="325" y="172" fill="#fde047" font-size="8.5" font-family="sans-serif">3. Workloads &amp; Scheduling: 15%</text>
    <text x="325" y="188" fill="#fde047" font-size="8.5" font-family="sans-serif">4. Cluster Architecture &amp; Install: 25%</text>
    <text x="325" y="204" fill="#fde047" font-size="8.5" font-family="sans-serif">5. Services &amp; Networking: 20%</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="720" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">FINAL READINESS GATE</text>
    <text x="605" y="140" fill="#4ade80" font-size="9" font-weight="bold" font-family="sans-serif">✓ All 8 Weeks Completed</text>
    <text x="605" y="160" fill="#4ade80" font-size="9" font-weight="bold" font-family="sans-serif">✓ 48 CKA Labs Passed</text>
    <text x="605" y="180" fill="#4ade80" font-size="9" font-weight="bold" font-family="sans-serif">✓ Speed Drills Mastered</text>
    <text x="605" y="205" fill="#38bdf8" font-size="10" font-weight="bold" font-family="sans-serif">CERTIFICATION READY!</text>
    """, "Figure 6.1: Killer.sh Benchmark Topology & Final CKA Readiness Gate")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LFCS CERTIFICATION GATE REVIEW & DOMAIN READINESS AUDIT", "Comprehensive Competency Map Across All 5 Linux Domains", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. ESSENTIAL CMDS (25%)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Navigation, inodes, links</text>
    <text x="65" y="158" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Permissions &amp; special bits</text>
    <text x="65" y="176" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Tar, gzip, bzip2, xz</text>
    <text x="65" y="194" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Find, grep, sed, awk</text>
    <text x="65" y="210" fill="#4ade80" font-size="8.5" font-weight="bold" font-family="sans-serif">100% Mastered</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="340" y="115" fill="#fbbf24" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. OPERATION (20%)</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• GRUB2 &amp; boot sequence</text>
    <text x="265" y="158" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Systemd units &amp; targets</text>
    <text x="265" y="176" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Journald logging</text>
    <text x="265" y="194" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Cron &amp; at task queues</text>
    <text x="265" y="210" fill="#4ade80" font-size="8.5" font-weight="bold" font-family="sans-serif">100% Mastered</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. USER &amp; SEC (15%)</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• /etc/passwd &amp; shadow</text>
    <text x="465" y="158" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Visudo &amp; sudo privileges</text>
    <text x="465" y="176" fill="#e2e8f0" font-size="8" font-family="sans-serif">• User limits &amp; PAM</text>
    <text x="465" y="194" fill="#e2e8f0" font-size="8" font-family="sans-serif">• SELinux &amp; AppArmor</text>
    <text x="465" y="210" fill="#4ade80" font-size="8.5" font-weight="bold" font-family="sans-serif">100% Mastered</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="10.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. STORAGE &amp; NET (40%)</text>
    <text x="665" y="140" fill="#e2e8f0" font-size="8" font-family="sans-serif">• MBR / GPT / Swap</text>
    <text x="665" y="155" fill="#e2e8f0" font-size="8" font-family="sans-serif">• LVM creation &amp; resize</text>
    <text x="665" y="170" fill="#e2e8f0" font-size="8" font-family="sans-serif">• /etc/fstab &amp; NFS</text>
    <text x="665" y="185" fill="#e2e8f0" font-size="8" font-family="sans-serif">• IP, routing, firewalld</text>
    <text x="665" y="200" fill="#34d399" font-size="10" font-weight="bold" font-family="sans-serif">CERTIFICATION READY!</text>
    """, "Figure 6.2: LFCS 5-Domain Final Certification Readiness Audit")

    cka_theory = """
    <p>
      Congratulations on completing the entire 8-week curriculum! The Killer.sh simulator is calibrated 20-30% harder than the actual CKA exam. Scoring 75-80% on Killer.sh guarantees an easy pass on the official exam.
    </p>
    """

    lfcs_theory = """
    <p>
      All 5 LFCS exam domains have been thoroughly drilled with hands-on lab automation, speed drills, and rigorous verification. You are fully prepared to pass the LFCS exam on your first attempt!
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kpass='echo Congratulations CKA Certified!'",
        "lfcs_aliases": "alias lfpass='echo Congratulations LFCS Certified!'",
        "checklist": [
            ("CKA", "Have you cleared all 8 weeks of CKA labs and killer.sh simulation?", "Full curriculum completed"),
            ("LFCS", "Have you cleared all 8 weeks of LFCS labs and mock marathons?", "Full curriculum completed"),
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
