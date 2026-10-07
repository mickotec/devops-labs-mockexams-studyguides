"""
CKA Curriculum Content: Week 5 (Days 1 to 6)
Day 1: Node Maintenance: Cordon, Drain & Uncordon
Day 2: Cluster Upgrade: Kubeadm Control Plane
Day 3: Cluster Upgrade: Worker Nodes
Day 4: ETCD Snapshot Backup & Disaster Recovery
Day 5: TLS Basics & PKI in Kubernetes
Day 6: Full Disaster Recovery & Upgrade Drill
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      Node maintenance safely removes workloads before applying OS patches, rebooting, or performing hardware upgrades.
    </p>
    <ul>
      <li><code>--ignore-daemonsets</code> is mandatory because DaemonSets cannot be rescheduled onto other nodes.</li>
      <li><code>--delete-emptydir-data</code> is needed if pods use node-local ephemeral storage.</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.1: Kubernetes Node Maintenance Lifecycle: Cordon, Drain & Uncordon</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">NODE MAINTENANCE WORKFLOW: CORDON, DRAIN & UNCORDON</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Safely Evicting Workloads for Host OS Maintenance</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias kdrain='kubectl drain --ignore-daemonsets --delete-emptydir-data --force'"""
    checklist = [('CKA', 'Can you drain a node safely and uncordon it after maintenance?', 'kubectl drain <node> ... && kubectl uncordon <node>')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_2():
    theory = """
    <p>
      Kubernetes upgrades must follow the version skew policy: you cannot skip minor versions (e.g. 1.29 to 1.31 is forbidden; you must go 1.29 -> 1.30 -> 1.31).
    </p>
    <ul>
      <li>Upgrade order: Control plane <code>kubeadm</code> -> <code>kubeadm upgrade apply</code> -> <code>kubelet</code>/<code>kubectl</code> -> Worker nodes.</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.1: Kubeadm Control Plane Upgrade Lifecycle Sequence</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBEADM CONTROL PLANE UPGRADE STATE MACHINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Step-by-Step Version Upgrade (e.g. 1.30 -> 1.31)</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias kup='kubeadm upgrade plan'"""
    checklist = [('CKA', 'Can you upgrade the control plane node using kubeadm?', 'kubeadm upgrade plan && kubeadm upgrade apply'), ('CKA', 'Do you understand why kubelet is unheld and restarted after kubeadm?', 'Kubelet manages node containers matching API version')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_3():
    theory = """
    <p>
      Worker nodes run <code>kubeadm upgrade node</code> rather than <code>kubeadm upgrade apply</code>.
    </p>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.1: Worker Node Upgrade Execution Pipeline</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBEADM WORKER NODE UPGRADE SEQUENCE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Drain -> Upgrade Kubeadm -> kubeadm upgrade node -> Upgrade Kubelet -> Uncordon</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias knodeup='kubeadm upgrade node'"""
    checklist = [('CKA', 'Can you upgrade worker node kubeadm and kubelet sequentially?', 'kubeadm upgrade node && restart kubelet')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_4():
    theory = """
    <p>
      ETCD backup and restoration is a guaranteed CKA question.
    </p>
    <ul>
      <li>Save: Pass <code>--cacert</code>, <code>--cert</code>, <code>--key</code>, and <code>--endpoints=https://127.0.0.1:2379</code>.</li>
      <li>Restore: Always restore to a fresh <code>--data-dir</code> and update <code>hostPath</code> in <code>/etc/kubernetes/manifests/etcd.yaml</code>.</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.1: ETCD Disaster Recovery Restore Pipeline</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">ETCD DISASTER RESTORATION SEQUENCE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Snapshot Restore to New Data Directory & Static Pod Update</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias etcdstatus='ETCDCTL_API=3 etcdctl snapshot status'"""
    checklist = [('CKA', 'Can you save and restore an ETCD snapshot end-to-end?', 'etcdctl snapshot save && restore to data-dir')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_5():
    theory = """
    <p>
      Kubernetes components authenticate using mutually trusted x509 TLS certificates.
    </p>
    <ul>
      <li>Verify expiry: <code>kubeadm certs check-expiration</code></li>
      <li>Renew: <code>kubeadm certs renew all</code></li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.1: Kubernetes PKI Hierarchy & Certificate Expiry Management</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBERNETES PKI & CERTIFICATE AUTHORITY ARCHITECTURE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Root CAs, Server Certificates & Client Credentials</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias kcerts='kubeadm certs check-expiration'"""
    checklist = [('CKA', 'Can you verify certificate expiration dates on the control plane?', 'kubeadm certs check-expiration')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
    }

def get_day_6():
    theory = """
    <p>
      Week 5 consolidation tests complete disaster readiness: full cluster backup, control plane upgrades, worker node upgrades, and rapid restoration after database loss.
    </p>
    """
    svg = """<svg viewBox="0 0 900 260" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.1: Catastrophic Disaster Recovery & Restoration Workflow</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">WEEK 5 FULL DISASTER RECOVERY PIPELINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Catastrophic Control Plane Reconstruction Flow</text>
    </g>
    
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

    
    <rect x="50" y="160" width="800" height="65" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="60" y="176" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">Total Recovery Drill:</text><text x="60" y="190" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">1. Stop kube-apiserver & etcd</text><text x="60" y="204" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">2. Run etcdctl snapshot restore /backup.db --data-dir=/var/lib/etcd-recovered</text><text x="60" y="218" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">3. Update etcd.yaml volume mount to /var/lib/etcd-recovered</text><text x="60" y="232" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">4. Verify kubectl get nodes & kubectl get pods -A</text>
    
    
</svg>"""
    aliases = """alias krecov='echo Check ETCD, Kubelet, and PKI'"""
    checklist = [('CKA', 'Can you recover from a completely deleted etcd data directory?', 'etcdctl snapshot restore to new dir')]
    return {
        "theory_html": theory,
        "svg": svg,
        "aliases": aliases,
        "checklist": checklist,
        "cka_theory_html": theory,
        "cka_svg": svg,
        "cka_aliases": aliases,
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
