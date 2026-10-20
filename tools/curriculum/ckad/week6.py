"""
CKAD Curriculum Content: Week 6 (Days 1 to 6)
Services & Advanced Networking
"""
from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <h3>CKAD Week 6 Day 1: Services: ClusterIP, NodePort & TargetPort Matching</h3>
    <p><strong>Overview:</strong> Exposing pods and validating endpoints. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Services: ClusterIP, NodePort & TargetPort Matching</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W6D1: Services: ClusterIP, NodePort & TargetPort Matching</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Exposing pods and validating endpoints</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Services: ClusterIP, NodePort & TargetPort Matching")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Services: ClusterIP, NodePort & TargetPort Matching in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """
    <h3>CKAD Week 6 Day 2: Headless Services & StatefulSets Architecture</h3>
    <p><strong>Overview:</strong> clusterIP None with stable network identities. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Headless Services & StatefulSets Architecture</li>
      <li><strong>Target Image / Workload:</strong> <code>redis:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W6D2: Headless Services & StatefulSets Architecture</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">clusterIP None with stable network identities</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Headless Services & StatefulSets Architecture")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Headless Services & StatefulSets Architecture in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """
    <h3>CKAD Week 6 Day 3: NetworkPolicy: Ingress Isolation & Pod Selectors</h3>
    <p><strong>Overview:</strong> Restricting incoming traffic to database pods. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> NetworkPolicy: Ingress Isolation & Pod Selectors</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W6D3: NetworkPolicy: Ingress Isolation & Pod Selectors</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Restricting incoming traffic to database pods</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "NetworkPolicy: Ingress Isolation & Pod Selectors")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve NetworkPolicy: Ingress Isolation & Pod Selectors in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """
    <h3>CKAD Week 6 Day 4: NetworkPolicy: Egress Lockdown & DNS Resolution</h3>
    <p><strong>Overview:</strong> Default deny egress while allowing CoreDNS port 53. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> NetworkPolicy: Egress Lockdown & DNS Resolution</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W6D4: NetworkPolicy: Egress Lockdown & DNS Resolution</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Default deny egress while allowing CoreDNS port 53</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "NetworkPolicy: Egress Lockdown & DNS Resolution")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve NetworkPolicy: Egress Lockdown & DNS Resolution in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """
    <h3>CKAD Week 6 Day 5: Ingress Networking: Host, Path Rules & Rewrite Target</h3>
    <p><strong>Overview:</strong> Ingress controller routing /app and /api with rewrite. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Ingress Networking: Host, Path Rules & Rewrite Target</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W6D5: Ingress Networking: Host, Path Rules & Rewrite Target</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Ingress controller routing /app and /api with rewrite</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Ingress Networking: Host, Path Rules & Rewrite Target")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Ingress Networking: Host, Path Rules & Rewrite Target in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """
    <h3>CKAD Week 6 Day 6: Week 6 Milestone: Microservices Network Security Sandbox</h3>
    <p><strong>Overview:</strong> Securing multi-tier application with NetworkPolicies & Ingress. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Week 6 Milestone: Microservices Network Security Sandbox</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 45m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W6D6: Week 6 Milestone: Microservices Network Security Sandbox</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Securing multi-tier application with NetworkPolicies & Ingress</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 45m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Week 6 Milestone: Microservices Network Security Sandbox")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Week 6 Milestone: Microservices Network Security Sandbox in under 45m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
