"""
CKAD Curriculum Content: Week 7 (Days 1 to 6)
State Persistence & Modern App Tooling
"""
from .svg_helpers import wrap_svg, card, code_box, arrow

def get_day_1():
    theory = """
    <h3>CKAD Week 7 Day 1: Volume Types: emptyDir & hostPath In-Depth</h3>
    <p><strong>Overview:</strong> Ephemeral storage and node filesystem sharing. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Volume Types: emptyDir & hostPath In-Depth</li>
      <li><strong>Target Image / Workload:</strong> <code>busybox:1.36</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W7D1: Volume Types: emptyDir & hostPath In-Depth</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Ephemeral storage and node filesystem sharing</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Volume Types: emptyDir & hostPath In-Depth")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Volume Types: emptyDir & hostPath In-Depth in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """
    <h3>CKAD Week 7 Day 2: PersistentVolumes & PersistentVolumeClaims</h3>
    <p><strong>Overview:</strong> Static volume provisioning and ReadWriteOnce binding. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> PersistentVolumes & PersistentVolumeClaims</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W7D2: PersistentVolumes & PersistentVolumeClaims</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Static volume provisioning and ReadWriteOnce binding</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "PersistentVolumes & PersistentVolumeClaims")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve PersistentVolumes & PersistentVolumeClaims in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """
    <h3>CKAD Week 7 Day 3: StorageClasses & Dynamic Volume Provisioning</h3>
    <p><strong>Overview:</strong> Configuring storage classes and PVC claim expansion. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> StorageClasses & Dynamic Volume Provisioning</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 25m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W7D3: StorageClasses & Dynamic Volume Provisioning</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Configuring storage classes and PVC claim expansion</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 25m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "StorageClasses & Dynamic Volume Provisioning")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve StorageClasses & Dynamic Volume Provisioning in under 25m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """
    <h3>CKAD Week 7 Day 4: Helm Fundamentals: Repos, Releases & Values Overrides</h3>
    <p><strong>Overview:</strong> helm repo, install, upgrade, and rollback with custom values. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Helm Fundamentals: Repos, Releases & Values Overrides</li>
      <li><strong>Target Image / Workload:</strong> <code>helm</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W7D4: Helm Fundamentals: Repos, Releases & Values Overrides</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">helm repo, install, upgrade, and rollback with custom values</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Helm Fundamentals: Repos, Releases & Values Overrides")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Helm Fundamentals: Repos, Releases & Values Overrides in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """
    <h3>CKAD Week 7 Day 5: Kustomize Basics: Overlays, Patches & Transformers</h3>
    <p><strong>Overview:</strong> base and overlays (dev/prod) with commonLabels and patches. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Kustomize Basics: Overlays, Patches & Transformers</li>
      <li><strong>Target Image / Workload:</strong> <code>kustomize</code></li>
      <li><strong>Target Time Limit:</strong> 30m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W7D5: Kustomize Basics: Overlays, Patches & Transformers</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">base and overlays (dev/prod) with commonLabels and patches</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 30m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Kustomize Basics: Overlays, Patches & Transformers")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Kustomize Basics: Overlays, Patches & Transformers in under 30m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """
    <h3>CKAD Week 7 Day 6: Week 7 Milestone: Declarative GitOps Kustomize Stack</h3>
    <p><strong>Overview:</strong> Deploying multi-environment application overlay with PVC. In the Certified Kubernetes Application Developer (CKAD) exam, speed and precision are paramount. Candidates must understand containerized runtime concepts, declarative YAML specifications, and imperative kubectl CLI shortcuts.</p>
    <ul>
      <li><strong>Core Competency:</strong> Week 7 Milestone: Declarative GitOps Kustomize Stack</li>
      <li><strong>Target Image / Workload:</strong> <code>nginx:alpine</code></li>
      <li><strong>Target Time Limit:</strong> 45m</li>
    </ul>
    """
    svg = wrap_svg(800, 180, """
    <rect x="40" y="30" width="720" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="65" y="65" fill="#38bdf8" font-size="14" font-weight="bold">CKAD W7D6: Week 7 Milestone: Declarative GitOps Kustomize Stack</text>
    <text x="65" y="95" fill="#f8fafc" font-size="12">Deploying multi-environment application overlay with PVC</text>
    <text x="65" y="125" fill="#94a3b8" font-size="11">Time: 45m • Focus: Application Development &amp; Cloud Native Architecture</text>
    """, "Week 7 Milestone: Declarative GitOps Kustomize Stack")
    aliases = "alias k='kubectl'\\nalias kdry='kubectl --dry-run=client -o yaml'"
    checklist = [
        ("CKAD", "Can you solve Week 7 Milestone: Declarative GitOps Kustomize Stack in under 45m?", "Review scenario and solution guide"),
        ("CKAD", "Can you verify requirements using kubectl jsonpath/custom-columns?", "Use -o jsonpath or -o custom-columns")
    ]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
