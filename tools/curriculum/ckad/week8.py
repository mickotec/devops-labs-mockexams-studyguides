"""
CKAD Curriculum Content: Week 8 (Days 1 to 6)
Security, CRDs & killer.sh Mock Exams
"""
from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <h3>CKAD Week 8 Day 1: Kubeconfig Architecture & Multi-Cluster Contexts</h3>
    <p><strong>Overview:</strong> Clusters, users, contexts, and active context switching. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Kubeconfig Architecture & Multi-Cluster Contexts</li>
      <li><strong>Target Image / Workload:</strong> <code>kubeconfig</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W8D1: Kubeconfig Architecture & Multi-Cluster Contexts</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Clusters, users, contexts, and active context switching</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Kubeconfig Architecture & Multi-Cluster Contexts")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Kubeconfig Architecture & Multi-Cluster Contexts in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """
    <h3>CKAD Week 8 Day 2: RBAC: Role & RoleBinding Scoped Authorizations</h3>
    <p><strong>Overview:</strong> Granting developer access to specific namespace resources. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> RBAC: Role & RoleBinding Scoped Authorizations</li>
      <li><strong>Target Image / Workload:</strong> <code>rbac</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W8D2: RBAC: Role & RoleBinding Scoped Authorizations</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Granting developer access to specific namespace resources</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "RBAC: Role & RoleBinding Scoped Authorizations")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve RBAC: Role & RoleBinding Scoped Authorizations in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """
    <h3>CKAD Week 8 Day 3: RBAC: ClusterRole & ClusterRoleBinding Global Rules</h3>
    <p><strong>Overview:</strong> Cluster-wide resource querying and non-namespaced APIs. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> RBAC: ClusterRole & ClusterRoleBinding Global Rules</li>
      <li><strong>Target Image / Workload:</strong> <code>rbac</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W8D3: RBAC: ClusterRole & ClusterRoleBinding Global Rules</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Cluster-wide resource querying and non-namespaced APIs</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "RBAC: ClusterRole & ClusterRoleBinding Global Rules")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve RBAC: ClusterRole & ClusterRoleBinding Global Rules in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """
    <h3>CKAD Week 8 Day 4: Custom Resource Definitions (CRDs) & API Extensions</h3>
    <p><strong>Overview:</strong> Creating CRDs and managing custom resource instances. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Custom Resource Definitions (CRDs) & API Extensions</li>
      <li><strong>Target Image / Workload:</strong> <code>crd</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W8D4: Custom Resource Definitions (CRDs) & API Extensions</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Creating CRDs and managing custom resource instances</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Custom Resource Definitions (CRDs) & API Extensions")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Custom Resource Definitions (CRDs) & API Extensions in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """
    <h3>CKAD Week 8 Day 5: CKAD killer.sh Mock Exam 1 (Timed Simulation)</h3>
    <p><strong>Overview:</strong> 16 Real-World Questions, 120 Minutes, Official Weights. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> CKAD killer.sh Mock Exam 1 (Timed Simulation)</li>
      <li><strong>Target Image / Workload:</strong> <code>mock-ckad-1</code></li>
      <li><strong>Target Time Limit:</strong> 120m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W8D5: CKAD killer.sh Mock Exam 1 (Timed Simulation)</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">16 Real-World Questions, 120 Minutes, Official Weights</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 120m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "CKAD killer.sh Mock Exam 1 (Timed Simulation)")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve CKAD killer.sh Mock Exam 1 (Timed Simulation) in under 120m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """
    <h3>CKAD Week 8 Day 6: CKAD killer.sh Mock Exam 2 (Timed Simulation)</h3>
    <p><strong>Overview:</strong> 16 Real-World Questions, 120 Minutes, Official Weights. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> CKAD killer.sh Mock Exam 2 (Timed Simulation)</li>
      <li><strong>Target Image / Workload:</strong> <code>mock-ckad-2</code></li>
      <li><strong>Target Time Limit:</strong> 120m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W8D6: CKAD killer.sh Mock Exam 2 (Timed Simulation)</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">16 Real-World Questions, 120 Minutes, Official Weights</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 120m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "CKAD killer.sh Mock Exam 2 (Timed Simulation)")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve CKAD killer.sh Mock Exam 2 (Timed Simulation) in under 120m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
