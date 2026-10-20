"""CKAD Curriculum Content: Week 7
Week 7: State Persistence & Storage
"""

def get_day_1():
    theory = """<p><code>emptyDir</code> provides pod-lifecycle temporary storage (or RAM tmpfs). <code>hostPath</code> mounts node filesystem directories.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 7 Day 1: Ephemeral Storage: emptyDir & Node-Bound hostPath Volumes</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kvol='kubectl explain pod.spec.volumes'"""
    checklist = [('CKAD', 'Mount an emptyDir with medium: Memory for in-memory cache', 'emptyDir: {medium: Memory}')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_2():
    theory = """<p>PersistentVolumes represent cluster-wide provisioned storage with accessModes (<code>RWO</code>, <code>ROX</code>, <code>RWX</code>) and reclaim policies (<code>Retain</code>, <code>Delete</code>).</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 7 Day 2: Persistent Volumes (PVs): AccessModes & Reclaim Policies</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgpv='kubectl get pv'"""
    checklist = [('CKAD', 'Create PersistentVolume with specific capacity and accessModes', 'kubectl explain pv.spec')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_3():
    theory = """<p>PersistentVolumeClaims request storage capacity and accessModes, binding to matching available PersistentVolumes.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 7 Day 3: Persistent Volume Claims (PVCs): Storage Requests & Binding</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgpvc='kubectl get pvc'"""
    checklist = [('CKAD', 'Create PersistentVolumeClaim matching PV storage and accessModes', 'kubectl explain pvc.spec')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_4():
    theory = """<p>Mounting PVCs in pod specs preserves file state across pod deletions and restarts.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 7 Day 4: Consuming PVCs in Pods & Data Persistence Verification</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kpvcvol='kubectl explain pod.spec.volumes.persistentVolumeClaim'"""
    checklist = [('CKAD', 'Mount a PersistentVolumeClaim into a Pod container', 'volumes: [{name: v, persistentVolumeClaim: {claimName: c}}]')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_5():
    theory = """<p>StorageClasses define provisioners and volume binding modes (<code>Immediate</code> vs <code>WaitForFirstConsumer</code>).</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 7 Day 5: StorageClasses & Dynamic Volume Provisioning</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgsc='kubectl get sc'"""
    checklist = [('CKAD', 'Inspect StorageClass parameters and volumeBindingMode', 'kubectl describe sc')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_6():
    theory = """<p>StatefulSets provide stable network identities and automatically generate dedicated PVCs for each replica via <code>volumeClaimTemplates</code>.</p>"""
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
  <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Week 7 Day 6: StatefulSets & VolumeClaimTemplates Architecture</text>
  <rect x="40" y="65" width="380" height="160" rx="9" fill="url(#cardDark)" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="60" y="100" fill="#38bdf8" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">Kubernetes Cluster Workload</text>
  <text x="60" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Target: VirtualBox Nodes (controlplane, node01, node02)</text>
  <rect x="470" y="65" width="390" height="160" rx="9" fill="url(#cardDark)" stroke="#34d399" stroke-width="1.5"/>
  <text x="490" y="100" fill="#34d399" font-size="14" font-weight="bold" font-family="-apple-system, sans-serif">CKAD Verification &amp; Orchestration</text>
  <text x="490" y="130" fill="#94a3b8" font-size="11" font-family="-apple-system, sans-serif">Automated grading via: ./lab check &lt;scenario&gt;</text>
</svg>"""
    aliases = """alias kgsts='kubectl get statefulset'"""
    checklist = [('CKAD', 'Deploy StatefulSet paired with Headless Service', 'kubectl explain sts.spec.serviceName')]
    return {"theory_html": theory, "svg": svg, "aliases": aliases, "checklist": checklist}

def get_day_content(day: int) -> dict:
    dispatch = {1: get_day_1, 2: get_day_2, 3: get_day_3, 4: get_day_4, 5: get_day_5, 6: get_day_6}
    return dispatch.get(day, get_day_1)()
