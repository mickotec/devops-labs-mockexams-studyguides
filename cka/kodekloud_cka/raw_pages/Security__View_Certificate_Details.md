> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# View Certificate Details

> Learn to inspect and verify certificates in a Kubernetes cluster, covering both manual setups and automated configurations like kubeadm.

Hello, and welcome to this lesson. In this guide, you will learn how to inspect and verify certificates in an existing Kubernetes cluster. Imagine joining a new team responsible for a Kubernetes environment where you need to perform a health check on cluster certificates due to reported issues. This lesson covers both manually set-up clusters and those configured using automated tools like kubeadm.

## Understanding Your Cluster Setup

Before diving into certificate verification, it’s important to understand your cluster’s setup. There are several methods for deploying a Kubernetes cluster, and each has its own approach to generating and managing certificates.

* If you deploy a cluster from scratch, you may generate and configure all certificates manually (as explored in a previous lesson).
* If you use an automated provisioning tool like kubeadm, certificate generation and configuration are handled for you. In this case, Kubernetes components are deployed as pods instead of OS services.

### Native Service Deployment

When Kubernetes components are deployed as native services, you can review service files to understand the certificate configuration. For example, inspect the kube-apiserver service file:

```bash theme={null}
cat /etc/systemd/system/kube-apiserver.service
[Service]
ExecStart=/usr/local/bin/kube-apiserver \\
  --advertise-address=172.17.0.32 \\
  --allow-privileged=true \\
  --apiserver-count=3 \\
  --authorization-mode=Node,RBAC \\
  --bind-address=0.0.0.0 \\
  --client-ca-file=/var/lib/kubernetes/ca.pem \\
  --enable-swagger-ui=true \\
  --etcd-cafile=/var/lib/kubernetes/ca.pem \\
  --etcd-certfile=/var/lib/kubernetes/kubernetes.pem \\
  --etcd-keyfile=/var/lib/kubernetes/kubernetes-key.pem \\
  --event-ttl=1h \\
  --kubelet-certificate-authority=/var/lib/kubernetes/ca.pem \\
  --kubelet-client-certfile=/var/lib/kubernetes/kubelet-client.crt \\
  --kubelet-client-key=/var/lib/kubernetes/kubelet-client.key \\
  --kubelet-https=true \\
  --service-node-port-range=30000-32767 \\
  --tls-cert-file=/var/lib/kubernetes/kube-apiserver.crt \\
  --tls-private-key-file=/var/lib/kubernetes/kube-apiserver-key.pem \\
  --v=2
```

### Deployment Using kubeadm

When using kubeadm, components such as the kube-apiserver are defined as pods in manifest files. For example, view the kube-apiserver pod manifest:

```yaml theme={null}
cat /etc/kubernetes/manifests/kube-apiserver.yaml
spec:
  containers:
    - command:
      - kube-apiserver
      - --authorization-mode=Node,RBAC
      - --advertise-address=172.17.0.32
      - --allow-privileged=true
      - --client-ca-file=/etc/kubernetes/pki/ca.crt
      - --disable-admission-plugins=PersistentVolumeLabel
      - --enable-admission-plugins=NodeRestriction
      - --enable-bootstrap-token-auth=true
      - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
      - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
      - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
      - --insecure-port=0
      - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
      - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
      - --proxy-client-certfile=/etc/kubernetes/pki/apiserver-kubelet-client.crt
      - --proxy-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
      - --request-timeout=30s
```

## Creating a Certificate Inventory

When performing a certificate health check, it’s essential to create a checklist—perhaps using a spreadsheet—to record details such as:

* Certificate file paths
* Configured names and alternate names
* Associated organizations
* Certificate owners
* Certificate authorities (issuers)
* Expiration dates

Begin by examining configuration files (such as the kube-apiserver manifest located in `/etc/kubernetes/manifests`) to identify the certificate files in use.

For example, the kube-apiserver manifest might reveal the following options:

```yaml theme={null}
spec:
  containers:
    - command:
      - kube-apiserver
      - --authorization-mode=Node,RBAC
      - --advertise-address=172.17.0.32
      - --allow-privileged=true
      - --client-ca-file=/etc/kubernetes/pki/ca.crt
      - --disable-admission-plugins=PersistentVolumeLabel
      - --enable-admission-plugins=NodeRestriction
      - --enable-bootstrap-token-auth=true
      - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
      - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
      - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
      - --etcd-servers=https://127.0.0.1:2379
      - --insecure-port=0
      - --kubelet-client-certificate=/etc/kubernetes/pki/apiserver-kubelet-client.crt
      - --kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-client.key
      - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
      - --proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.crt
      - --proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.key
      - --secure-port=6443
      - --service-account-key-file=/etc/kubernetes/pki/sa.pub
      - --service-cluster-ip-range=10.96.0.0/12
      - --tls-cert-file=/etc/kubernetes/pki/apiserver.crt
      - --tls-private-key-file=/etc/kubernetes/pki/apiserver.key
```

<Callout icon="lightbulb" color="#1CB2FE">
  Make sure to document all certificate details as part of your checklist. This practice simplifies troubleshooting and renewal processes.
</Callout>

## Inspecting Certificate Details

After identifying certificate files, use OpenSSL to decode them and check their details. For example, to review the API server certificate, run:

```bash theme={null}
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout
```

This command displays:

* The subject name and any alternate names
* The validity period (including expiry dates)
* The issuing certificate authority

Repeat this process for all certificates in your Kubernetes cluster. Ensure that:

* Certificate names and alternate names are correctly configured.
* Each certificate is associated with the appropriate organization.
* Certificates are issued by the correct certificate authority (e.g., kubeadm typically uses "Kubernetes" as the CA).
* None of the certificates have expired.

<Callout icon="triangle-alert" color="#FF6B6B">
  An expired or misconfigured certificate can cause critical disruptions in your cluster's operations. Always validate certificate expiry dates and issuer details.
</Callout>

## Troubleshooting with Logs

When certificate issues are suspected, reviewing logs can provide valuable insights.

### For Clusters Using Native OS Services

Check service logs using system commands. For example, inspect etcd logs with:

```bash theme={null}
journalctl -u etcd.service -l
```

Below is an example excerpt from etcd logs:

```plaintext theme={null}
2019-02-13 02:53:28.144631 I | etcdmain: etcd Version: 3.2.18
2019-02-13 02:53:28.144680 I | etcdmain: Git SHA: eddf599c6
2019-02-13 02:53:28.144684 I | etcdmain: Go Version: go1.8.7
2019-02-13 02:53:28.144692 I | etcdmain: Go OS/Arch: linux/amd64
2019-02-13 02:53:28.144696 I | etcdmain: setting maximum number of CPUs to 4, total number of available CPUs is 4
2019-02-13 02:53:28.144734 N | etcdmain: the server is already initialized as member before, starting as etcd member...
2019-02-13 02:53:28.146651 I | etcdserver: name = master
...
WARNING: 2019/02/13 02:53:30 Failed to serve client requests on 127.0.0.1:2379
Failed to dial 127.0.0.1:2379: connection error: desc = "transport: authentication handshake failed: remote error: tls: bad certificate"; please retry.
```

### For Clusters Using kubeadm

Since core components are deployed as pods, retrieve logs using:

* Running `kubectl logs <pod-name>` for pod-level logs.
* If the API server or etcd is down and `kubectl` is unresponsive, list all containers with:

  ```bash theme={null}
  docker ps -a
  ```

  Then inspect container logs:

  ```bash theme={null}
  docker logs <container-id>
  ```

## Additional Resources

For further details on certificate requirements and best practices, please refer to the official [Kubernetes Documentation](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) and explore additional resources available on the Kubernetes website.

That’s it for this lesson. Head over to your practice environment and gain hands-on experience in viewing and verifying certificates in an existing Kubernetes cluster.

<Frame>
  ![The image shows a table detailing Kubernetes certificate configurations, including default CNs, parent CAs, key paths, cert paths, commands, and arguments for various components.](https://kodekloud.com/kk-media/image/upload/v1752869980/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-View-Certificate-Details/frame_210.jpg)
</Frame>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/f2241ff5-cbe9-4e0a-843b-cac131682ec1" />
</CardGroup>
