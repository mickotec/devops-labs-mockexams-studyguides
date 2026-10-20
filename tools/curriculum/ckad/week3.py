"""CKAD Curriculum Content: Week 3
Week 3: Multi-Container Pods & Scheduling
"""

def get_day_1():
    theory = """<p>The <strong>Sidecar pattern</strong> enhances primary containers by co-locating supporting processes (e.g. log streaming) sharing an <code>emptyDir</code> volume.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 3 Day 1: Multi-Container Pods: Sidecar Pattern for Logging</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias klogs='kubectl logs -c'"""
    checklist = [('CKAD', 'Mount shared emptyDir between two containers in one pod', 'kubectl explain pod.spec.volumes.emptyDir'), ('CKAD', 'Retrieve logs from specific container with -c flag', 'kubectl logs <pod> -c <container>')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """<p>The <strong>Adapter pattern</strong> normalizes disparate application metrics or outputs into a standardized format (e.g. Prometheus metrics) for cluster scrapers.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 3 Day 2: Multi-Container Pods: Adapter Pattern for Metric Formatting</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kexec='kubectl exec -it'"""
    checklist = [('CKAD', 'Understand adapter pattern for normalizing heterogeneous output', 'kubectl explain pod.spec.containers')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """<p>The <strong>Ambassador pattern</strong> acts as a local proxy container routing application connections from <code>localhost</code> to remote cluster services.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 3 Day 3: Multi-Container Pods: Ambassador Pattern for Proxies</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kpf='kubectl port-forward'"""
    checklist = [('CKAD', 'Connect two containers in the same pod via localhost', 'curl http://localhost:6379')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """<p><strong>Init Containers</strong> run sequentially to completion before any application containers start, gating startup on external dependencies.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 3 Day 4: Init Containers & Sequential Dependency Checks</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgi='kubectl get pods -o wide'"""
    checklist = [('CKAD', 'Define initContainers in pod spec to gate startup', 'kubectl explain pod.spec.initContainers'), ('CKAD', 'Use netcat (nc -z) in init container to wait for dependent service', "command: ['sh', '-c', 'until nc -z -w 2 db-svc 3306; do sleep 2; done']")]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """<p><strong>Taints</strong> allow nodes to repel pods unless those pods possess matching <strong>Tolerations</strong>.</p>
<ul>
  <li>Taint Effects: <code>NoSchedule</code>, <code>PreferNoSchedule</code>, <code>NoExecute</code>.</li>
  <li>Operators: <code>Equal</code> (exact match) and <code>Exists</code> (wildcard match).</li>
</ul>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 3 Day 5: Node Taints, Effects & Pod Tolerations</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias ktaint='kubectl taint nodes'"""
    checklist = [('CKAD', 'Apply and remove taints on worker nodes', 'kubectl taint nodes node01 tier=gold:NoSchedule-'), ('CKAD', 'Configure pod tolerations in pod spec', 'kubectl explain pod.spec.tolerations')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """<p><strong>Node Affinity</strong> provides expressive rules attracting pods to specific nodes based on node labels.</p>
<ul>
  <li><code>requiredDuringSchedulingIgnoredDuringExecution:</code> Hard scheduling requirement.</li>
  <li><code>preferredDuringSchedulingIgnoredDuringExecution:</code> Soft weighted preference.</li>
</ul>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 3 Day 6: Node Selectors, Node Affinity & Scheduling Rules</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgnl='kubectl get nodes --show-labels'"""
    checklist = [('CKAD', 'Label a node with key-value pairs', 'kubectl label node node02 disktype=nvme'), ('CKAD', 'Configure requiredDuringScheduling nodeAffinity in pod spec', 'kubectl explain pod.spec.affinity.nodeAffinity')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
