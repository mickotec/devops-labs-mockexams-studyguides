"""
Curriculum Content: Week 3 (Days 1 to 6)
Day 1: Manual Scheduling, Labels & Selectors | Linux Boot Architecture & GRUB2
Day 2: Taints, Tolerations & Node Affinity | Systemd Targets & Runlevel Management
Day 3: Resource Requirements, Limits & LimitRanges | Creating & Managing Systemd Services
Day 4: DaemonSets & Static Pods Architecture | Process Diagnostics & Signal Management
Day 5: Priority Classes & Multiple Schedulers | System Integrity, Resource Monitoring & Top
Day 6: Week 3 Scheduling Troubleshooting Matrix | Week 3 Systemd & Process Orchestration
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    # Day 1: Manual Scheduling & GRUB2
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "MANUAL SCHEDULING: nodeName vs nodeSelector", "Bypassing kube-scheduler vs Constraint Matching", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. DIRECT BINDING: spec.nodeName</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">spec:</text>
    <text x="75" y="155" fill="#4ade80" font-size="8.8" font-family="monospace">  nodeName: node02</text>
    <text x="65" y="175" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Completely bypasses <code>kube-scheduler</code>!</text>
    <text x="65" y="195" fill="#fde047" font-size="8.5" font-family="sans-serif">• Used when scheduler is down or during testing.</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Can be injected into an unassigned pod via Binding API object.</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. LABEL MATCHING: spec.nodeSelector</text>
    <text x="465" y="140" fill="#fde047" font-size="8.8" font-family="monospace">spec:</text>
    <text x="475" y="155" fill="#fde047" font-size="8.8" font-family="monospace">  nodeSelector:</text>
    <text x="485" y="170" fill="#fde047" font-size="8.8" font-family="monospace">    disktype: ssd</text>
    <text x="465" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Labels placed on node: <code>kubectl label node node01 disktype=ssd</code></text>
    <text x="465" y="210" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• Pod stays in <code>Pending</code> if no nodes carry matching label!</text>
    """, "Figure 1.1: Kubernetes Manual Scheduling & Node Selector Architecture")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX BOOT SEQUENCE: UEFI/BIOS TO SYSTEMD PID 1", "Hardware Initialization -> Kernel Boot -> User Space Systemd", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. FIRMWARE</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• UEFI / BIOS</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Power-On Self Test (POST)</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Reads ESP partition or MBR</text>
    <text x="65" y="200" fill="#a7f3d0" font-size="8.5" font-family="monospace">/boot/efi (EFI/)</text>

    <rect x="250" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="340" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. GRUB2 BOOTLOADER</text>
    <text x="265" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <code>/boot/grub/grub.cfg</code></text>
    <text x="265" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Edits in <code>/etc/default/grub</code></text>
    <text x="265" y="180" fill="#fde047" font-size="8.5" font-family="monospace">update-grub</text>
    <text x="265" y="200" fill="#fca5a5" font-size="8.5" font-family="sans-serif">Press 'e' at boot to edit kernel</text>

    <rect x="450" y="90" width="180" height="135" rx="6" fill="#1e293b" stroke="#c084fc"/>
    <text x="540" y="115" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. KERNEL &amp; INITRAMFS</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">vmlinuz-&lt;version&gt;</text>
    <text x="465" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">initrd.img-&lt;version&gt;</text>
    <text x="465" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Loads root disk drivers</text>
    <text x="465" y="200" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Mounts read-only rootfs (/)</text>

    <rect x="650" y="90" width="200" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="750" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">4. SYSTEMD (PID 1)</text>
    <text x="665" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">/sbin/init -> systemd</text>
    <text x="665" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Initializes system targets</text>
    <text x="665" y="180" fill="#34d399" font-size="8.5" font-family="monospace">default.target</text>
    <text x="665" y="200" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">Spawns all daemons in parallel</text>
    """, "Figure 1.2: Linux Boot Architecture: UEFI -> GRUB2 -> Kernel/Initramfs -> Systemd")

    cka_theory = """
    <p>
      In Kubernetes, pods without a scheduler can still be assigned to nodes using <code>spec.nodeName</code>. When using <code>nodeSelector</code>, the pod specifies key-value pairs that must match labels on the target node.
    </p>
    <ul>
      <li>Label node: <code>kubectl label node node01 disk=fast</code></li>
      <li>Remove label: <code>kubectl label node node01 disk-</code></li>
      <li>Direct binding: Setting <code>spec.nodeName: node01</code> schedules immediately without filtering or scoring.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      The Linux boot pipeline moves from hardware initialization to GRUB2, kernel unpacking, initramfs root filesystem mount, and handoff to PID 1 (<code>systemd</code>).
    </p>
    <ul>
      <li>GRUB config template: <code>/etc/default/grub</code> (apply with <code>update-grub</code> or <code>grub2-mkconfig -o /boot/grub2/grub.cfg</code>).</li>
      <li>Emergency root recovery: Append <code>init=/bin/bash</code> or <code>rd.break</code> to kernel parameters in GRUB to bypass root password.</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias klabel='kubectl label node'\nalias kgetn='kubectl get nodes --show-labels'",
        "lfcs_aliases": "alias grubup='sudo update-grub'",
        "checklist": [
            ("CKA", "Can you manually assign a pod to a node bypassing the scheduler?", "Set spec.nodeName: <node> in Pod manifest"),
            ("CKA", "Can you label and filter nodes with nodeSelector?", "kubectl label node <node> env=prod"),
            ("LFCS", "Can you edit GRUB parameters permanently via /etc/default/grub?", "GRUB_CMDLINE_LINUX_DEFAULT and update-grub"),
            ("LFCS", "Can you explain the function of initramfs during early boot?", "Provides disk/storage drivers to mount real root filesystem"),
        ]
    }

def get_day_2():
    # Day 2: Taints, Tolerations & Affinity | Systemd Targets
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "TAINTS, TOLERATIONS & NODE AFFINITY RULES", "Node Repulsion vs Pod Attraction Mechanics", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="235" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">TAINTS &amp; TOLERATIONS (Repulsion)</text>
    <text x="65" y="140" fill="#fca5a5" font-size="8.8" font-family="monospace">k taint node node01 dedicated=gpu:NoSchedule</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <strong>NoSchedule:</strong> Prevents new pods without toleration.</text>
    <text x="65" y="175" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <strong>PreferNoSchedule:</strong> Soft repulsion (scheduler tries to avoid).</text>
    <text x="65" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• <strong>NoExecute:</strong> Evicts existing pods lacking toleration!</text>
    <text x="65" y="210" fill="#fde047" font-size="8" font-family="monospace">tolerations: [{{key: dedicated, operator: Equal, value: gpu, effect: NoSchedule}}]</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">NODE AFFINITY (Attraction)</text>
    <text x="465" y="140" fill="#34d399" font-size="8.8" font-family="monospace">requiredDuringSchedulingIgnoredDuringExecution</text>
    <text x="465" y="155" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">  -> Hard requirement (pod won't schedule without match)</text>
    <text x="465" y="175" fill="#fbbf24" font-size="8.8" font-family="monospace">preferredDuringSchedulingIgnoredDuringExecution</text>
    <text x="465" y="190" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">  -> Soft preference (weighted score from 1 to 100)</text>
    <text x="465" y="210" fill="#a7f3d0" font-size="8" font-family="monospace">matchExpressions: [{{key: zone, operator: In, values: [us-east1, us-east2]}}]</text>
    """, "Figure 2.1: Kubernetes Taints/Tolerations & Node Affinity Decision Matrix")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SYSTEMD TARGETS & RUNLEVEL HIERARCHY", "Target Synchronization & Default Target Management", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">MULTI-USER.TARGET (Runlevel 3)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Standard server console environment</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Networking, storage &amp; multi-user logins</text>
    <text x="65" y="180" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• No graphical display server</text>
    <text x="65" y="205" fill="#4ade80" font-size="8.5" font-family="monospace">systemctl isolate multi-user.target</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">GRAPHICAL.TARGET (Runlevel 5)</text>
    <text x="325" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Extends <code>multi-user.target</code></text>
    <text x="325" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Spawns X11 / Wayland &amp; Display Manager</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl get-default</text>
    <text x="325" y="205" fill="#fde047" font-size="8.5" font-family="monospace">systemctl set-default graphical.target</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="715" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">RESCUE &amp; EMERGENCY TARGETS</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">rescue.target (Runlevel 1)</text>
    <text x="595" y="155" fill="#94a3b8" font-size="8" font-family="sans-serif">Single user root shell, minimal mounts</text>
    <text x="595" y="175" fill="#e2e8f0" font-size="8.5" font-family="monospace">emergency.target</text>
    <text x="595" y="190" fill="#fca5a5" font-size="8" font-family="sans-serif">Read-only root, no services initialized</text>
    <text x="595" y="210" fill="#38bdf8" font-size="8" font-family="monospace">systemctl isolate rescue.target</text>
    """, "Figure 2.2: Systemd Target Dependency Hierarchy & Runlevel Transition")

    cka_theory = """
    <p>
      Taints allow a node to repel a set of pods. Tolerations allow pods to schedule onto nodes with matching taints.
    </p>
    <ul>
      <li>Add taint: <code>kubectl taint nodes node01 key=value:NoSchedule</code></li>
      <li>Remove taint: <code>kubectl taint nodes node01 key:NoSchedule-</code></li>
      <li>Node Affinity: Allows complex boolean matching using operators: <code>In</code>, <code>NotIn</code>, <code>Exists</code>, <code>DoesNotExist</code>, <code>Gt</code>, <code>Lt</code>.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Systemd uses <strong>Targets</strong> (.target units) to group dependencies and bring the system into a desired state, replacing legacy SysV runlevels.
    </p>
    <ul>
      <li>View active target: <code>systemctl get-default</code></li>
      <li>Change default boot target: <code>systemctl set-default multi-user.target</code></li>
      <li>Switch active target immediately: <code>systemctl isolate rescue.target</code></li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias ktaint='kubectl taint node'\nalias kdescnode='kubectl describe node | grep -A5 Taints'",
        "lfcs_aliases": "alias target='systemctl get-default'",
        "checklist": [
            ("CKA", "Can you taint a node with NoSchedule and write a pod toleration?", "kubectl taint node <n> key=val:NoSchedule"),
            ("CKA", "Can you configure requiredDuringScheduling NodeAffinity in pod YAML?", "spec.affinity.nodeAffinity"),
            ("LFCS", "Can you query and set the default systemd target?", "systemctl get-default && systemctl set-default <target>"),
            ("LFCS", "Can you switch the running system to rescue mode?", "systemctl isolate rescue.target"),
        ]
    }

def get_day_3():
    # Day 3: Resource Requirements & Systemd Services
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "KUBERNETES RESOURCE REQUESTS, LIMITS & OOMKILLER", "Guaranteed Allocation vs Ceiling Cap & CFS Throttling", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="235" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">REQUESTS (Guaranteed Scheduling)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">resources:</text>
    <text x="75" y="155" fill="#4ade80" font-size="8.8" font-family="monospace">  requests:</text>
    <text x="85" y="170" fill="#4ade80" font-size="8.8" font-family="monospace">    cpu: "250m"       # 0.25 vCPU cores</text>
    <text x="85" y="185" fill="#4ade80" font-size="8.8" font-family="monospace">    memory: "256Mi"   # 256 Megabytes</text>
    <text x="65" y="205" fill="#e2e8f0" font-size="8" font-family="sans-serif">• Used by <code>kube-scheduler</code> to find nodes with capacity.</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="650" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">LIMITS (Enforced Hard Caps)</text>
    <text x="465" y="140" fill="#fca5a5" font-size="8.8" font-family="monospace">  limits:</text>
    <text x="475" y="155" fill="#fca5a5" font-size="8.8" font-family="monospace">    cpu: "500m"       # Throttled by CFS quota</text>
    <text x="475" y="170" fill="#fca5a5" font-size="8.8" font-family="monospace">    memory: "512Mi"   # OOMKilled if exceeded!</text>
    <text x="465" y="190" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• <strong>CPU Throttling:</strong> Container slowed down, does NOT terminate.</text>
    <text x="465" y="205" fill="#f43f5e" font-size="8.5" font-family="sans-serif">• <strong>Memory Exceeded:</strong> Kernel OOMKiller terminates process (Exit 137)!</text>
    """, "Figure 3.1: Kubernetes Resource Allocation: Requests vs Limits & OOMKiller")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SYSTEMD SERVICE UNIT ARCHITECTURE & LIFECYCLE", "Unit File Layout: [Unit], [Service], [Install]", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">[Unit] SECTION</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">Description=My Custom Daemon</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">After=network.target</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">Wants=redis.service</text>
    <text x="65" y="200" fill="#94a3b8" font-size="8" font-family="sans-serif">Defines metadata and boot ordering</text>

    <rect x="310" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="440" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">[Service] SECTION</text>
    <text x="325" y="138" fill="#4ade80" font-size="8.5" font-family="monospace">Type=simple / forking / oneshot</text>
    <text x="325" y="156" fill="#4ade80" font-size="8.5" font-family="monospace">ExecStart=/usr/local/bin/app</text>
    <text x="325" y="174" fill="#4ade80" font-size="8.5" font-family="monospace">Restart=on-failure</text>
    <text x="325" y="192" fill="#4ade80" font-size="8.5" font-family="monospace">User=appuser</text>
    <text x="325" y="210" fill="#fde047" font-size="8" font-family="monospace">EnvironmentFile=/etc/app.env</text>

    <rect x="590" y="90" width="260" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="720" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">[Install] &amp; SYSTEMCTL</text>
    <text x="605" y="138" fill="#fde047" font-size="8.5" font-family="monospace">WantedBy=multi-user.target</text>
    <text x="605" y="158" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl daemon-reload</text>
    <text x="605" y="176" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl enable --now app</text>
    <text x="605" y="194" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl status app</text>
    <text x="605" y="212" fill="#a7f3d0" font-size="8" font-family="sans-serif">Path: /etc/systemd/system/app.service</text>
    """, "Figure 3.2: Systemd Custom Service Architecture & Management")

    cka_theory = """
    <p>
      Resource configuration prevents noisy neighbor problems and guarantees cluster capacity.
    </p>
    <ul>
      <li><strong>CPU Units:</strong> 1 CPU = 1 AWS vCPU / 1 GCP Core = 1000m (millicores).</li>
      <li><strong>Memory Units:</strong> <code>Mi</code> (Mebibytes: $2^{20}$) vs <code>M</code> (Megabytes: $10^6$). Always use <code>Mi</code> and <code>Gi</code> in Kubernetes!</li>
      <li><strong>LimitRange:</strong> Enforces minimum and maximum resource constraints per container in a namespace.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Creating and debugging custom systemd service files is a prominent LFCS requirement.
    </p>
    <ul>
      <li>Unit locations: <code>/etc/systemd/system/</code> (administrator custom units), <code>/lib/systemd/system/</code> (package-installed).</li>
      <li>After creating or modifying a unit file, you must run <code>systemctl daemon-reload</code>!</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias ktop='kubectl top nodes && kubectl top pods'",
        "lfcs_aliases": "alias sc='systemctl'\nalias scu='systemctl daemon-reload'",
        "checklist": [
            ("CKA", "Can you define requests and limits in a pod and verify QoS class?", "kubectl get pod <name> -o yaml | grep qosClass"),
            ("CKA", "Do you know what exit code 137 indicates?", "Process killed by SIGKILL / OOMKiller"),
            ("LFCS", "Can you create a systemd service from scratch in /etc/systemd/system?", "Create unit file, reload daemon, enable and start"),
            ("LFCS", "Can you restart a failed systemd service and inspect its journal logs?", "systemctl restart <svc> && journalctl -u <svc> -e"),
        ]
    }

def get_day_4():
    # Day 4: DaemonSets & Static Pods | Process Diagnostics & Signals
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "DAEMONSETS VS STATIC PODS SCHEDULING ARCHITECTURE", "Cluster-Wide Node Agents vs Autonomous Local Pods", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">DAEMONSETS (Cluster-Managed)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Exactly one pod per qualifying node</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Automatically tolerates master/control-plane taints</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">apiVersion: apps/v1, kind: DaemonSet</text>
    <text x="65" y="200" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Use cases: CNI plugins (kube-flannel, calico), Fluentbit loggers</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="650" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">STATIC PODS (Kubelet-Managed)</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Managed directly by kubelet from host disk</text>
    <text x="465" y="160" fill="#34d399" font-size="8.5" font-family="monospace">Path: /etc/kubernetes/manifests/</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• No controller needed; self-bootstraps controlplane</text>
    <text x="465" y="200" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• Cannot be managed or deleted by kubectl!</text>
    """, "Figure 4.1: Kubernetes DaemonSet Controller vs Node-Level Static Pods")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "LINUX PROCESS STATES & POSIX SIGNALS", "Process Lifecycle States & Signal Handling Dispatch", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">PROCESS STATES (ps / top)</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">R: Running / Runnable on CPU</text>
    <text x="65" y="158" fill="#e2e8f0" font-size="8.5" font-family="monospace">S: Interruptible Sleep (waiting for event)</text>
    <text x="65" y="176" fill="#fca5a5" font-size="8.5" font-family="monospace">D: Uninterruptible Sleep (I/O wait!)</text>
    <text x="65" y="194" fill="#fbbf24" font-size="8.5" font-family="monospace">Z: Zombie (terminated, uncollected)</text>
    <text x="65" y="212" fill="#e2e8f0" font-size="8.5" font-family="monospace">T: Stopped (SIGSTOP / Ctrl-Z)</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="435" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">KEY POSIX SIGNALS</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">1 (SIGHUP): Reload configuration</text>
    <text x="325" y="158" fill="#fde047" font-size="8.5" font-family="monospace">2 (SIGINT): Interrupt (Ctrl-C)</text>
    <text x="325" y="176" fill="#fde047" font-size="8.5" font-family="monospace">9 (SIGKILL): Force kill (Uncatchable!)</text>
    <text x="325" y="194" fill="#fde047" font-size="8.5" font-family="monospace">15 (SIGTERM): Graceful termination</text>
    <text x="325" y="212" fill="#fde047" font-size="8.5" font-family="monospace">19 (SIGSTOP): Pause process execution</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">COMMAND DISPATCH</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">kill -15 &lt;pid&gt;    # Graceful</text>
    <text x="595" y="158" fill="#4ade80" font-size="8.5" font-family="monospace">kill -9 &lt;pid&gt;     # Immediate kill</text>
    <text x="595" y="176" fill="#4ade80" font-size="8.5" font-family="monospace">pkill -u user nginx</text>
    <text x="595" y="194" fill="#4ade80" font-size="8.5" font-family="monospace">pgrep -l app</text>
    <text x="595" y="212" fill="#38bdf8" font-size="8.5" font-family="monospace">killall -HUP nginx</text>
    """, "Figure 4.2: Linux Process States & Signal Dispatch Architecture")

    cka_theory = """
    <p>
      DaemonSets ensure a copy of an agent runs on every worker node. When new nodes join, the DaemonSet controller automatically adds a pod.
    </p>
    <ul>
      <li>Convert a Deployment YAML to DaemonSet: Change <code>kind: DaemonSet</code> and remove <code>spec.replicas</code> and <code>strategy</code>.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      Managing processes and sending proper signals is foundational to Linux systems engineering.
    </p>
    <ul>
      <li>Always try <code>SIGTERM (15)</code> first to allow the application to flush buffers and close connections cleanly before resorting to <code>SIGKILL (9)</code>.</li>
      <li>Processes in state <code>D</code> (Disk sleep) cannot be killed even with <code>SIGKILL</code> because they are waiting on uninterruptible kernel I/O!</li>
    </ul>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kds='kubectl get ds -o wide'",
        "lfcs_aliases": "alias psig='kill -l'\nalias topmem='ps aux --sort=-%mem | head -n 10'",
        "checklist": [
            ("CKA", "Can you convert a Deployment YAML into a valid DaemonSet YAML?", "Change kind to DaemonSet and remove spec.replicas"),
            ("CKA", "Can you deploy a static pod on a worker node?", "Place manifest in node staticPodPath"),
            ("LFCS", "Can you identify high CPU/memory processes with ps or top?", "ps aux --sort=-%cpu | head"),
            ("LFCS", "Can you send a reload signal (SIGHUP) to a running service?", "kill -HUP <pid> or pkill -HUP <name>"),
        ]
    }

def get_day_5():
    # Day 5: Priority Classes & Top
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "PRIORITY CLASSES & POD PREEMPTION ARCHITECTURE", "Preemption Loop: Evicting Lower-Priority Pods for Critical Workloads", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="235" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">PRIORITYCLASS SPEC</text>
    <text x="65" y="140" fill="#fde047" font-size="8.8" font-family="monospace">apiVersion: scheduling.k8s.io/v1</text>
    <text x="65" y="155" fill="#fde047" font-size="8.8" font-family="monospace">kind: PriorityClass</text>
    <text x="65" y="170" fill="#fde047" font-size="8.8" font-family="monospace">metadata: {{name: high-priority}}</text>
    <text x="65" y="185" fill="#fde047" font-size="8.8" font-family="monospace">value: 1000000</text>
    <text x="65" y="200" fill="#fde047" font-size="8.8" font-family="monospace">preemptionPolicy: PreemptLowerPriority</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="650" y="115" fill="#fb7185" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">PREEMPTION DECISION LOOP</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">1. High-priority pod arrives; node has insufficient CPU/RAM.</text>
    <text x="465" y="160" fill="#fca5a5" font-size="8.5" font-family="sans-serif">2. Scheduler identifies lower-priority pods on the node.</text>
    <text x="465" y="180" fill="#fca5a5" font-size="8.5" font-family="sans-serif">3. Lower-priority pod is evicted (grace period respected).</text>
    <text x="465" y="200" fill="#4ade80" font-size="8.5" font-family="sans-serif">4. High-priority pod binds and transitions to Running!</text>
    """, "Figure 5.1: PriorityClass Preemption Pipeline & Pod Eviction Loop")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "SYSTEM INTEGRITY & RESOURCE MONITORING (TOP / UPTIME)", "Load Average, CPU State Breakdown & Memory Utilization", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">LOAD AVERAGE (1, 5, 15 min)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">load average: 0.85, 1.20, 1.45</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Number of processes running or waiting on CPU / disk I/O.</text>
    <text x="65" y="180" fill="#fde047" font-size="8.5" font-family="sans-serif">• On an 8-core CPU, load &lt; 8.0 means normal capacity.</text>
    <text x="65" y="200" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• If load &gt;&gt; core count, system is saturated (bottlenecked).</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">CPU STATE METRICS (top / mpstat)</text>
    <text x="465" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">us (user): User space application CPU</text>
    <text x="465" y="158" fill="#38bdf8" font-size="8.5" font-family="monospace">sy (system): Kernel syscall overhead</text>
    <text x="465" y="176" fill="#fca5a5" font-size="8.5" font-family="monospace">wa (iowait): Time CPU waits on disk I/O</text>
    <text x="465" y="194" fill="#94a3b8" font-size="8.5" font-family="monospace">id (idle): Free CPU capacity</text>
    <text x="465" y="210" fill="#fbbf24" font-size="8" font-family="sans-serif">High 'wa' indicates disk thrashing or slow I/O subsystem!</text>
    """, "Figure 5.2: Linux Resource Diagnostics: Load Average & CPU Utilization Metrics")

    cka_theory = """
    <p>
      PriorityClasses ensure mission-critical pods schedule even when cluster capacity is exhausted by evicting lower-priority pods.
    </p>
    <ul>
      <li>Set in Pod: <code>spec.priorityClassName: high-priority</code></li>
      <li>System critical priorities: <code>system-cluster-critical</code> and <code>system-node-critical</code> are built-in.</li>
    </ul>
    """

    lfcs_theory = """
    <p>
      System performance diagnostics rely on understanding the load average and CPU states in <code>top</code>, <code>htop</code>, <code>uptime</code>, and <code>vmstat</code>.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kpc='kubectl get priorityclass'",
        "lfcs_aliases": "alias vm='vmstat 1 5'",
        "checklist": [
            ("CKA", "Can you create a PriorityClass and apply it to a pod?", "kubectl create priorityclass && spec.priorityClassName"),
            ("LFCS", "Can you explain load average relative to CPU core count?", "Load >= CPU cores indicates queued processes"),
            ("LFCS", "Can you determine if high load is caused by disk I/O wait?", "Inspect %wa in top or vmstat"),
        ]
    }

def get_day_6():
    # Day 6: Week 3 Scheduling Troubleshooting & Systemd Orchestration
    svg_cka = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 3 SCHEDULING TROUBLESHOOTING MATRIX", "Diagnosis Flowchart for Unschedulable & Pending Pods", "cardDark", "#0f172a", "#38bdf8")}
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">0/N Nodes Fit</text>
    <text x="140" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">Insufficient CPU/RAM</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Node Has Taint</text>
    <text x="350" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">Add Pod Toleration</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">NodeSelector Miss</text>
    <text x="560" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">Label Node Correctly</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Scheduler Dead</text>
    <text x="765" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">Restart Static Pod</text>

    {code_box(50, 160, 800, 65, "Triage Command Sequence:\n1. kubectl describe pod <name> | grep -A 10 Events\n2. kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints\n3. kubectl describe node <name> | grep -A 7 'Allocated resources'")}
    """, "Figure 6.1: Week 3 Scheduling Troubleshooting Decision Flowchart")

    svg_lfcs = wrap_svg(900, 260, f"""
    {card(30, 50, 840, 190, "WEEK 3 SYSTEMD & PROCESS ORCHESTRATION PIPELINE", "Service Dependencies, Cgroups & Resource Throttling", "cardDark", "#0f172a", "#10b981")}
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SYSTEMD CGROUPS</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Resource slices: system.slice, user.slice</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">CPUQuota=50%</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.5" font-family="monospace">MemoryMax=512M</text>
    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">systemd-cgtop</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="435" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEPENDENCY ORDERING</text>
    <text x="325" y="140" fill="#fde047" font-size="8.5" font-family="monospace">After=, Before= (Ordering)</text>
    <text x="325" y="160" fill="#fde047" font-size="8.5" font-family="monospace">Requires= (Hard dependency)</text>
    <text x="325" y="180" fill="#fde047" font-size="8.5" font-family="monospace">Wants= (Soft dependency)</text>
    <text x="325" y="200" fill="#e2e8f0" font-size="8.5" font-family="monospace">systemctl list-dependencies</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="715" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">SERVICE HEALTH TRIAGE</text>
    <text x="595" y="140" fill="#4ade80" font-size="8.5" font-family="monospace">systemctl --failed</text>
    <text x="595" y="160" fill="#4ade80" font-size="8.5" font-family="monospace">systemctl reset-failed</text>
    <text x="595" y="180" fill="#34d399" font-size="8.5" font-family="monospace">journalctl -u app.service -xe</text>
    <text x="595" y="200" fill="#94a3b8" font-size="8" font-family="sans-serif">Full contextual stacktrace analysis</text>
    """, "Figure 6.2: Systemd Process Control, Cgroups & Diagnostic Tooling")

    cka_theory = """
    <p>
      Week 3 consolidation tests scheduling diagnostic agility: solving pod affinity deadlocks, taints without tolerations, and pod resource limits exceeding node capacity.
    </p>
    """

    lfcs_theory = """
    <p>
      Week 3 consolidation synthesizes boot processes, runlevels/targets, unit creation, and process signal management into an integrated administrative toolkit.
    </p>
    """

    return {
        "cka_theory_html": cka_theory,
        "cka_svg": svg_cka,
        "lfcs_theory_html": lfcs_theory,
        "lfcs_svg": svg_lfcs,
        "cka_aliases": "alias kpend='kubectl get pods -A --field-selector=status.phase=Pending'",
        "lfcs_aliases": "alias failed='systemctl --failed'",
        "checklist": [
            ("CKA", "Can you troubleshoot and resolve a pod stuck in Pending due to scheduling constraints?", "kubectl describe pod <name> events analysis"),
            ("LFCS", "Can you list failed systemd services and view their logs?", "systemctl --failed && journalctl -u <svc> -xe"),
            ("LFCS", "Can you inspect real-time cgroup resource consumption?", "systemd-cgtop"),
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
