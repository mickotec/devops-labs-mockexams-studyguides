"""
CKAD Curriculum Content: Week 5 (Days 1 to 6)
Application Observability & Debugging
"""
from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <h3>CKAD Week 5 Day 1: Liveness Probes: HTTP, Command & TCP Checks</h3>
    <p><strong>Overview:</strong> Detecting deadlock and restarting failed containers. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Liveness Probes: HTTP, Command & TCP Checks</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W5D1: Liveness Probes: HTTP, Command & TCP Checks</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Detecting deadlock and restarting failed containers</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Liveness Probes: HTTP, Command & TCP Checks")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Liveness Probes: HTTP, Command & TCP Checks in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """
    <h3>CKAD Week 5 Day 2: Readiness Probes & Service Traffic Gating</h3>
    <p><strong>Overview:</strong> Preventing traffic to unready containers until warmup. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Readiness Probes & Service Traffic Gating</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W5D2: Readiness Probes & Service Traffic Gating</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Preventing traffic to unready containers until warmup</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Readiness Probes & Service Traffic Gating")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Readiness Probes & Service Traffic Gating in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """
    <h3>CKAD Week 5 Day 3: Startup Probes for Slow-Initializing Applications</h3>
    <p><strong>Overview:</strong> failureThreshold and periodSeconds for slow containers. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Startup Probes for Slow-Initializing Applications</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W5D3: Startup Probes for Slow-Initializing Applications</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">failureThreshold and periodSeconds for slow containers</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Startup Probes for Slow-Initializing Applications")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Startup Probes for Slow-Initializing Applications in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """
    <h3>CKAD Week 5 Day 4: Container Logging: Multi-Container & Previous Logs</h3>
    <p><strong>Overview:</strong> Extracting logs from crashing pods with --previous. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Container Logging: Multi-Container & Previous Logs</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 20m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W5D4: Container Logging: Multi-Container & Previous Logs</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Extracting logs from crashing pods with --previous</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 20m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Container Logging: Multi-Container & Previous Logs")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Container Logging: Multi-Container & Previous Logs in under 20m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """
    <h3>CKAD Week 5 Day 5: Metrics Server & CLI Resource Monitoring</h3>
    <p><strong>Overview:</strong> kubectl top pod and top node parsing and sorting. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Metrics Server & CLI Resource Monitoring</li>
      <li><strong>Target Image / Workload:</strong> <code>metrics-server</code></li>
      <li><strong>Target Time Limit:</strong> 20m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W5D5: Metrics Server & CLI Resource Monitoring</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">kubectl top pod and top node parsing and sorting</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 20m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Metrics Server & CLI Resource Monitoring")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Metrics Server & CLI Resource Monitoring in under 20m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """
    <h3>CKAD Week 5 Day 6: Week 5 Milestone: Comprehensive Health & Triage Suite</h3>
    <p><strong>Overview:</strong> Configuring full probe lifecycle and resolving crash loops. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Week 5 Milestone: Comprehensive Health & Triage Suite</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 40m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W5D6: Week 5 Milestone: Comprehensive Health & Triage Suite</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Configuring full probe lifecycle and resolving crash loops</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 40m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Week 5 Milestone: Comprehensive Health & Triage Suite")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Week 5 Milestone: Comprehensive Health & Triage Suite in under 40m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
