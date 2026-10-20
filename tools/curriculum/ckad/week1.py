"""
CKAD Curriculum Content: Week 1 (Days 1 to 6)
Core Concepts & Pod Architecture
"""
from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <h3>CKAD Week 1 Day 1: Multi-Container Pods & Sidecar Logging</h3>
    <p><strong>Overview:</strong> emptyDir shared volume and log shipping. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Multi-Container Pods & Sidecar Logging</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W1D1: Multi-Container Pods & Sidecar Logging</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">emptyDir shared volume and log shipping</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Multi-Container Pods & Sidecar Logging")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Multi-Container Pods & Sidecar Logging in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """
    <h3>CKAD Week 1 Day 2: Init Containers & Service Dependency Blocking</h3>
    <p><strong>Overview:</strong> Sequential init containers blocking until db is ready. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Init Containers & Service Dependency Blocking</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W1D2: Init Containers & Service Dependency Blocking</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Sequential init containers blocking until db is ready</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Init Containers & Service Dependency Blocking")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Init Containers & Service Dependency Blocking in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """
    <h3>CKAD Week 1 Day 3: Imperative Pod & Deployment CLI Mastery</h3>
    <p><strong>Overview:</strong> Rapid kubectl run and create with dry-run. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Imperative Pod & Deployment CLI Mastery</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 20m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W1D3: Imperative Pod & Deployment CLI Mastery</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Rapid kubectl run and create with dry-run</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 20m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Imperative Pod & Deployment CLI Mastery")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Imperative Pod & Deployment CLI Mastery in under 20m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """
    <h3>CKAD Week 1 Day 4: Advanced Output Formatting with JSONPath</h3>
    <p><strong>Overview:</strong> Extracting custom columns and sorting. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Advanced Output Formatting with JSONPath</li>
      <li><strong>Target Image / Workload:</strong> <code>kube-system pods</code></li>
      <li><strong>Target Time Limit:</strong> 20m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W1D4: Advanced Output Formatting with JSONPath</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Extracting custom columns and sorting</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 20m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Advanced Output Formatting with JSONPath")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Advanced Output Formatting with JSONPath in under 20m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """
    <h3>CKAD Week 1 Day 5: ReplicaSets & Deployment Scaling Strategies</h3>
    <p><strong>Overview:</strong> Pod template selectors and replica management. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> ReplicaSets & Deployment Scaling Strategies</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 20m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W1D5: ReplicaSets & Deployment Scaling Strategies</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Pod template selectors and replica management</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 20m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "ReplicaSets & Deployment Scaling Strategies")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve ReplicaSets & Deployment Scaling Strategies in under 20m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """
    <h3>CKAD Week 1 Day 6: Week 1 Milestone: Multi-Tier Core Application</h3>
    <p><strong>Overview:</strong> Full multi-tier app with sidecars and NodePort. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Week 1 Milestone: Multi-Tier Core Application</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 40m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W1D6: Week 1 Milestone: Multi-Tier Core Application</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Full multi-tier app with sidecars and NodePort</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 40m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Week 1 Milestone: Multi-Tier Core Application")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Week 1 Milestone: Multi-Tier Core Application in under 40m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
