"""
CKAD Curriculum Content: Week 3 (Days 1 to 6)
Workload Scheduling & Pod Placement
"""
from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <h3>CKAD Week 3 Day 1: Resource Requests, Limits & OOM Troubleshooting</h3>
    <p><strong>Overview:</strong> CPU/Memory requests, limits, and OOMKilled resolution. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Resource Requests, Limits & OOM Troubleshooting</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W3D1: Resource Requests, Limits & OOM Troubleshooting</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">CPU/Memory requests, limits, and OOMKilled resolution</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Resource Requests, Limits & OOM Troubleshooting")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Resource Requests, Limits & OOM Troubleshooting in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """
    <h3>CKAD Week 3 Day 2: Manual Node Scheduling & NodeSelector</h3>
    <p><strong>Overview:</strong> Targeting specific nodes using nodeSelector and labels. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Manual Node Scheduling & NodeSelector</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 20m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W3D2: Manual Node Scheduling & NodeSelector</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Targeting specific nodes using nodeSelector and labels</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 20m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Manual Node Scheduling & NodeSelector")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Manual Node Scheduling & NodeSelector in under 20m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """
    <h3>CKAD Week 3 Day 3: Node Affinity: Required vs Preferred</h3>
    <p><strong>Overview:</strong> requiredDuringScheduling vs preferredDuringScheduling. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Node Affinity: Required vs Preferred</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W3D3: Node Affinity: Required vs Preferred</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">requiredDuringScheduling vs preferredDuringScheduling</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Node Affinity: Required vs Preferred")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Node Affinity: Required vs Preferred in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """
    <h3>CKAD Week 3 Day 4: Taints & Tolerations: Dedicated Workload Isolation</h3>
    <p><strong>Overview:</strong> Tainting worker nodes with NoSchedule and tolerations. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Taints & Tolerations: Dedicated Workload Isolation</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W3D4: Taints & Tolerations: Dedicated Workload Isolation</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Tainting worker nodes with NoSchedule and tolerations</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Taints & Tolerations: Dedicated Workload Isolation")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Taints & Tolerations: Dedicated Workload Isolation in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """
    <h3>CKAD Week 3 Day 5: Labels, Selectors & Annotation Bulk Management</h3>
    <p><strong>Overview:</strong> Querying, filtering, and updating labels across namespaces. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Labels, Selectors & Annotation Bulk Management</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 20m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W3D5: Labels, Selectors & Annotation Bulk Management</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Querying, filtering, and updating labels across namespaces</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 20m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Labels, Selectors & Annotation Bulk Management")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Labels, Selectors & Annotation Bulk Management in under 20m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """
    <h3>CKAD Week 3 Day 6: Week 3 Milestone: Precision Workload Placement</h3>
    <p><strong>Overview:</strong> Deploying multi-node pod topology with taints and affinity. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Week 3 Milestone: Precision Workload Placement</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 40m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W3D6: Week 3 Milestone: Precision Workload Placement</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Deploying multi-node pod topology with taints and affinity</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 40m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Week 3 Milestone: Precision Workload Placement")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Week 3 Milestone: Precision Workload Placement in under 40m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
