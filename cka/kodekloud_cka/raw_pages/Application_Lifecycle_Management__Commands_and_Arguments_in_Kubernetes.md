> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Commands and Arguments in Kubernetes

> This lesson covers configuring commands and arguments in Kubernetes pods to adjust container behaviors by overriding default settings from the Dockerfile.

Welcome to this lesson on configuring commands and arguments in Kubernetes pods. In this session, we'll learn how to adjust container behaviors by overriding default settings defined in the Dockerfile via the pod definition.

Previously, we built a simple Docker image—named "ubuntu-sleeper"—that executes a sleep command for a specified number of seconds. By default, running a container with this image makes it sleep for five seconds. However, you can easily change this behavior by passing a command-line argument.

## Overriding Default Behavior with Arguments

Suppose we want to create a pod using the "ubuntu-sleeper" image. We begin with a basic pod definition where the pod's name and image are specified. When the pod is created, it starts a container that runs the default sleep command (sleeping for five seconds) and then exits. To modify the sleep duration to 10 seconds, simply append an additional argument in the pod specification. Any argument provided in the Docker run command correlates with the `args` property in the pod definition file (formatted as an array).

<Callout icon="lightbulb" color="#1CB2FE">
  When you append an argument to the Docker run command, it overrides the default parameters defined by the CMD instruction in the Dockerfile.
</Callout>

Consider the following examples:

Docker commands:

```bash theme={null}
docker run --name ubuntu-sleeper ubuntu-sleeper
docker run --name ubuntu-sleeper ubuntu-sleeper 10
```

Pod definition YAML:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper-pod
spec:
  containers:
  - name: ubuntu-sleeper
    image: ubuntu-sleeper
    args: ["10"]
```

## Dockerfile Instructions and Their Mappings

The Dockerfile for the "ubuntu-sleeper" image is defined with both an ENTRYPOINT and a CMD:

```dockerfile theme={null}
FROM Ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```

* The **ENTRYPOINT** instruction specifies the command to run when the container starts.
* The **CMD** instruction provides default parameters for that command.

By specifying the `args` field in the pod definition file, the CMD instruction is overridden, which effectively changes the sleep duration from 5 to 10 seconds.

## Overriding the ENTRYPOINT

Now, consider a scenario where you want to override the ENTRYPOINT itself (for example, switching from "sleep" to an alternative command like "sleep2.0"). In Docker, you would use the `--entrypoint` option in the `docker run` command. In Kubernetes, this is achieved by providing the `command` field in the pod definition. Here, the `command` field corresponds to the Dockerfile’s ENTRYPOINT, while the `args` field continues to override the CMD instruction.

Docker command example with overridden ENTRYPOINT:

```bash theme={null}
docker run --name ubuntu-sleeper \
  --entrypoint sleep2.0 \
  ubuntu-sleeper 10
```

Pod definition YAML with overridden ENTRYPOINT:

```yaml theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper-pod
spec:
  containers:
    - name: ubuntu-sleeper
      image: ubuntu-sleeper
      command: ["sleep2.0"]
      args: ["10"]
```

## Deployment of the Pod

Once your pod definition is ready, deploy the pod using the following command:

```bash theme={null}
kubectl create -f pod-definition.yml
```

## Key Fields Summary

Below is a table summarizing the Kubernetes pod definition fields that map to Dockerfile instructions:

| Pod Definition Field | Dockerfile Instruction | Functionality Description                                                                            |
| -------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------- |
| command              | ENTRYPOINT             | Specifies the command to run when the container starts (completely replacing Dockerfile ENTRYPOINT). |
| args                 | CMD                    | Provides default parameters passed to the command (overriding the Dockerfile CMD).                   |

<Callout icon="lightbulb" color="#1CB2FE">
  Remember that specifying the `command` in a pod definition replaces the Dockerfile's ENTRYPOINT entirely, while the `args` field only overrides the default parameters defined by CMD.
</Callout>

This concludes the lesson on managing commands and arguments within your Kubernetes pods. Next, proceed to the coding exercises section to practice these concepts and refine your troubleshooting skills with real-world scenarios.

Happy coding!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/2ddcf79b-abb0-4aeb-ad0c-3d54c7b4fc64/lesson/ade38026-5294-40ba-bf2e-8cb09f793b83" />

  <Card title="Practice Lab" icon="installation" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/2ddcf79b-abb0-4aeb-ad0c-3d54c7b4fc64/lesson/5d42a689-ba40-4aaa-9407-6677a622b2f4" />
</CardGroup>
