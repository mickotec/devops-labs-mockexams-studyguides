> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 2025 Updates Validating and Mutating Admission Controllers

> This article explores Kubernetes Admission Controllers, detailing validating and mutating types, their configurations, and how to implement custom external admission webhooks.

This article provides an in-depth look at Kubernetes Admission Controllers, focusing on both validating and mutating types. Learn how these controllers work, inspect typical API requests, and explore how to configure custom external admission webhooks for advanced validations and mutations.

## Validating Admission Controllers

Validating admission controllers verify that an object meets specific criteria before it is persisted in the cluster. For example, the namespace existence or namespace lifecycle admission controller checks if a namespace exists and, if not, rejects the incoming request. Another example is the default storage class admission controller. When you create a PersistentVolumeClaim (PVC) without specifying a storage class, this validating controller intercepts the request and modifies it by adding the default storage class.

Consider the initial PVC creation request:

```yaml theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

After the request passes through authentication, authorization, and the admission controller, the modified PVC appears as follows:

```yaml theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
  storageClassName: default
```

Since the controller modifies the request, such controllers are also considered mutating admission controllers.

## Mutating vs. Validating Admission Controllers

Admission controllers in Kubernetes can be classified into two main types:

* **Mutating Admission Controllers:** Modify (mutate) objects before they are persisted.
* **Validating Admission Controllers:** Validate objects to ensure they meet specific criteria, allowing or denying the request accordingly.

Some controllers perform both mutation and validation. Typically, mutating controllers run first so that subsequent validating controllers can work with the modified object. For instance, if a namespace auto-provisioning mutating admission controller creates a missing namespace before the namespace existence validating controller runs, the request proceeds smoothly. However, if the validating controller executes first, it would reject the request due to the missing namespace.

<Callout icon="lightbulb" color="#1CB2FE">
  If any admission controller (mutating or validating) rejects a request, the entire request is denied and an error is returned to the user.
</Callout>

<Frame>
  ![The image depicts a diagram of Kubernetes admission controllers, showing categories like "Mutating" and "Validating," with examples such as "AlwaysPullImages" and "DefaultStorageClass."](https://kodekloud.com/kk-media/image/upload/v1752869883/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-2025-Updates-Validating-and-Mutating-Admission-Controllers/frame_140.jpg)
</Frame>

All built-in admission controllers are part of the Kubernetes source code. But for custom validations and mutations, Kubernetes supports external admission controllers using webhook mechanisms:

* Mutating Admission Webhook
* Validating Admission Webhook

## Configuring External Admission Webhooks

External admission webhooks can point to servers either inside or outside the Kubernetes cluster. Once the built-in admission controllers finish processing, the API server sends an AdmissionReview object (in JSON format) containing request details such as user information, operation type, and object metadata to the external webhook.

Below is an example AdmissionReview request sent to a webhook server:

```json theme={null}
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "request": {
    "uid": "705ab415-6393-11e7-b7cc-4201a8000002",
    "kind": {"group": "autoscaling", "version": "v1", "kind": "Scale"},
    "resource": {"group": "apps", "version": "v1", "resource": "deployments"},
    "subresource": "scale",
    "requestKind": {"group": "autoscaling", "version": "v1", "kind": "Scale"},
    "requestResource": {"group": "apps", "version": "v1", "resource": "deployments"}
  }
}
```

The webhook server processes the AdmissionReview request and responds with its own AdmissionReview JSON object. If the request is allowed, the response might appear as follows:

```json theme={null}
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "request": {
    "uid": "705ab41f-6393-11e8-b7cc-4201a8000002",
    "kind": {
      "group": "autoscaling",
      "version": "v1",
      "kind": "Scale"
    },
    "resource": {
      "group": "apps",
      "version": "v1",
      "resource": "deployments"
    },
    "subResource": "scale",
    "requestKind": {
      "group": "autoscaling",
      "version": "v1",
      "kind": "Scale"
    },
    "requestResource": {
      "group": "apps",
      "version": "v1",
      "resource": "deployments"
    }
  },
  "response": {
    "uid": "<value_from request.uid>",
    "allowed": true
  }
}
```

If the "allowed" field is set to false, the API server rejects the request.

## Deploying Your Admission Webhook Server

To implement your custom webhook server, you must deploy it and ensure it can support the required mutation and validation APIs by returning correct JSON responses. The following Go code snippet illustrates a basic webhook server setup:

```go theme={null}
package main

import (
    "encoding/json"
    "flag"
    "fmt"
    "io/ioutil"
    "net/http"
    "k8s.io/api/admission/v1beta1"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/klog"
)

// toAdmissionResponse creates an AdmissionResponse with an error message.
func toAdmissionResponse(err error) v1beta1.AdmissionResponse {
    return v1beta1.AdmissionResponse{
        Result: &metav1.Status{
            Message: err.Error(),
        },
    }
}

// admitFunc defines the signature for validators and mutators.
type admitFunc func(v1beta1.AdmissionReview) v1beta1.AdmissionResponse

// serve processes the HTTP request before calling the admitFunc.
func serve(w http.ResponseWriter, r *http.Request, admit admitFunc) {
    var data []byte
    if r.Body == nil {
        return
    }
    data, err := ioutil.ReadAll(r.Body)
    if err != nil {
        return
    }
    // Additional processing logic goes here...
}
```

Below is a pseudocode example of a webhook server implemented in Python. This example demonstrates both validation and mutation logic.

### Python Webhook Server Example

In this Python example, the "/validate" endpoint rejects requests where the object's name matches the user's name, while the "/mutate" endpoint adds a label with the user's name:

```python theme={null}
from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    object_name = request.json["request"]["object"]["metadata"]["name"]
    user_name = request.json["request"]["userInfo"]["name"]
    status = True
    message = ""
    if object_name == user_name:
        message = "You can't create objects with your own name"
        status = False
    return jsonify(
        {
            "response": {
                "allowed": status,
                "uid": request.json["request"]["uid"],
                "status": {"message": message},
            }
        }
    )

@app.route("/mutate", methods=["POST"])
def mutate():
    user_name = request.json["request"]["userInfo"]["name"]
    patch = [{"op": "add", "path": "/metadata/labels/users", "value": user_name}]
    encoded_patch = base64.b64encode(str(patch).encode()).decode()
    return jsonify(
        {
            "response": {
                "allowed": True,
                "uid": request.json["request"]["uid"],
                "patch": encoded_patch,
                "patchType": "JSONPatch",
            }
        }
    )

if __name__ == "__main__":
    app.run(port=443, debug=True)
```

<Callout icon="lightbulb" color="#1CB2FE">
  Even if you may not need to write such code for an exam, understanding the flow and structure of AdmissionReview objects is essential for managing custom admission controllers in Kubernetes.
</Callout>

## Hosting the Webhook Server and Configuring Webhooks

After developing your webhook server, deploy it either as a standalone service or containerize it and run it within your Kubernetes cluster. If running inside the cluster, ensure that the server is accessible via a Kubernetes Service.

To instruct the API server to use your webhook for validations or mutations, create a `ValidatingWebhookConfiguration` or a `MutatingWebhookConfiguration` object. Below is an example configuration for a validating webhook that triggers on pod creation:

```yaml theme={null}
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: "pod-policy.example.com"
webhooks:
- name: "pod-policy.example.com"
  clientConfig:
    service:
      namespace: "webhook-namespace"
      name: "webhook-service"
    caBundle: "Ci0tLS0tQk......tLS0K"
  rules:
  - apiGroups: [""]
    apiVersions: ["v1"]
    operations: ["CREATE"]
    resources: ["pods"]
    scope: "Namespaced"
```

In the configuration above:

* The **clientConfig** block specifies how the API server connects to your webhook service, including the TLS certificate bundle (`caBundle`).
* The **rules** section defines the operations that trigger the webhook—in this case, whenever a pod is created.

Once this configuration is applied, the Kubernetes API server will call your webhook service for each relevant pod creation event, and the request will be allowed or rejected according to the logic implemented in your webhook.

## Conclusion

This guide has provided an overview of Kubernetes admission controllers—both validating and mutating—and demonstrated how to configure external admission webhooks. By applying these concepts, you can enhance the security, flexibility, and management of your Kubernetes clusters.

For further reading, check out these resources:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Terraform Registry](https://registry.terraform.io/)

Experiment with these configurations and webhook implementations in a test environment to gain hands-on experience and further solidify your understanding of Kubernetes Admission Controllers.

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/cd124bdf-9911-4cc1-8177-f2d8b6dfd2a0/lesson/84e17c75-8713-40fc-9ece-148b50942fc9" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/cd124bdf-9911-4cc1-8177-f2d8b6dfd2a0/lesson/1f3b6bb8-1b60-486a-b7da-08c8c33d8508" />
</CardGroup>
