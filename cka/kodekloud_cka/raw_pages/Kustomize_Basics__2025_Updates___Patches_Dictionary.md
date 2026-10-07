> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Patches Dictionary

> Learn to update, add, and remove keys in Kubernetes Deployment configurations using JSON 6902 patches and strategic merge patches with practical examples.

In this article, you'll learn how to update, add, and remove keys in a Kubernetes Deployment configuration using both JSON 6902 patches and strategic merge patches. Each example starts with a Deployment that contains a label with the key "component" set to "api". The goal is to modify or update these labels as needed in each scenario.

***

## Updating a Key in a Dictionary

### Using a JSON 6902 Patch

Consider the following Deployment configuration:

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: api
  template:
    metadata:
      labels:
        component: api
    spec:
      containers:
        - name: nginx
          image: nginx
```

To update the label from `"component: api"` to `"component: web"` using a JSON 6902 patch, include this patch in your `kustomization.yaml`:

```yaml theme={null}
kustomization:
  patches:
    - target:
        kind: Deployment
        name: api-deployment
      patch: |-
        - op: replace
          path: /spec/template/metadata/labels/component
          value: web
```

The patch navigates to the "component" key within the labels dictionary using the path `/spec/template/metadata/labels/component` and replaces its value with "web".

<Callout icon="lightbulb" color="#1CB2FE">
  The JSON 6902 patch method provides precise control when updating complex configurations. Choose the patch type that best fits your needs.
</Callout>

### Using a Strategic Merge Patch

Alternatively, you can update the label using a strategic merge patch stored in a separate file, for example, `label-patch.yaml`. Your main Deployment configuration remains unchanged, and your `kustomization.yaml` is updated as follows:

```yaml theme={null}
kustomization:
  patches:
    - label-patch.yaml
```

Here is an example of the contents for `label-patch.yaml`:

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    metadata:
      labels:
        component: web
```

Kustomize will merge this patch with the original Deployment configuration, resulting in an updated "component" label.

***

## Adding a New Key to a Dictionary

### Using a JSON 6902 Patch

Suppose you want to add a new label `"org"` with the value `"KodeKloud"` while keeping the original `"component: api"` label. Start with the following Deployment:

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: api
  template:
    metadata:
      labels:
        component: api
    spec:
      containers:
        - name: nginx
          image: nginx
```

Then, add the following JSON 6902 patch in your `kustomization.yaml`:

```yaml theme={null}
kustomization:
  patches:
    - target:
        kind: Deployment
        name: api-deployment
      patch: |-
        - op: add
          path: /spec/template/metadata/labels/org
          value: KodeKloud
```

This patch uses the `add` operation to insert the new key `"org"` with the specified value into the labels dictionary.

### Using a Strategic Merge Patch

For a strategic merge patch, create a separate file (e.g., `label-patch.yaml`) with the following content:

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    metadata:
      labels:
        org: KodeKloud
```

Then, reference the patch file in your `kustomization.yaml`:

```yaml theme={null}
kustomization:
  patches:
    - label-patch.yaml
```

Kustomize automatically merges the patch with the existing configuration while preserving both labels: `"component: api"` and `"org: KodeKloud"`.

<Callout icon="lightbulb" color="#1CB2FE">
  When adding new keys, always verify that the target dictionary exists to avoid runtime errors.
</Callout>

***

## Removing a Key from a Dictionary

### Using a JSON 6902 Patch

Assume you have a Deployment configuration that includes two labels:

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: api
  template:
    metadata:
      labels:
        org: KodeKloud
        component: api
    spec:
      containers:
        - name: nginx
          image: nginx
```

To remove the `"org"` label using a JSON 6902 patch, modify your `kustomization.yaml` as follows:

```yaml theme={null}
kustomization:
  patches:
    - target:
        kind: Deployment
        name: api-deployment
      patch: |-
        - op: remove
          path: /spec/template/metadata/labels/org
```

This patch navigates to the "org" key and removes it, leaving only the "component" label in place.

### Using a Strategic Merge Patch

To remove the `"org"` label via a strategic merge patch, create a patch file (e.g., `label-patch.yaml`) with the following content:

```yaml theme={null}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    metadata:
      labels:
        org: null
```

Reference this patch file in your `kustomization.yaml`:

```yaml theme={null}
kustomization:
  patches:
    - label-patch.yaml
```

Kustomize interprets the `null` value as an instruction to remove the `"org"` label from the original configuration.

<Callout icon="triangle-alert" color="#FF6B6B">
  Ensure that you specify the correct path for removal operations to avoid inadvertently deleting other keys in the configuration.
</Callout>

***

With these examples, you now understand how to update, add, and remove keys in a Kubernetes Deployment configuration using both JSON 6902 patches and strategic merge patches. For more detailed information on Kubernetes configurations and patch strategies, visit the [Kubernetes Documentation](https://kubernetes.io/docs/).

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/031e84b8-bcbc-4f39-94d6-66d93b05bddc/lesson/045b04b8-d4bc-42a1-8c50-dfb934e67cce" />
</CardGroup>
