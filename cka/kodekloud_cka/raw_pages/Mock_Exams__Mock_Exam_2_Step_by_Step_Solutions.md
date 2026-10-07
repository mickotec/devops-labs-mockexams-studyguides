> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mock Exam 2 Step by Step Solutions

> This article provides step-by-step solutions for Kubernetes cluster configuration and troubleshooting across various scenarios.

This article provides detailed step-by-step solutions for Mock Exam Two. Each question covers a key aspect of Kubernetes cluster configuration—from creating storage classes and deployments to configuring ingress, RBAC, network policies, HPA setups, and troubleshooting common issues. Follow the solutions below to configure your clusters and gain hands-on experience with Kubernetes.

***

## Question 1 – Creating a Default Local StorageClass

In this question, you will create a StorageClass named **local-sc** on Cluster One's control plane. This StorageClass must be set as the default with the following criteria:

1. SSH into your control plane:

   ```plaintext theme={null}
   ssh cluster1-controlplane
   Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-1078-gcp x86_64)
    * Documentation: https://help.ubuntu.com/
    * Management: https://landscape.canonical.com
    * Support: https://ubuntu.com/pro

   This system has been minimized by removing packages and content that are not required on a system that users do not log into.
   To restore this content, you can run the 'unminimize' command.
   ```

2. Referencing the documentation, copy the example configuration and update it as follows:
   * Change the `name` to **local-sc**.
   * Update the annotation `storageclass.kubernetes.io/is-default-class` to `"true"`.
   * Set the `provisioner` to `kubernetes.io/no-provisioner`.
   * Remove any unnecessary fields (such as `reclaimPolicy` and `mountOptions`) not specified.
   * Retain only `allowVolumeExpansion` and `volumeBindingMode: WaitForFirstConsumer`.

The final YAML configuration should look like this:

```yaml theme={null}
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-sc
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/no-provisioner
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

After saving the file (e.g., as `question1.yaml`), apply the configuration:

```bash theme={null}
kubectl apply -f question1.yaml
```

You should see the following confirmation:

```plaintext theme={null}
storageclass.storage.k8s.io/local-sc created
```

***

## Question 2 – Deployment with App and Sidecar Containers for Logging

This question guides you through creating a deployment named **logging-deployment** in the `logging-ns` namespace. The deployment uses one replica and runs two containers within the same pod:

* **app-container**: Uses the busybox image to continuously append log entries to `/var/log/app/app.log`.
* **log-agent**: Also based on busybox, this container tails the same log file.

Both containers share an `emptyDir` volume mounted at `/var/log/app`.

Below is the complete YAML configuration (save as `question2.yaml`):

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: logging-deployment
  namespace: logging-ns
spec:
  replicas: 1
  selector:
    matchLabels:
      app: logger
  template:
    metadata:
      labels:
        app: logger
    spec:
      volumes:
        - name: log-volume
          emptyDir: {}
      containers:
      - name: app-container
        image: busybox
        command:
          - sh
          - -c
          - "while true; do echo 'Log entry' >> /var/log/app/app.log; sleep 5; done"
        volumeMounts:
          - name: log-volume
            mountPath: /var/log/app
      - name: log-agent
        image: busybox
        command:
          - tail
          - -f
          - /var/log/app/app.log
```

Apply the configuration:

```bash theme={null}
kubectl apply -f question2.yaml
```

Next, verify that the pod is running and inspect its logs:

```bash theme={null}
kubectl get pod -n logging-ns
kubectl logs <pod-name> -c log-agent -n logging-ns
```

You should see repeated "Log entry" outputs confirming that the log file is being written and tailed properly.

***

## Question 3 – Creating an Ingress Resource to Route Traffic

Here, you will create an Ingress resource named **webapp-ingress** in the `ingress-ns` namespace. This ingress routes traffic to a service called **webapp-svc**, using the NGINX ingress controller with the following criteria:

* Hostname: `kodekloud-ingress.app`
* Path: `/` (with `PathType: Prefix`)
* Forward traffic to **webapp-svc** on port 80

Below is the YAML configuration (save as `question3.yaml`):

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp-ingress
  namespace: ingress-ns
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: kodekloud-ingress.app
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: webapp-svc
            port:
              number: 80
```

Apply the configuration:

```bash theme={null}
kubectl apply -f question3.yaml
```

Test the ingress setup by sending an HTTP request:

```bash theme={null}
curl -s http://kodekloud-ingress.app/
```

You should see the default NGINX welcome page, confirming correct configuration.

***

## Question 4 – Updating an Nginx Deployment with Rolling Updates

In this question, create a deployment named **nginx-deploy** using **nginx:1.16** and then perform a rolling update to upgrade the image to **nginx:1.17**.

1. Generate an initial deployment YAML using a dry run:

   ```bash theme={null}
   kubectl create deployment nginx-deploy --image=nginx:1.16 --dry-run=client -o yaml > question4.yaml
   ```

   The generated YAML will be similar to:

   ```yaml theme={null}
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-deploy
     labels:
       app: nginx-deploy
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: nginx-deploy
     template:
       metadata:
         labels:
           app: nginx-deploy
       spec:
         containers:
         - name: nginx
           image: nginx:1.16
           resources: {}
   ```

2. Apply the deployment:

   ```bash theme={null}
   kubectl apply -f question4.yaml
   ```

3. Update the image to version 1.17 using a rolling update:

   ```bash theme={null}
   kubectl set image deployment/nginx-deploy nginx=nginx:1.17
   ```

4. Verify the rollout history:

   ```bash theme={null}
   kubectl rollout history deployment nginx-deploy
   kubectl rollout history deployment nginx-deploy --revision=2
   ```

The output should indicate that revision 2 is using **nginx:1.17**.

***

## Question 5 – Creating a User via CSR and Configuring RBAC

This question has two parts:

### Part A: Create a CertificateSigningRequest (CSR) for User "john"

1. The private key is located at `/root/cka/john.key` and the CSR file at `/root/cka/john.csr`. Base64 encode the CSR file content for use in your CSR object.
2. The CSR object should use the signer `kubernetes.io/kube-apiserver-client` and specify these usages: `digital signature`, `key encipherment`, and `client auth`.

Example CSR YAML (save as `question5.yaml`):

```yaml theme={null}
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: john-developer
spec:
  signerName: kubernetes.io/kube-apiserver-client
  request: <BASE64_ENCODED_CONTENT_OF_/root/cka/john.csr>
  usages:
    - digital signature
    - key encipherment
    - client auth
```

To obtain the Base64 encoded CSR, run:

```bash theme={null}
cat /root/cka/john.csr | base64 | tr -d '\n'
```

Apply the CSR:

```bash theme={null}
kubectl apply -f question5.yaml
```

Approve the CSR:

```bash theme={null}
kubectl certificate approve john-developer
```

### Part B: Grant RBAC Permissions with Role and RoleBinding

Create a Role named **developer** in the `development` namespace to allow the following verbs on `pods`: `create`, `list`, `get`, `update`, and `delete`. Then, bind the role to user **john**.

Save the following YAML as `question5-rbac.yaml`:

```yaml theme={null}
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
  namespace: development
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["create", "list", "get", "update", "delete"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: john-developer-role-binding
  namespace: development
subjects:
- kind: User
  name: john
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io
```

Apply the RBAC configuration:

```bash theme={null}
kubectl apply -f question5-rbac.yaml
```

Test the permissions by running:

```bash theme={null}
kubectl auth can-i create pods --as=john -n development
```

A response of **yes** confirms that the RBAC configuration is working.

***

## Question 6 – Creating an Nginx Pod with an Internal Service and DNS Testing

In this exercise, you will deploy an Nginx pod named **nginx-resolver** and expose it internally using a ClusterIP service named **nginx-resolver-service**. Then you will verify DNS resolution using a BusyBox pod.

1. Create the Nginx pod:

   ```bash theme={null}
   kubectl run nginx-resolver --image=nginx
   ```

2. Expose the pod internally:

   ```bash theme={null}
   kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP
   ```

3. Verify the service endpoints:

   ```bash theme={null}
   kubectl get svc nginx-resolver-service
   kubectl get pod -o wide
   ```

4. Run a temporary BusyBox pod to perform an nslookup:

   ```bash theme={null}
   kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service
   ```

Optionally, redirect the DNS lookup results to a file (e.g., `/root/cka/nginx.svc`) if necessary. Remember that Kubernetes creates DNS entries for both pods and services.

***

## Question 7 – Creating a Static Pod

Create a static pod named **nginx-critical** on Node One. This pod should automatically restart on failure and must reside in the `/etc/kubernetes/manifests` directory.

1. Generate a pod YAML definition via dry run:

   ```bash theme={null}
   kubectl run nginx-critical --image=nginx --restart=Always --dry-run=client -o yaml > static.yaml
   ```

2. SSH into Node One:

   ```bash theme={null}
   ssh cluster1-node01
   ```

3. Place the YAML file into `/etc/kubernetes/manifests/static.yaml` with contents similar to:

   ```yaml theme={null}
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx-critical
     labels:
       run: nginx-critical
   spec:
     containers:
     - name: nginx-critical
       image: nginx
     dnsPolicy: ClusterFirst
     restartPolicy: Always
   ```

The kubelet will automatically create the static pod. Verify its status:

```bash theme={null}
kubectl get pod -o wide
```

***

## Question 8 – Creating a Horizontal Pod Autoscaler (HPA)

Create an HPA for a deployment named **backend-deployment** in the `backend` namespace. The HPA should target an average memory utilization of 65% across all pods, with a minimum of 3 replicas and a maximum of 15.

Below is the example HPA YAML (save as `webapp-hpa.yaml`):

```yaml theme={null}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: backend-hpa
  namespace: backend
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend-deployment
  minReplicas: 3
  maxReplicas: 15
  metrics:
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 65
```

Apply the HPA configuration:

```bash theme={null}
kubectl apply -f webapp-hpa.yaml
```

Verify the HPA details:

```bash theme={null}
kubectl describe hpa -n backend
```

***

## Question 9 – Troubleshooting a Non-Responsive API Server

If Cluster Two fails to respond to `kubectl` commands (e.g., with the error message "The connection to the server cluster2-controlplane:6443 was refused"), perform the following steps:

1. Run a command such as:

   ```bash theme={null}
   kubectl get nodes
   ```

   which may yield:

   ```plaintext theme={null}
   The connection to the server cluster2-controlplane:6443 was refused - did you specify the right host or port?
   ```

2. Use `crictl pods` to check the running containers and notice that the API server container is missing.

3. Verify the kubelet status:

   ```bash theme={null}
   sudo systemctl status kubelet
   ```

   If it is inactive, start and enable the kubelet:

   ```bash theme={null}
   sudo systemctl start kubelet
   sudo systemctl enable kubelet
   ```

After starting the kubelet, the API server container should be recreated. Confirm by running:

```bash theme={null}
kubectl get nodes
```

***

## Question 10 – Modifying the Web Gateway for HTTPS

Modify the existing web gateway in the `cka5673` namespace on Cluster One so that it handles HTTPS traffic on port 443 for `kodekloud.com` using TLS certificates stored in the **kodekloud-tls** secret.

1. Verify that the secret exists:

   ```bash theme={null}
   kubectl get secret -n cka5673
   ```

2. Retrieve the current gateway configuration:

   ```bash theme={null}
   kubectl get gateway -n cka5673 -o yaml > question10.yaml
   ```

3. Edit the YAML file to update the listener section. Change to the following:

   ```yaml theme={null}
   listeners:
   - name: https
     port: 443
     protocol: HTTPS
     hostname: kodekloud.com
     tls:
       certificateRefs:
       - name: kodekloud-tls
   ```

4. Apply the updated configuration:

   ```bash theme={null}
   kubectl apply -f question10.yaml
   ```

***

## Question 11 – Uninstalling a Vulnerable Helm Release

Identify and uninstall the Helm release that uses the vulnerable image `kodekloud/webapp-color:v1`.

1. List all Helm releases across namespaces:

   ```bash theme={null}
   helm list -A
   ```

2. Search for the vulnerable image in each release’s manifests:

   ```bash theme={null}
   helm get manifest <release-name> -n <namespace> | grep -i kodekloud/webapp-color:v1
   ```

3. Once identified (for example, if the release is named `atlanta-page-apd` in the `atlanta-page-04` namespace), uninstall it:

   ```bash theme={null}
   helm uninstall atlanta-page-apd -n atlanta-page-04
   ```

This action removes the vulnerable release from your cluster.

***

## Question 12 – Applying a Network Policy

Implement a network policy that allows traffic from frontend applications (namespace `frontend`) to backend applications (namespace `backend`), while blocking traffic from the databases (namespace `databases`).

After reviewing the provided policies, **net-pol-3.yaml** is the correct choice. Its contents are as follows:

```yaml theme={null}
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: net-policy-3
  namespace: backend
spec:
  podSelector: {}
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend
  ports:
  - protocol: TCP
    port: 80
```

Apply the policy without affecting any other existing policies:

```bash theme={null}
kubectl apply -f net-pol-3.yaml
```

***

## Question 13 – Troubleshooting a Failed Deployment Due to Resource Quota

On Cluster Three, if the **backend-api** deployment fails to scale to three replicas due to resource quota limitations, follow these troubleshooting steps:

1. Describe the deployment to see error events:

   ```bash theme={null}
   kubectl describe deployment backend-api
   ```

   Also check the ReplicaSets for error events indicating that pod creation is forbidden by resource quotas.

2. Describe the resource quota:

   ```bash theme={null}
   kubectl describe resourcequota cpu-mem-quota
   ```

   An example output might be:

   ```plaintext theme={null}
   Name:            cpu-mem-quota
   Namespace:       default
   Resource         Used     Hard
   ------------------------------
   requests.cpu     200m     300m
   requests.memory  256Mi    300Mi
   ```

   If the new pod’s request (e.g., 128Mi) exceeds the quota, adjustments are needed.

3. Update the deployment’s resource requests to ensure the total for three replicas remains within the limits. For instance, reduce the memory request from `128Mi` to `100Mi`:

   ```yaml theme={null}
   resources:
     requests:
       cpu: 100m
       memory: 100Mi
     limits:
       cpu: 150m
       memory: 150Mi
   ```

4. Update the deployment using editing or applying a modified YAML, and if necessary, delete the problematic ReplicaSet to trigger a new rollout:

   ```bash theme={null}
   kubectl edit deployment backend-api
   kubectl delete rs <offending-replicaset>
   ```

After the changes, all three pods should start and run successfully.

***

## Question 14 – Deploying Calico CNI with a Custom CIDR

On Cluster Four, deploy Calico as your CNI provider. Use the official Calico custom-resources YAML from GitHub and modify the CIDR to `172.17.0.0/16`.

1. Download the custom-resources file:

   ```bash theme={null}
   curl -O https://raw.githubusercontent.com/projectcalico/calico/v3.29.2/manifests/custom-resources.yaml
   ```

2. Edit the downloaded YAML file. Locate the Calico IP pool definition and update the `cidr` value as shown below:

   ```yaml theme={null}
   apiVersion: operator.tigera.io/v1
   kind: Installation
   metadata:
     name: default
   spec:
     calicoNetwork:
       ipPools:
       - name: default-ip4-ipool
         blockSize: 26
         cidr: 172.17.0.0/16
         encapsulation: VXLANCrossSubnet
         natOutgoing: Enabled
         nodeSelector: all
   ```

3. Apply the modified configuration:

   ```bash theme={null}
   kubectl apply -f custom-resources.yaml
   ```

4. To verify that Calico is operating correctly and pod-to-pod communication works, deploy a test pod (such as an Nginx pod) and use a BusyBox or net-tools container for connectivity tests:

   ```bash theme={null}
   kubectl run web-app --image=nginx
   kubectl run test --rm -it --image=jrcs/net-tools --restart=Never -- sh -c "curl -s <web-app-pod-IP>"
   ```

If the connectivity test is successful, Calico is configured and running correctly.

***

<Callout icon="lightbulb" color="#1CB2FE">
  This article provides a comprehensive walkthrough of essential Kubernetes configurations and troubleshooting steps. By following these step-by-step solutions, you can better understand Kubernetes components and improve your operational skills.
</Callout>

Happy learning and good luck on your Kubernetes journey!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/d33baa6d-ccd3-410b-a20c-5d5b9c7a2114/lesson/458a15d9-47dd-4d8d-b497-671db87a9e70" />
</CardGroup>
