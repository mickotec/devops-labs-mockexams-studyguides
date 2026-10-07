> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 2025 Updates Admission Controllers

> This article explores admission controllers in Kubernetes, focusing on their role in enhancing security and enforcing policies before object persistence.

In this lesson, we explore admission controllers in Kubernetes and understand how they enhance security and enforce policies before object persistence in etcd. Every operation performed using the kubectl command-line utility—such as creating a pod—is first sent as a request to the API server. The API server then processes the request and stores its information.

When a request reaches the API server, it is first handled by an authentication process. For instance, when using kubectl, the required certificates for authentication are provided in the KubeConfig file:

```bash theme={null}
cat ~/.kube/config
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVU...
```

After successful authentication, the request undergoes an authorization process using role-based access control (RBAC). For example, a role may be defined to allow specific operations on pods:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list", "get", "create", "update", "delete"]
```

This configuration permits a user assigned to the developer role to list, get, create, update, and delete pods. RBAC rules can be further refined to target specific resource names. For instance, to restrict a developer so they can only create pods with designated names:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["create"]
  resourceNames: ["blue", "orange"]
```

However, object-level permissions may not be sufficient in certain scenarios. When a pod creation request is received, you might need to inspect the configuration—for example, verifying that the pod does not use images from public registries, enforcing the use of a designated registry, or disallowing the "latest" tag. You might also enforce security policies, such as ensuring the container is not running as the root user or rejecting certain capability configurations. Consider the following pod specification:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu:latest
      command: ["sleep", "3600"]
      securityContext:
        runAsUser: 0
      capabilities:
        add: ["MAC_ADMIN"]
```

Standard RBAC rules operate only at the API level and cannot inspect or modify an object’s contents. This limitation is overcome by admission controllers, which validate or even mutate requests prior to persisting objects. Admission controllers can enforce specific policies, such as:

* Changing requests based on internal guidelines.
* Enforcing container image policies.
* Ensuring that certain metadata labels are always applied.

Kubernetes includes a variety of built-in admission controllers. Some common examples include:

* **Always Pull Images:** Forces the pod to pull images from the registry every time.
* **Default Storage Class:** Automatically adds a default storage class to PersistentVolumeClaims (PVCs) when none is provided.
* **Event Rate Limit:** Restricts the API server’s request-handling rate.
* **Namespace Exists:** Ensures that requested namespaces exist before proceeding.

## Namespace Admission Controllers

The namespace admission controller ensures that pods are created only in existing namespaces. For example, if you run:

```bash theme={null}
kubectl run nginx --image nginx --namespace blue
```

and if the "blue" namespace does not exist, you will receive an error like:

```bash theme={null}
Error from server (NotFound): namespaces "blue" not found
```

In this situation, after authentication and authorization, the namespace admission controller checks for the existence of the "blue" namespace and rejects the request since it does not exist.

Alternatively, Kubernetes offers the namespace auto-provision admission controller, which automatically creates a namespace if it does not exist (this feature is disabled by default). With the auto-provision controller enabled, executing the same command:

```bash theme={null}
kubectl run nginx --image nginx --namespace blue
```

results in the automatic creation of the "blue" namespace and a successful pod creation.

To view the admission controllers enabled by default, run:

```bash theme={null}
kube-apiserver -h | grep enable-admission-plugins
```

This command will list plugins such as NamespaceLifecycle, LimitRanger, ServiceAccount, TaintNodesByCondition, among others. If you are using a kubeadm-based setup, run the command within the kube-apiserver control plane pod using kubectl exec.

## Enabling Admission Controllers

To add an admission controller, update the --enable-admission-plugins flag on the Kube API server. In a kubeadm-based setup, this involves modifying the Kube API server manifest. For example, update the ExecStart command in the systemd service file as below:

```plaintext theme={null}
ExecStart=/usr/local/bin/kube-apiserver \\
  --advertise-address=${INTERNAL_IP} \\
  --allow-privileged=true \\
  --apiserver-count=3 \\
  --authorization-mode=Node,RBAC \\
  --bind-address=0.0.0.0 \\
  --enable-swagger-ui=true \\
  --etcd-servers=https://127.0.0.1:2379 \\
  --event-ttl=1h \\
  --runtime-config=api/all \\
  --service-cluster-ip-range=10.32.0.0/24 \\
  --service-node-port-range=30000-32767 \\
  --v=2 \\
  --enable-admission-plugins=NodeRestriction,NamespaceAutoProvision
```

For kubeadm-based setups where the API server runs as a pod, the manifest might look like this:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  name: kube-apiserver
  namespace: kube-system
spec:
  containers:
  - command:
    - kube-apiserver
    - --authorization-mode=Node,RBAC
    - --advertise-address=172.17.0.107
    - --allow-privileged=true
    - --enable-bootstrap-token-auth=true
    - --enable-admission-plugins=NodeRestriction,NamespaceAutoProvision
    image: k8s.gcr.io/kube-apiserver-amd64:v1.11.3
    name: kube-apiserver
```

To disable specific admission controller plugins, use the --disable-admission-plugins flag similarly.

After updating your configuration, running the following command in a non-existent namespace:

```bash theme={null}
kubectl run nginx --image nginx --namespace blue
```

should output:

```bash theme={null}
Pod/nginx created!
```

Verifying the available namespaces:

```bash theme={null}
kubectl get namespaces
```

will display:

```bash theme={null}
NAME         STATUS   AGE
blue         Active   3m
default      Active   23m
kube-public  Active   24m
kube-system  Active   24m
```

This demonstrates how admission controllers not only reject invalid requests but can also perform backend operations like automatically creating a namespace.

<Callout icon="lightbulb" color="#1CB2FE">
  Both the namespace auto-provision and namespace existence admission controllers are deprecated. They have been replaced by the namespace lifecycle admission controller, which enforces that requests to non-existent namespaces are rejected and protects default namespaces (default, kube-system, and kube-public) from deletion.
</Callout>

That’s it for now. Practice using admission controllers in your exercises to reinforce your learnings. See you in the next lesson!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/cd124bdf-9911-4cc1-8177-f2d8b6dfd2a0/lesson/30310f99-eca1-44a7-a564-ce20246e48eb" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/cd124bdf-9911-4cc1-8177-f2d8b6dfd2a0/lesson/d9398583-1f11-4b74-a8ee-2bc0790f3193" />
</CardGroup>
