"""
CKA Curriculum Content: Week 1 (Days 1 to 6)
Day 1: K8s Architecture & Container Runtimes
Day 2: ETCD Fundamentals & Cluster State Store
Day 3: Pod Internals & YAML Architecture
Day 4: Multi-Container Pod Patterns & Init Containers
Day 5: Fast Imperative CLI Mastery with Kubectl
Day 6: Week 1 Integration & Speedrun Drill
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
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
    svg = """<svg viewBox="0 0 900 310" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
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
  <rect x="0" y="0" width="900" height="310" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.1: Kubernetes Control Plane Architecture & CRI Node Execution Pipeline</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="400" height="240" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="30" y="50" width="400" height="28" rx="9" fill="#38bdf8" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">CONTROL PLANE NODE (controlplane)</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Core Cluster Brain</text>
    </g>
    
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

    
    <g filter="url(#shadow)">
      <rect x="470" y="50" width="400" height="240" rx="9" fill="url(#cardDark)" stroke="#10b981" stroke-width="1.5"/>
      <rect x="470" y="50" width="400" height="28" rx="9" fill="#10b981" opacity="0.18"/>
      <text x="484" y="70" fill="#34d399" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">WORKER NODE (node01)</text>
      <text x="484" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Workload Execution Host</text>
    </g>
    
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

    
    <line x1="210" y1="125" x2="238" y2="125" stroke="#34d399" stroke-width="2" marker-end="url(#arrowGreen)"/>
    
    
    
    <line x1="430" y1="115" x2="493" y2="115" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowSky)"/>
    <text x="461" y="110" fill="#38bdf8" font-size="8.8" font-weight="bold" text-anchor="middle" font-family="-apple-system, sans-serif">HTTPS</text>
    
    
    <line x1="670" y1="140" x2="670" y2="153" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowSky)"/>
    <text x="670" y="141" fill="#38bdf8" font-size="8.8" font-weight="bold" text-anchor="middle" font-family="-apple-system, sans-serif">gRPC</text>
    
    
    <line x1="670" y1="205" x2="670" y2="218" stroke="#34d399" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="670" y="206" fill="#34d399" font-size="8.8" font-weight="bold" text-anchor="middle" font-family="-apple-system, sans-serif">runc</text>
    
    
</svg>"""
    aliases = """alias k='kubectl'
export do='--dry-run=client -o yaml'
export now='--grace-period=0 --force'"""
    checklist = [('CKA', 'Can you identify why a static pod is failing on a control plane node?', 'crictl ps -a && crictl logs <id>'), ('CKA', "Do you understand why kubectl delete pod won't terminate a static pod?", 'kubectl delete pod <name> (kubelet recreates it)'), ('CKA', 'Can you terminate unmanaged containers directly via CRI/containerd?', 'sudo ctr -n k8s.io tasks kill <id>')]
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
      ETCD is Kubernetes' distributed state database. In the CKA exam, tasks testing ETCD health inspection, member list queries, and snapshot backups occur frequently.
    </p>
    <ul>
      <li><strong>TLS Flag Triad:</strong> <code>etcdctl</code> requires three certificate parameters: <code>--cacert</code>, <code>--cert</code>, and <code>--key</code> found in <code>/etc/kubernetes/manifests/etcd.yaml</code>.</li>
      <li><strong>Snapshot Save:</strong> <code>ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 &lt;certs&gt; snapshot save /path/to/backup.db</code></li>
      <li><strong>Quorum:</strong> Needs $Q = \lfloor N/2 
floor + 1$ alive members. A 3-node cluster tolerates 1 node failure.</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 290" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
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
  <rect x="0" y="0" width="900" height="290" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.1: ETCD Quorum Architecture, TLS Mutual Auth & Snapshot Flow</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="400" height="220" rx="9" fill="url(#cardDark)" stroke="#059669" stroke-width="1.5"/>
      <rect x="30" y="50" width="400" height="28" rx="9" fill="#059669" opacity="0.18"/>
      <text x="44" y="70" fill="#34d399" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">ETCD CLUSTER QUORUM & RAFT</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Consensus: N/2 + 1 Nodes Required</text>
    </g>
    
    <rect x="50" y="90" width="105" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="102" y="116" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Node 1 (Leader)</text>
    <text x="102" y="134" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">:2379 / :2380</text>

    <rect x="175" y="90" width="105" height="60" rx="6" fill="#064e3b" stroke="#6ee7b7"/>
    <text x="227" y="116" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Node 2 (Follower)</text>
    <text x="227" y="134" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">:2379 / :2380</text>

    <rect x="300" y="90" width="110" height="60" rx="6" fill="#064e3b" stroke="#6ee7b7"/>
    <text x="355" y="116" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Node 3 (Follower)</text>
    <text x="355" y="134" fill="#a7f3d0" font-size="8" text-anchor="middle" font-family="monospace">:2379 / :2380</text>

    
    <rect x="50" y="165" width="360" height="90" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="60" y="181" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">Quorum Formula: Q = floor(N/2) + 1</text><text x="60" y="195" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">• 3 nodes -> Quorum = 2 (Tolerates 1 failure)</text><text x="60" y="209" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">• 5 nodes -> Quorum = 3 (Tolerates 2 failures)</text><text x="60" y="223" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">TLS Required: --cacert, --cert, --key</text>
    

    
    <g filter="url(#shadow)">
      <rect x="470" y="50" width="400" height="220" rx="9" fill="url(#cardDark)" stroke="#0284c7" stroke-width="1.5"/>
      <rect x="470" y="50" width="400" height="28" rx="9" fill="#0284c7" opacity="0.18"/>
      <text x="484" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">ETCD SNAPSHOT & DISASTER RESTORE</text>
      <text x="484" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Point-in-Time Database Backup</text>
    </g>
    
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
    
</svg>"""
    aliases = """export ETCDCTL_API=3
alias etcdctl='etcdctl --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key'"""
    checklist = [('CKA', 'Can you locate ETCD client certificates in /etc/kubernetes/manifests/etcd.yaml?', "grep -E 'cert-file|key-file|trusted-ca-file' /etc/kubernetes/manifests/etcd.yaml"), ('CKA', 'Can you save and verify an ETCD snapshot with etcdctl?', 'etcdctl snapshot save test.db && etcdctl snapshot status test.db'), ('CKA', 'Do you know how to query raw keys with prefix in ETCD v3?', 'etcdctl get /registry/namespaces --prefix --keys-only')]
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
      A <strong>Pod</strong> is the smallest deployable computing unit in Kubernetes. Containers within a Pod share the network namespace (IP address and port space) and storage volumes.
    </p>
    <ul>
      <li><strong>Pause Container:</strong> Creates and holds the network and IPC namespaces. If an application container crashes and restarts, the IP address is preserved.</li>
      <li><strong>Inter-Container Communication:</strong> Containers in the same Pod communicate over <code>localhost</code>. They must not bind to the same network port.</li>
      <li><strong>RestartPolicy:</strong> <code>Always</code> (default for Pods/Deployments), <code>OnFailure</code> (Jobs), <code>Never</code>.</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 270" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
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
  <rect x="0" y="0" width="900" height="270" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.1: Pod Multi-Container Shared Resources, Namespaces & Pause Container</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="200" rx="9" fill="url(#cardDark)" stroke="#6366f1" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#6366f1" opacity="0.18"/>
      <text x="44" y="70" fill="#818cf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">POD ANATOMY & SHARED NAMESPACE ARCHITECTURE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Pause Container holds Network & IPC Namespaces</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias krun='kubectl run --dry-run=client -o yaml'"""
    checklist = [('CKA', 'Can you generate a Pod YAML quickly with --dry-run=client -o yaml?', 'kubectl run nginx --image=nginx --dry-run=client -o yaml'), ('CKA', 'Can you configure multi-port pods without port collision?', 'Check containerPort uniqueness'), ('CKA', 'Do you know how to share storage volumes between pod containers?', 'spec.volumes emptyDir + volumeMounts')]
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
      Multi-container Pods allow tightly coupled helper processes to run alongside the main application.
    </p>
    <ul>
      <li><strong>Init Containers:</strong> Run sequentially to completion before app containers start. If an init container fails, Kubernetes restarts the Pod until it succeeds (unless restartPolicy=Never).</li>
      <li><strong>Sidecar Containers:</strong> Extend or enhance the primary container (e.g. log streaming, synchronization). In Kubernetes 1.28+, native sidecars use <code>initContainers</code> with <code>restartPolicy: Always</code>.</li>
    </ul>
    """
    svg = """<svg viewBox="0 0 900 270" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
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
  <rect x="0" y="0" width="900" height="270" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  
        <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.1: Kubernetes Multi-Container Architectural Patterns</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="200" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">MULTI-CONTAINER POD DESIGN PATTERNS</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Sidecar, Adapter & Ambassador</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias klogs='kubectl logs -f'"""
    checklist = [('CKA', 'Can you write an init container that blocks until a service is available?', 'initContainers with curl or nc probe'), ('CKA', 'Can you stream logs from a sidecar sharing an emptyDir volume?', 'kubectl logs -c sidecar')]
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
      Time management is the number one failure point in CKA. Candidates who hand-type YAML run out of time. Master imperative generators:
    </p>
    <ul>
      <li>Generate base Pod: <code>kubectl run my-pod --image=nginx --dry-run=client -o yaml > pod.yaml</code></li>
      <li>Generate Service: <code>kubectl expose pod my-pod --port=80 --name=my-svc --dry-run=client -o yaml > svc.yaml</code></li>
      <li>Instant deletion: <code>kubectl delete pod &lt;name&gt; --force --grace-period=0</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.1: Kubectl Imperative Object Generation Engine & Exam Execution Shortcuts</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBECTL IMPERATIVE GENERATION WORKFLOW</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Speed Strategy for 100% CKA Exam Completion</text>
    </g>
    
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
    
</svg>"""
    aliases = """alias k='kubectl'
export do='--dry-run=client -o yaml'
export now='--force --grace-period=0'"""
    checklist = [('CKA', 'Can you generate and edit a Pod YAML in under 30 seconds?', 'kubectl run test --image=busybox $do > test.yaml'), ('CKA', 'Can you change default kubectl namespace permanently for the current context?', 'kubectl config set-context --current --namespace=<ns>')]
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
      Week 1 consolidation integrates the full control plane stack: diagnosing crashed static pods, fixing API communication, managing pods with init containers, and rapid imperative commands under time pressure.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.1: Week 1 Integration: Incident Triage & Root Cause Discovery Flowchart</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">WEEK 1 CONTROL PLANE & WORKLOAD TRIAGE PIPELINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Incident Diagnosis Decision Tree</text>
    </g>
    
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

    
    <rect x="50" y="160" width="800" height="65" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="60" y="176" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">Fast Triage Flow:</text><text x="60" y="190" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">1. kubectl get nodes -> check Ready state</text><text x="60" y="204" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">2. kubectl get pods -A -o wide -> identify non-Running pods</text><text x="60" y="218" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">3. crictl ps -a & crictl logs <id> -> inspect static pods on controlplane</text>
    
    
</svg>"""
    aliases = """alias k='kubectl'
alias kgp='kubectl get pods -o wide'"""
    checklist = [('CKA', 'Can you troubleshoot an entire cluster startup failure in under 10 minutes?', 'crictl ps -a & journalctl -u kubelet'), ('CKA', 'Can you build a multi-container pod with shared volume in 3 minutes?', 'kubectl run multi-pod with YAML edit')]
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
