# [CKA W4D1-CKA] Solution & Technical Walkthrough

### Tasks & Official Solution
1. Deploy `custom-streamer`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: custom-streamer
  namespace: w4d1-cmd
spec:
  containers:
  - name: streamer
    image: busybox:1.36
    command: ["/bin/sh", "-c"]
    args: ["while true; do echo STREAMING_EVENT; sleep 2; done"]
```
`kubectl apply -f streamer.yaml`

2. Deploy `env-interpolator`:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-interpolator
  namespace: w4d1-cmd
spec:
  containers:
  - name: interpolator
    image: busybox:1.36
    env:
    - name: CLUSTER_ROLE
      value: "processor"
    command: ["/bin/sh", "-c"]
    args: ["echo Initialized as $(CLUSTER_ROLE) && sleep 3600"]
```
`kubectl apply -f interpolator.yaml`
