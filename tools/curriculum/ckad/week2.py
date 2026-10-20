"""
CKAD Curriculum Content: Week 2 (Days 1 to 6)
Configuration & Security Primitives
"""
from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <h3>CKAD Week 2 Day 1: Container Commands & Arguments Overrides</h3>
    <p><strong>Overview:</strong> Overriding entrypoint and cmd via command and args. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Container Commands & Arguments Overrides</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W2D1: Container Commands & Arguments Overrides</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Overriding entrypoint and cmd via command and args</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Container Commands & Arguments Overrides")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Container Commands & Arguments Overrides in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """
    <h3>CKAD Week 2 Day 2: ConfigMaps from Literals, Files & Env Injection</h3>
    <p><strong>Overview:</strong> Injecting configuration as env and volume mounts. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> ConfigMaps from Literals, Files & Env Injection</li>
      <li><strong>Target Image / Workload:</strong> <code>alpine:3.19</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W2D2: ConfigMaps from Literals, Files & Env Injection</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Injecting configuration as env and volume mounts</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "ConfigMaps from Literals, Files & Env Injection")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve ConfigMaps from Literals, Files & Env Injection in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """
    <h3>CKAD Week 2 Day 3: Secrets Creation, Base64 & Safe Mounting</h3>
    <p><strong>Overview:</strong> Opaque secrets, TLS secrets, and read-only mounts. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Secrets Creation, Base64 & Safe Mounting</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W2D3: Secrets Creation, Base64 & Safe Mounting</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Opaque secrets, TLS secrets, and read-only mounts</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Secrets Creation, Base64 & Safe Mounting")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Secrets Creation, Base64 & Safe Mounting in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """
    <h3>CKAD Week 2 Day 4: SecurityContexts: UID, GID & Linux Capabilities</h3>
    <p><strong>Overview:</strong> runAsUser, runAsGroup, fsGroup, drop ALL, add NET_ADMIN. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> SecurityContexts: UID, GID & Linux Capabilities</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W2D4: SecurityContexts: UID, GID & Linux Capabilities</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">runAsUser, runAsGroup, fsGroup, drop ALL, add NET_ADMIN</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "SecurityContexts: UID, GID & Linux Capabilities")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve SecurityContexts: UID, GID & Linux Capabilities in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """
    <h3>CKAD Week 2 Day 5: ServiceAccounts & Token Auto-mount Policies</h3>
    <p><strong>Overview:</strong> Custom ServiceAccount association and automount token false. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> ServiceAccounts & Token Auto-mount Policies</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W2D5: ServiceAccounts & Token Auto-mount Policies</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Custom ServiceAccount association and automount token false</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "ServiceAccounts & Token Auto-mount Policies")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve ServiceAccounts & Token Auto-mount Policies in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """
    <h3>CKAD Week 2 Day 6: Week 2 Milestone: Hardened Workload Configuration</h3>
    <p><strong>Overview:</strong> Secure Pod with SA, Secret env, and readOnly root. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Week 2 Milestone: Hardened Workload Configuration</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 40m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W2D6: Week 2 Milestone: Hardened Workload Configuration</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Secure Pod with SA, Secret env, and readOnly root</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 40m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Week 2 Milestone: Hardened Workload Configuration")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Week 2 Milestone: Hardened Workload Configuration in under 40m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
