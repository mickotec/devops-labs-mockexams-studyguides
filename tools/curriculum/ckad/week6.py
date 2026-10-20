"""CKAD Curriculum Content: Week 6
Week 6: Services, Networking & Ingress
"""

def get_day_1():
    theory = """<p>Services expose applications with stable virtual IPs (ClusterIP) or node ports (NodePort) routing to container targetPorts.</p>"""
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
  </defs>
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 6 Day 1: Kubernetes Services: ClusterIP, NodePort & Port Mapping</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgsvc='kubectl get svc'\nalias kgep='kubectl get endpoints'"""
    checklist = [('CKAD', 'Create ClusterIP and NodePort services using kubectl expose', 'kubectl expose deploy web --port=80 --target-port=8080')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """<p>Headless Services (<code>clusterIP: None</code>) provide direct CoreDNS SRV and A record resolution for stateful pods.</p>"""
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
  </defs>
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 6 Day 2: Headless Services & Direct Stateful Pod Discovery</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias knslookup='kubectl run test-dns --image=busybox --rm -it -- nslookup'"""
    checklist = [('CKAD', 'Create Headless Service by setting clusterIP: None', 'kubectl explain svc.spec.clusterIP')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """<p>Default-deny NetworkPolicies enforce zero-trust isolation by dropping all incoming or outgoing traffic across the namespace.</p>"""
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
  </defs>
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 6 Day 3: NetworkPolicies: Default Ingress & Egress Namespace Isolation</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgnp='kubectl get netpol'"""
    checklist = [('CKAD', 'Create default deny ingress policy using empty podSelector', 'kubectl explain netpol.spec')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """<p>Granular NetworkPolicies whitelist traffic strictly from authorized pods, namespaces, and explicit TCP/UDP ports.</p>"""
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
  </defs>
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 6 Day 4: NetworkPolicies: Fine-Grained Pod & Namespace Selector Rules</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kdnp='kubectl describe netpol'"""
    checklist = [('CKAD', 'Allow ingress from pods matching specific labels on port 8080', 'from: [{podSelector: {matchLabels: {app: web}}}]')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """<p>Ingress controllers manage external HTTP routing into cluster services based on host headers and URL path prefixes.</p>"""
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
  </defs>
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 6 Day 5: Ingress Networking: Host & Path-Based HTTP Routing</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kging='kubectl get ingress'"""
    checklist = [('CKAD', 'Create Ingress with host-based routing imperatively', "kubectl create ingress store --rule='store.internal/api*=api-svc:80'")]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """<p>Use <code>rewrite-target</code> annotations and regex path capture groups to strip prefixes before forwarding requests to backends.</p>"""
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
  </defs>
  <rect x="0" y="0" width="900" height="260" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="15" y="10" width="870" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
  <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 6 Day 6: Ingress URL Rewriting, Annotations & TLS Termination</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kinganno='kubectl get ingress -o jsonpath="{.items[*].metadata.annotations}"'"""
    checklist = [('CKAD', 'Configure nginx.ingress.kubernetes.io/rewrite-target annotation', 'annotations: {nginx.ingress.kubernetes.io/rewrite-target: /}')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
