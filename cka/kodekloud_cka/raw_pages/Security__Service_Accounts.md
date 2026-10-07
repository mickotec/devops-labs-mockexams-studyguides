> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Service Accounts

> This guide explains Kubernetes service accounts, their creation, usage, and security enhancements in recent versions.

Welcome to this comprehensive guide on Kubernetes service accounts. In this lesson, we focus on how service accounts function—primarily from an application developer's perspective. While advanced security topics such as authentication, authorization, and role-based access control (RBAC) are covered extensively in the [Kubernetes Administrators Course](https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator), this guide is dedicated solely to working with service accounts.

There are two main types of accounts in Kubernetes:

* **User Accounts:** Designed for human users like administrators or developers.
* **Service Accounts:** Intended for machine-to-machine interactions or application-specific tasks. For instance, monitoring tools like Prometheus use a service account to query the Kubernetes API for performance metrics, while Jenkins uses one for deploying applications.

<Frame>
  ![The image shows a comparison between "User" and "Service" roles, with icons for Admin, Developer, and robots.](https://kodekloud.com/kk-media/image/upload/v1752869950/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_60.jpg)
</Frame>

## Example: A Kubernetes Dashboard Application

Consider an example: "my Kubernetes dashboard," a basic dashboard application built with Python. This application retrieves a list of Pods from a Kubernetes cluster by sending API requests and subsequently displays the results on a web page. To authenticate its API requests, the application uses a dedicated service account.

<Frame>
  ![The image shows a Kubernetes dashboard interface connected to a Kubernetes cluster with three nodes via the kube-api.](https://kodekloud.com/kk-media/image/upload/v1752869951/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_110.jpg)
</Frame>

### Creating a Service Account

To create a service account named `dashboard-sa`, run:

```bash theme={null}
kubectl create serviceaccount dashboard-sa
```

To view all service accounts, use:

```bash theme={null}
kubectl get serviceaccount
```

The output will appear similar to:

```bash theme={null}
NAME           SECRETS   AGE
default        1         218d
dashboard-sa   1         4d
```

Upon creation, Kubernetes automatically generates a service account token stored as a Secret and links it to the account. To inspect the details of your service account and its token, execute:

```bash theme={null}
kubectl describe serviceaccount dashboard-sa
```

Expected output:

```bash theme={null}
Name:                dashboard-sa
Namespace:           default
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   dashboard-sa-token-kbbdm
Tokens:              dashboard-sa-token-kbbdm
Events:              <none>
```

To examine the token itself, view the corresponding Secret:

```bash theme={null}
kubectl describe secret dashboard-sa-token-kbbdm
```

Sample output:

```bash theme={null}
Name:                dashboard-sa-token-kbbdm
Namespace:           default
Labels:              <none>
Type:                kubernetes.io/service-account-token
Data
  token: eyJhbGciOiJSUzI1NiIsImtpZCI6Ij...  (truncated for privacy)
```

This token serves as the authentication bearer token for accessing the Kubernetes API. For example, using curl:

```bash theme={null}
curl https://192.168.56.70:6443/api -k \
--header "Authorization: Bearer eyJhbgG…"
```

<Callout icon="lightbulb" color="#1CB2FE">
  In your custom dashboard application, you would typically place the token into the appropriate configuration field to enable API authentication.
</Callout>

## Automatic Mounting of Service Account Tokens

When deploying third-party applications (such as a custom dashboard or Prometheus) on a Kubernetes cluster, you can have Kubernetes automatically mount the service account token as a volume into the Pod. This token is typically available at the path: `/var/run/secrets/kubernetes.io/serviceaccount`.

<Frame>
  ![The image shows a Kubernetes dashboard interface with icons representing security, a database, and user credentials, indicating a secure connection to a Kubernetes pod.](https://kodekloud.com/kk-media/image/upload/v1752869953/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_270.jpg)
</Frame>

Every namespace includes a default service account that is automatically injected into Pods. For example, consider the following simple Pod manifest using a custom dashboard image:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  containers:
  - name: my-kubernetes-dashboard
    image: my-kubernetes-dashboard
```

After creating this Pod, running:

```bash theme={null}
kubectl describe pod my-kubernetes-dashboard
```

will reveal a volume mounted from a Secret (usually named something like `default-token-xxxx`). You might see an excerpt similar to:

```bash theme={null}
Name:           my-kubernetes-dashboard
Namespace:      default
Status:         Running
IP:             10.244.0.15
Containers:
  nginx:
    Image:        my-kubernetes-dashboard
    Mounts:       /var/run/secrets/kubernetes.io/serviceaccount from default-token-j4hkv (ro)
Volumes:
  default-token-j4hkv:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-j4hkv
    Optional:    false
```

Inside the Pod, listing the contents of the service account directory shows files such as the `token` file containing the bearer token:

```bash theme={null}
kubectl exec -it my-kubernetes-dashboard -- ls /var/run/secrets/kubernetes.io/serviceaccount
kubectl exec -it my-kubernetes-dashboard -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

### Using a Different Service Account

By default, Pods use the `default` service account. To assign a different service account—like the previously created `dashboard-sa`—update your Pod definition to include the `serviceAccountName` field:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  serviceAccountName: dashboard-sa
  containers:
    - name: my-kubernetes-dashboard
      image: my-kubernetes-dashboard
```

<Callout icon="lightbulb" color="#1CB2FE">
  Remember that you cannot modify the service account of an existing Pod. To use a new service account, delete and recreate the Pod. Deployments will automatically roll out new Pods when changes are made to the Pod template.
</Callout>

After deploying the updated manifest, running:

```bash theme={null}
kubectl describe pod my-kubernetes-dashboard
```

will show that the new service account is now in effect, with volume mounting information reflecting the token for `dashboard-sa` (e.g., `dashboard-sa-token-kbbdm`).

If you wish to disable the automatic mounting of the service account token, set `automountServiceAccountToken` to `false` in the Pod specification:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  automountServiceAccountToken: false
  containers:
  - name: my-kubernetes-dashboard
    image: my-kubernetes-dashboard
```

## Changes in Kubernetes Versions 1.22 and 1.24

Prior to Kubernetes v1.22, service account tokens were automatically mounted from Secrets without an expiration date. Starting with v1.22, the TokenRequest API (KEP-1205) was introduced to generate tokens that are audience-bound, time-bound, and object-bound—enhancing security significantly.

Below is an example Pod definition using a projected volume sourced from the TokenRequest API:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: default
spec:
  containers:
    - image: nginx
      name: nginx
      volumeMounts:
        - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
          name: kube-api-access-6mtg8
          readOnly: true
  volumes:
    - name: kube-api-access-6mtg8
      projected:
        defaultMode: 420
        sources:
          - serviceAccountToken:
              expirationSeconds: 3607
            path: token
          - configMap:
              name: kube-root-ca.crt
              items:
                - key: ca.crt
                  path: ca.crt
          - downwardAPI:
              items:
                - fieldRef:
                    apiVersion: v1
                    fieldPath: metadata.namespace
```

Starting with Kubernetes v1.24, Kubernetes no longer automatically creates non-expiring service account tokens stored as Secrets. Instead, after creating a new service account, you must generate a token explicitly with:

```bash theme={null}
kubectl create token dashboard-sa
```

This command produces a token with an expiry (by default, one hour from creation). You can verify and decode this token using tools like jq or [jwt.io](https://jwt.io):

```bash theme={null}
jq -R 'split(".") | select(length > 0) | .[0] | @base64 | fromjson' <<< <TOKEN>
```

If necessary (though not recommended), you can still create a non-expiring token by manually creating a Secret. Ensure the service account exists first:

```yaml theme={null}
apiVersion: v1
kind: Secret
metadata:
  name: mysecretname
  annotations:
    kubernetes.io/service-account.name: dashboard-sa
type: kubernetes.io/service-account-token
```

<Callout icon="triangle-alert" color="#FF6B6B">
  It is highly recommended to use the TokenRequest API to generate tokens, as API-generated tokens provide additional security features such as expiry, audience restrictions, and improved manageability.
</Callout>

<Frame>
  ![The image shows a JWT (JSON Web Token) decoding interface with encoded data on the left and decoded JSON data on the right.](https://kodekloud.com/kk-media/image/upload/v1752869955/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_560.jpg)
</Frame>

<Frame>
  ![The image describes Kubernetes' JWT security issues, including lack of audience binding, broad attack surfaces, absence of time bounds, and scalability challenges requiring secrets per service account.](https://kodekloud.com/kk-media/image/upload/v1752869956/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_580.jpg)
</Frame>

<Frame>
  ![The image is a slide about Kubernetes v1.22, featuring KEP 1205 for Bound Service Account Tokens, highlighting the TokenRequest API with audience and time-bound features.](https://kodekloud.com/kk-media/image/upload/v1752869957/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_620.jpg)
</Frame>

<Frame>
  ![The image explains Kubernetes service account token secrets and recommends the TokenRequest API for secure token management since version 1.22.](https://kodekloud.com/kk-media/image/upload/v1752869958/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_830.jpg)
</Frame>

## Summary

* **Service Accounts vs. User Accounts:** Service accounts are meant for applications (or machines), whereas user accounts are for human users.
* **Token Generation:** Creating a service account automatically generates a token stored in a Secret, which is used for API authentication.
* **Automatic Token Mounting:** Pods can automatically mount the service account token at `/var/run/secrets/kubernetes.io/serviceaccount`, though this behavior can be modified.
* **Enhanced Security:** Since Kubernetes v1.22, tokens are generated using the TokenRequest API, making them audience-bound, time-bound, and more secure.
* **Kubernetes v1.24 Changes:** With v1.24, Kubernetes no longer provisions non-expiring tokens automatically via Secrets; use the `kubectl create token` command to generate tokens as needed.

For additional insights, refer to the Kubernetes enhancement proposals and the official documentation on service accounts and tokens.

<Frame>
  ![The image lists references related to Kubernetes service account tokens, including links to GitHub and Kubernetes documentation.](https://kodekloud.com/kk-media/image/upload/v1752869959/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Service-Accounts/frame_870.jpg)
</Frame>

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/01b112f9-20dc-442a-8521-008064deb80d" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/06c49ebe-214f-40cb-9195-ceb816fcf2b5" />
</CardGroup>
