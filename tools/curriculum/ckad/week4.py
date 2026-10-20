"""CKAD Curriculum Content: Week 4
Week 4: Observability, Health Probes & Maintenance
"""

def get_day_1():
    theory = """<p><strong>Readiness Probes</strong> prevent traffic routing to warming-up or overloaded pods by controlling Service Endpoints.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 4 Day 1: Readiness Probes & Service Endpoint Management</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgep='kubectl get endpoints'"""
    checklist = [('CKAD', 'Configure HTTP GET readiness probe on container port', 'kubectl explain pod.spec.containers.readinessProbe.httpGet'), ('CKAD', 'Verify unready pod is excluded from service endpoints', 'kubectl get endpoints <service>')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """<p><strong>Liveness Probes</strong> detect deadlocked or broken processes, triggering kubelet automated container restarts.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 4 Day 2: Liveness Probes & Automated Container Healing</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgpr='kubectl get pods'"""
    checklist = [('CKAD', 'Configure Exec liveness probe in pod manifest', 'kubectl explain pod.spec.containers.livenessProbe.exec')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """<p><strong>Startup Probes</strong> disable liveness and readiness checks during slow initialization windows, preventing premature container kills.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 4 Day 3: Startup Probes for Slow-Starting Applications</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias ksp='kubectl explain pod.spec.containers.startupProbe'"""
    checklist = [('CKAD', 'Configure failureThreshold and periodSeconds for slow boot window', 'failureThreshold: 30, periodSeconds: 5')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """<p>Retrieve logs of previous crashed instances using <code>kubectl logs -p</code> and target specific containers with <code>-c</code>.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 4 Day 4: Multi-Container Logs & Crash Troubleshooting</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias klp='kubectl logs --previous'"""
    checklist = [('CKAD', 'Retrieve logs of previous crashed container using -p flag', 'kubectl logs <pod> -c <container> -p')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """<p>Metrics Server provides real-time CPU and Memory utilization data via <code>kubectl top pod</code> and <code>kubectl top node</code>.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 4 Day 5: Metrics Server & CLI Workload Monitoring (kubectl top)</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias ktopp='kubectl top pod'\nalias ktopn='kubectl top node'"""
    checklist = [('CKAD', 'Sort pods by CPU usage across all namespaces', 'kubectl top pod -A --sort-by=cpu'), ('CKAD', 'Sort pods by memory usage within a namespace', 'kubectl top pod -n <ns> --sort-by=memory')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """<p>Exit Code 137 indicates kernel OOMKiller termination (exceeded memory limit). Exit Code 127 indicates missing executable binary in PATH.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 4 Day 6: Debugging Exit Codes: 137 OOMKilled & 127 Command Not Found</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kexit='kubectl get pod -o jsonpath="{.status.containerStatuses[*].lastState.terminated.exitCode}"'"""
    checklist = [('CKAD', 'Diagnose Exit Code 137 OOMKilled and adjust memory limits', 'kubectl describe pod <name> | grep -i oom'), ('CKAD', 'Fix Exit Code 127 Command Not Found in pod command spec', 'kubectl logs <pod>')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
