> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Security Contexts

> This lesson explains how to secure containers in Kubernetes by configuring security settings at the pod and container levels.

Hello, and welcome to this lesson on Security Contexts in Kubernetes. My name is Mumshad Mannambeth, and in this guide, we'll explain how you can secure your containers by configuring security settings at both the pod and container levels.

When you run a Docker container, you have the flexibility to define various security parameters. For example, you can set a specific user ID or modify Linux capabilities. Consider the following Docker commands:

```bash theme={null}
docker run --user=1001 ubuntu sleep 3600
docker run --cap-add MAC_ADMIN ubuntu
```

These configurations help manage the security of Docker containers, and similar settings are available in Kubernetes.

In Kubernetes, containers are always encapsulated in pods. You can define security settings either at the pod level, which affects all containers in the pod, or at the container level where the settings apply specifically to one container. Note that if the same security configuration is set at both the pod and container levels, the container-specific settings take precedence over the pod-level configurations.

Below is an example of a pod definition that configures the security context at the container level, using an Ubuntu image that runs the `sleep` command:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
spec:
  containers:
    - name: ubuntu
      image: ubuntu
      command: ["sleep", "3600"]
      securityContext:
        runAsUser: 1000
        capabilities:
          add: ["MAC_ADMIN"]
```

This configuration instructs Kubernetes to run the container as user ID 1000 and adds the `MAC_ADMIN` capability. If your goal is to enforce these security settings across all containers within a single pod, you can define the security context at the pod level instead.

<Callout icon="lightbulb" color="#1CB2FE">
  For more hands-on practice with viewing, configuring, and troubleshooting security contexts in Kubernetes, check out the available lab resources.
</Callout>

By leveraging security contexts, you enhance the security posture of your containerized applications in Kubernetes. For additional guidance, you may find the following resources useful:

* [Kubernetes Documentation](https://kubernetes.io/docs/)
* [Kubernetes Concepts: Security Contexts](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)

Thank you for following along, and happy securing!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/64d6108a-af51-49d4-9019-c5641a145195" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/77826599-d456-4cb5-8cbc-b713cc077b45/lesson/dc4ab297-ee13-4ee9-ba36-c70608f4b3ed" />
</CardGroup>
