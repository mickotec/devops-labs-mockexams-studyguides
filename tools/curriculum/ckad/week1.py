"""CKAD Curriculum Content: Week 1
Week 1: Core Concepts & Pod Architecture
"""

def get_day_1():
    theory = """<p>In Kubernetes, the <strong>Pod</strong> is the smallest deployable compute unit, encapsulating one or more application containers with shared network IP and storage.</p>
<ul>
  <li><strong>Atomic Scheduling:</strong> All containers in a single Pod are co-located and co-scheduled on the same node.</li>
  <li><strong>Shared Resources:</strong> Containers share an IP address and port space (communicating via <code>localhost</code>) and can share volumes via <code>emptyDir</code>.</li>
  <li><strong>Four YAML Root Keys:</strong> <code>apiVersion</code>, <code>kind</code>, <code>metadata</code>, and <code>spec</code>.</li>
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 1 Day 1: Pod Architecture, YAML Basics & Creating Pods</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias k='kubectl'\nalias krun='kubectl run --dry-run=client -o yaml'\nexport do='--dry-run=client -o yaml'"""
    checklist = [('CKAD', 'Understand the four top-level YAML keys (apiVersion, kind, metadata, spec)', 'kubectl explain pod'), ('CKAD', 'Create Pod manifest imperatively without starting the container', 'kubectl run web --image=nginx $do > pod.yaml'), ('CKAD', 'Configure two containers sharing an emptyDir volume in a single Pod', 'kubectl explain pod.spec.volumes.emptyDir')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """<p>Kubernetes Pod specifications are largely <strong>immutable</strong> after creation. Except for image, activeDeadlineSeconds, and tolerations, modifying a pod requires recreating it.</p>
<ul>
  <li><strong>ENTRYPOINT vs Command:</strong> Docker's <code>ENTRYPOINT</code> maps to Kubernetes <code>spec.containers[*].command</code>.</li>
  <li><strong>CMD vs Args:</strong> Docker's <code>CMD</code> maps to Kubernetes <code>spec.containers[*].args</code>.</li>
  <li><strong>Fast Replacement:</strong> Use <code>kubectl replace --force -f &lt;file&gt;</code> to cleanly delete and recreate modified pods.</li>
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 1 Day 2: Editing Pods & Container Entrypoint/Command Overrides</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kreplace='kubectl replace --force -f'\nexport now='--grace-period=0 --force'"""
    checklist = [('CKAD', 'Distinguish command (ENTRYPOINT) vs args (CMD) in Kubernetes', 'kubectl explain pod.spec.containers.command'), ('CKAD', 'Replace a running pod with modified commands without hanging', 'kubectl replace --force -f /tmp/pod.yaml')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """<p>A <strong>ReplicaSet</strong> ensures a specified number of identical pod replicas are running at any given time.</p>
<ul>
  <li><strong>MatchLabels Equality:</strong> The ReplicaSet controller identifies pods using <code>spec.selector.matchLabels</code>.</li>
  <li><strong>Adoption &amp; Orphan Lifecycle:</strong> A ReplicaSet acquires any running pod matching its selector. Changing a pod's label orphans it from the ReplicaSet.</li>
  <li><strong>Scaling:</strong> Scale replica count instantly via <code>kubectl scale rs &lt;name&gt; --replicas=&lt;n&gt;</code>.</li>
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 1 Day 3: ReplicaSets, Selectors & Label Matching</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgrs='kubectl get rs'\nalias kscale='kubectl scale'"""
    checklist = [('CKAD', 'Understand matchLabels validation against template labels', 'kubectl explain rs.spec.selector'), ('CKAD', 'Scale a ReplicaSet imperatively using kubectl scale', 'kubectl scale rs frontend-rs --replicas=5')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """<p><strong>Deployments</strong> provide declarative updates for Pods and ReplicaSets, handling automated zero-downtime rolling updates.</p>
<ul>
  <li><strong>Rolling Updates:</strong> Updating the pod template triggers a rolling update with <code>maxSurge</code> and <code>maxUnavailable</code> controls.</li>
  <li><strong>Rollout Management:</strong> Check status with <code>kubectl rollout status</code> and rollback with <code>kubectl rollout undo</code>.</li>
  <li><strong>Declarative Manifests:</strong> Generate Deployment manifests with <code>kubectl create deployment web --image=nginx:1.24 $do</code>.</li>
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 1 Day 4: Deployments, Rolling Updates & Declarative Rollouts</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgd='kubectl get deploy'\nalias kroll='kubectl rollout status deployment'"""
    checklist = [('CKAD', 'Create deployment imperatively with image and replicas', 'kubectl create deploy api --image=nginx:1.24 --replicas=3'), ('CKAD', 'Roll back a failed deployment update to previous revision', 'kubectl rollout undo deploy/api')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """<p><strong>Namespaces</strong> provide virtual cluster isolation for resource grouping, multi-tenancy, and quota enforcement.</p>
<ul>
  <li><strong>Cross-Namespace DNS:</strong> Pods communicate across namespaces using CoreDNS FQDN: <code>&lt;service&gt;.&lt;namespace&gt;.svc.cluster.local</code>.</li>
  <li><strong>Context Switching:</strong> Change active namespace via <code>kubectl config set-context --current --namespace=&lt;target-ns&gt;</code>.</li>
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 1 Day 5: Namespaces, Isolation & Cross-Namespace DNS</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kns='kubectl config set-context --current --namespace'\nalias kgns='kubectl get ns'"""
    checklist = [('CKAD', 'Create namespaces imperatively via kubectl', 'kubectl create ns dev && kubectl create ns prod'), ('CKAD', 'Reach a service across namespaces using full FQDN', 'curl http://backend.prod.svc.cluster.local:80')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """<p>Mastering imperative commands, JSONPath queries, and recursive documentation is vital for CKAD exam speed.</p>
<ul>
  <li><strong>Fast Generation:</strong> Combine <code>--dry-run=client -o yaml</code> on run, create, and expose commands.</li>
  <li><strong>JSONPath Extraction:</strong> Extract specific fields with <code>-o jsonpath='{.items[*].metadata.name}'</code>.</li>
  <li><strong>Offline Documentation:</strong> Explore API structures using <code>kubectl explain --recursive</code>.</li>
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 1 Day 6: Imperative Commands, Output Formatting & kubectl explain</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """export do='--dry-run=client -o yaml'\nexport now='--grace-period=0 --force'\nalias ke='kubectl explain'"""
    checklist = [('CKAD', 'Generate Pod and Deployment manifests using --dry-run=client -o yaml', 'kubectl run test --image=redis $do'), ('CKAD', 'Extract nested fields using jsonpath filter queries', "kubectl get pods -o jsonpath='{.items[0].status.podIP}'")]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
