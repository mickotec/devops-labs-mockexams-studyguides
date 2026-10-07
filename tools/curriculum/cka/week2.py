"""
CKA Curriculum Content: Week 2 (Days 1 to 6)
Day 1: ReplicaSets & Self-Healing Controllers
Day 2: Deployments, Rollouts & Revisions
Day 3: Services: ClusterIP, NodePort & LoadBalancer
Day 4: Namespaces & DNS Resolution Inside Clusters
Day 5: Kubectl Explain & Declarative Workflow
Day 6: Week 2 Speed Drills & Controller Triathlon
"""

from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <p>
      The <strong>ReplicaSet</strong> ensures a specified number of Pod replicas match a label selector at all times. In modern Kubernetes, administrators rarely create ReplicaSets directly; they use <strong>Deployments</strong>, which manage ReplicaSets declaratively.
    </p>
    <ul>
      <li><strong>MatchLabels:</strong> Must strictly match <code>template.metadata.labels</code> or admission is rejected.</li>
      <li><strong>Pod Adoption &amp; Orphanage:</strong> ReplicaSets manage pods based solely on label matching, not creation origin. Changing a pod's label causes the ReplicaSet to spawn a replacement.</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 1.1: ReplicaSet Selector Matching Loop & Self-Healing Action</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">REPLICASET RECONCILIATION LOOP & SELECTOR ARCHITECTURE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Desired State vs Actual State Synchronization</text>
    </g>
    
    <rect x="50" y="90" width="230" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="165" y="115" fill="#38bdf8" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">REPLICASET SPEC</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.8" font-family="monospace">replicas: 3</text>
    <text x="65" y="160" fill="#fde047" font-size="8.8" font-family="monospace">selector:</text>
    <text x="75" y="175" fill="#fde047" font-size="8.5" font-family="monospace">matchLabels:</text>
    <text x="85" y="190" fill="#fde047" font-size="8.5" font-family="monospace">app: web-store</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">Matches pod labels in same namespace</text>

    <rect x="310" y="90" width="220" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="420" y="115" fill="#34d399" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">ACTIVE MANAGED PODS</text>
    <rect x="325" y="130" width="190" height="25" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="420" y="147" fill="#ffffff" font-size="8.8" text-anchor="middle" font-family="monospace">web-store-a1 (labels: app=web-store)</text>
    <rect x="325" y="160" width="190" height="25" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="420" y="177" fill="#ffffff" font-size="8.8" text-anchor="middle" font-family="monospace">web-store-b2 (labels: app=web-store)</text>
    <rect x="325" y="190" width="190" height="25" rx="4" fill="#065f46" stroke="#34d399"/>
    <text x="420" y="207" fill="#ffffff" font-size="8.8" text-anchor="middle" font-family="monospace">web-store-c3 (labels: app=web-store)</text>

    <rect x="560" y="90" width="290" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="705" y="115" fill="#fbbf24" font-size="11.5" font-weight="bold" text-anchor="middle" font-family="sans-serif">SELF-HEALING CONTROLLER ACTION</text>
    <text x="575" y="140" fill="#fca5a5" font-size="8.5" font-family="sans-serif">• If Pod web-store-a1 dies: Actual (2) &lt; Desired (3)</text>
    <text x="575" y="158" fill="#4ade80" font-size="8.5" font-family="sans-serif">  -> RS Controller immediately spawns replacement!</text>
    <text x="575" y="180" fill="#fde047" font-size="8.5" font-family="sans-serif">• If someone changes pod label:</text>
    <text x="575" y="198" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">  -> Pod is orphaned; RS spawns a new one to reach 3!</text>
    
</svg>"""
    aliases = """alias krs='kubectl get rs -o wide'
alias kscale='kubectl scale rs --replicas'"""
    checklist = [('CKA', 'Can you scale a ReplicaSet up and down imperatively and declaratively?', 'kubectl scale rs <name> --replicas=5'), ('CKA', 'Do you understand what happens when a managed pod label is removed?', 'ReplicaSet detects deficit and spawns new pod')]
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
      Deployments provide declarative updates for Pods and ReplicaSets.
    </p>
    <ul>
      <li><strong>Rolling Updates:</strong> Controlled by <code>maxSurge</code> (extra pods allowed above desired) and <code>maxUnavailable</code> (allowed deficit).</li>
      <li><strong>Rollout Management:</strong>
        <pre><code>kubectl rollout status deployment/my-deploy
kubectl rollout history deployment/my-deploy
kubectl rollout undo deployment/my-deploy --to-revision=2</code></pre>
      </li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 2.1: Kubernetes Deployment RollingUpdate Mechanics & Rollout Controller</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">DEPLOYMENT ROLLING UPDATE & REVISION HISTORY</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Zero-Downtime Releases via Dual ReplicaSet Scaling</text>
    </g>
    
    <rect x="50" y="90" width="220" height="135" rx="6" fill="#1e293b" stroke="#60a5fa"/>
    <text x="160" y="115" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">DEPLOYMENT SPEC</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">strategy: RollingUpdate</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="monospace">maxSurge: 25%</text>
    <text x="65" y="180" fill="#e2e8f0" font-size="8.5" font-family="monospace">maxUnavailable: 25%</text>
    <text x="65" y="205" fill="#fde047" font-size="8.5" font-family="monospace">revisionHistoryLimit: 10</text>

    <rect x="300" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#f43f5e"/>
    <text x="420" y="115" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">OLD RS (v1: nginx:1.24)</text>
    <text x="315" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Scale down: 4 -> 3 -> 2 -> 1 -> 0</text>
    <text x="315" y="160" fill="#94a3b8" font-size="8.5" font-family="sans-serif">• Pods gracefully terminate (preStop)</text>
    <text x="315" y="185" fill="#cbd5e1" font-size="8.5" font-family="monospace">pod-v1-abc1 (Terminating)</text>
    <text x="315" y="205" fill="#fca5a5" font-size="8" font-family="sans-serif">Retained for instant rollback capability!</text>

    <rect x="570" y="90" width="280" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="710" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">NEW RS (v2: nginx:1.25)</text>
    <text x="585" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Scale up: 0 -> 1 -> 2 -> 3 -> 4</text>
    <text x="585" y="160" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Wait for Readiness Probes to pass</text>
    <text x="585" y="185" fill="#cbd5e1" font-size="8.5" font-family="monospace">pod-v2-xyz9 (Running &amp; Ready)</text>
    <text x="585" y="205" fill="#38bdf8" font-size="8" font-family="monospace">kubectl rollout undo deploy &lt;name&gt;</text>
    
</svg>"""
    aliases = """alias kroll='kubectl rollout status'
alias kundo='kubectl rollout undo'"""
    checklist = [('CKA', 'Can you update an image in a deployment and check rollout status?', 'kubectl set image deploy/<name> <c>=<img:tag> && kubectl rollout status deploy/<name>'), ('CKA', 'Can you rollback a deployment to a previous revision?', 'kubectl rollout undo deploy/<name> --to-revision=<n>')]
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
      Services route traffic to Pods matching their selector. The <strong>EndpointSlice</strong> (or Endpoints) object lists healthy Pod IPs.
    </p>
    <ul>
      <li><strong>TargetPort vs Port:</strong> <code>port</code> is the Service port; <code>targetPort</code> is the port exposed on the Pod container.</li>
      <li><strong>Troubleshooting Tip:</strong> If <code>kubectl get endpoints &lt;svc&gt;</code> has no IPs, the Service selector does not match the Pod labels, or the Pods failed their Readiness Probes!</li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 3.1: Kubernetes Service Topologies & Endpoint Dispatch</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBERNETES SERVICE TYPES & TRAFFIC ROUTING</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">ClusterIP, NodePort & LoadBalancer</text>
    </g>
    
    <rect x="50" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="175" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">1. CLUSTERIP (Default)</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Internal virtual IP inside cluster</text>
    <text x="65" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Inaccessible from external network</text>
    <text x="65" y="180" fill="#34d399" font-size="8.5" font-family="monospace">spec.type: ClusterIP</text>
    <text x="65" y="200" fill="#a7f3d0" font-size="8" font-family="monospace">Port: 80 -> TargetPort: 8080</text>

    <rect x="325" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="450" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">2. NODEPORT (30000-32767)</text>
    <text x="340" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Exposes port on every worker node</text>
    <text x="340" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Routes: NodeIP:NodePort -> Pod</text>
    <text x="340" y="180" fill="#fde047" font-size="8.5" font-family="monospace">spec.type: NodePort</text>
    <text x="340" y="200" fill="#fef3c7" font-size="8" font-family="monospace">NodePort: 31234 -> Port 80</text>

    <rect x="600" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="725" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">3. LOADBALANCER</text>
    <text x="615" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Provisions cloud provider load balancer</text>
    <text x="615" y="160" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Automatically configures NodePort</text>
    <text x="615" y="180" fill="#38bdf8" font-size="8.5" font-family="monospace">spec.type: LoadBalancer</text>
    <text x="615" y="200" fill="#7dd3fc" font-size="8" font-family="monospace">External-IP: 20.42.18.9</text>
    
</svg>"""
    aliases = """alias ksvc='kubectl get svc,endpoints'"""
    checklist = [('CKA', 'Can you expose a deployment as a NodePort service imperatively?', 'kubectl expose deploy <name> --type=NodePort --port=80'), ('CKA', 'Can you inspect Endpoints to verify pod discovery?', 'kubectl get endpoints <service-name>')]
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
      Kubernetes CoreDNS provides automatic DNS records for Services and Pods.
    </p>
    <ul>
      <li>Service FQDN: <code>&lt;service-name&gt;.&lt;namespace&gt;.svc.cluster.local</code></li>
      <li>Pod DNS: <code>&lt;pod-ip-dashed&gt;.&lt;namespace&gt;.pod.cluster.local</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 4.1: Kubernetes CoreDNS Service Discovery & FQDN Architecture</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBERNETES CLUSTER DNS RESOLUTION HIERARCHY</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">FQDN Format: <service>.<namespace>.svc.cluster.local</text>
    </g>
    
    <rect x="50" y="90" width="240" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="170" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">POD /etc/resolv.conf</text>
    <text x="65" y="140" fill="#e2e8f0" font-size="8.5" font-family="monospace">nameserver 10.96.0.10</text>
    <text x="65" y="160" fill="#fde047" font-size="8" font-family="monospace">search default.svc.cluster.local</text>
    <text x="65" y="175" fill="#fde047" font-size="8" font-family="monospace">       svc.cluster.local</text>
    <text x="65" y="190" fill="#fde047" font-size="8" font-family="monospace">       cluster.local</text>
    <text x="65" y="210" fill="#94a3b8" font-size="8" font-family="sans-serif">options ndots:5</text>

    <rect x="310" y="90" width="250" height="135" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="435" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">COREDNS (kube-system)</text>
    <text x="325" y="140" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• CoreDNS static/deployment pods</text>
    <text x="325" y="160" fill="#a7f3d0" font-size="8.5" font-family="sans-serif">• Watches Service &amp; Endpoint state</text>
    <text x="325" y="185" fill="#e2e8f0" font-size="8.5" font-family="monospace">dig @10.96.0.10 web.prod.svc...</text>
    <text x="325" y="205" fill="#38bdf8" font-size="8" font-family="monospace">kubectl get pods -n kube-system -l k8s-app=kube-dns</text>

    <rect x="580" y="90" width="270" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="715" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">CROSS-NAMESPACE CALLS</text>
    <text x="595" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Same namespace: <code>curl web-svc</code></text>
    <text x="595" y="165" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Across namespaces:</text>
    <text x="605" y="185" fill="#fde047" font-size="8.5" font-family="monospace">curl web-svc.finance.svc</text>
    <text x="595" y="205" fill="#4ade80" font-size="8" font-family="sans-serif">Fully Qualified: web-svc.finance.svc.cluster.local</text>
    
</svg>"""
    aliases = """alias kns='kubectl config set-context --current --namespace'"""
    checklist = [('CKA', 'Can you test DNS resolution from within a cluster using busybox?', 'kubectl run dns-test --image=busybox:1.36 --rm -it -- nslookup <svc>'), ('CKA', 'Can you resolve services across different namespaces?', '<svc-name>.<namespace>.svc.cluster.local')]
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
      <code>kubectl explain</code> is your built-in offline reference. Use it to check manifest schemas without leaving the shell:
    </p>
    <ul>
      <li>Check required fields: <code>kubectl explain pod.spec</code></li>
      <li>Examine probe configurations: <code>kubectl explain pod.spec.containers.livenessProbe.httpGet</code></li>
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 5.1: Kubectl Explain Offline API Specification Navigation Tree</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">KUBECTL EXPLAIN SCHEMA RECURSION ENGINE</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Offline API Specification Navigator</text>
    </g>
    
    <rect x="50" y="90" width="370" height="135" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="235" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">RECURSIVE DRILLDOWN</text>
    <text x="65" y="140" fill="#4ade80" font-size="8.8" font-family="monospace">k explain pod.spec.containers</text>
    <text x="65" y="160" fill="#4ade80" font-size="8.8" font-family="monospace">k explain pod.spec.containers.livenessProbe</text>
    <text x="65" y="180" fill="#4ade80" font-size="8.8" font-family="monospace">k explain deploy.spec.strategy.rollingUpdate</text>
    <text x="65" y="200" fill="#fde047" font-size="8.5" font-family="monospace">k explain service.spec --recursive | grep -A5 type</text>

    <rect x="450" y="90" width="400" height="135" rx="6" fill="#1e293b" stroke="#fbbf24"/>
    <text x="650" y="115" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">EXAM USAGE TACTICS</text>
    <text x="465" y="140" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• When unsure of YAML casing or required subfields:</text>
    <text x="465" y="160" fill="#38bdf8" font-size="8.5" font-family="monospace">kubectl explain &lt;type&gt;.&lt;field&gt;</text>
    <text x="465" y="180" fill="#e2e8f0" font-size="8.5" font-family="sans-serif">• Displays field type: <code>&lt;string&gt;</code>, <code>&lt;[]Object&gt;</code>, <code>&lt;boolean&gt;</code></text>
    <text x="465" y="200" fill="#34d399" font-size="8.5" font-family="sans-serif">• 100% available in offline / air-gapped exam terminals!</text>
    
</svg>"""
    aliases = """alias kexp='kubectl explain'"""
    checklist = [('CKA', 'Can you use kubectl explain to locate field names and types quickly?', 'kubectl explain pod.spec.tolerations'), ('CKA', 'Can you query a deeply nested subfield with recursive explain?', 'kubectl explain deployment.spec.strategy --recursive')]
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
      Week 2 integration requires synthesizing deployments, service routing, CoreDNS resolution, and declarative management into a fast, repeatable exam routine.
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
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">Figure 6.1: Week 2 Workload Triathlon Execution Sequence</text>
        

  
    
    <g filter="url(#shadow)">
      <rect x="30" y="50" width="840" height="190" rx="9" fill="url(#cardDark)" stroke="#0f172a" stroke-width="1.5"/>
      <rect x="30" y="50" width="840" height="28" rx="9" fill="#0f172a" opacity="0.18"/>
      <text x="44" y="70" fill="#38bdf8" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">WEEK 2 CONTROLLER TRIATHLON WORKFLOW</text>
      <text x="44" y="90" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">Deployment -> ReplicaSet -> Pods -> Service -> Ingress</text>
    </g>
    
    <rect x="50" y="90" width="180" height="60" rx="6" fill="#1e3a8a" stroke="#60a5fa"/>
    <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Deployment</text>
    <text x="140" y="135" fill="#93c5fd" font-size="8.5" text-anchor="middle" font-family="monospace">Rollout &amp; Spec</text>

    <rect x="260" y="90" width="180" height="60" rx="6" fill="#047857" stroke="#34d399"/>
    <text x="350" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">ReplicaSet</text>
    <text x="350" y="135" fill="#a7f3d0" font-size="8.5" text-anchor="middle" font-family="monospace">Replicas Count (3)</text>

    <rect x="470" y="90" width="180" height="60" rx="6" fill="#78350f" stroke="#fbbf24"/>
    <text x="560" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Pods (x3)</text>
    <text x="560" y="135" fill="#fef3c7" font-size="8.5" text-anchor="middle" font-family="monospace">app=web, env=prod</text>

    <rect x="680" y="90" width="170" height="60" rx="6" fill="#881337" stroke="#f43f5e"/>
    <text x="765" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle" font-family="sans-serif">Service &amp; Endpoints</text>
    <text x="765" y="135" fill="#fca5a5" font-size="8.5" text-anchor="middle" font-family="monospace">VIP &amp; TargetPort</text>

    
    <rect x="50" y="160" width="800" height="65" rx="5" fill="#030712" stroke="#334155" stroke-width="1"/>
    <text x="60" y="176" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">Triathlon Rapid Sequence:</text><text x="60" y="190" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">1. k create deploy web --image=nginx:alpine --replicas=3 $do > web.yaml</text><text x="60" y="204" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">2. k expose deploy web --port=80 --target-port=80 --type=NodePort $do > svc.yaml</text><text x="60" y="218" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">3. k apply -f web.yaml -f svc.yaml && k get pods,svc,endpoints -l app=web</text>
    
    
</svg>"""
    aliases = """alias kall='kubectl get deploy,rs,po,svc,ep'"""
    checklist = [('CKA', 'Can you create a Deployment, expose it as NodePort, and test it in under 4 minutes?', 'kubectl create deploy && kubectl expose'), ('CKA', 'Can you perform a rolling update and immediate rollback?', 'kubectl rollout undo deploy/<name>')]
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
