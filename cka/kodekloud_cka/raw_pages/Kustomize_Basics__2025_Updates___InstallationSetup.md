> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# InstallationSetup

> This guide explains how to install and set up Kustomize for customizing Kubernetes resource configurations.

In this guide, you'll learn how to install and set up Kustomize—a powerful tool for customizing Kubernetes resource configurations. Before proceeding, ensure that you have a running Kubernetes cluster and that [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) is installed and configured on your local machine. Kustomize supports Linux, Windows, and macOS.

## Installation Steps

The Kustomize team provides a convenient installation script that automatically detects your operating system and installs the appropriate version. To download and run this script, execute the following command in your terminal:

```bash theme={null}
curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash
```

After the script completes, verify the installation by checking the version of Kustomize with:

```bash theme={null}
kustomize version --short
```

You should see an output resembling the following:

```text theme={null}
{kustomize/v4.4.1  2021-11-11T23:36:27Z }
```

<Callout icon="lightbulb" color="#1CB2FE">
  If you do not see the expected version output, it may indicate an installation issue or that your current terminal session has not updated the necessary environment variables.
</Callout>

## Troubleshooting

If you encounter any issues during installation, try the following steps:

1. Close your current terminal session and reopen it.
2. Rerun the installation script to ensure that all components are set up correctly.

For more detailed troubleshooting and advanced configuration options, refer to the [Kustomize Documentation](https://kubectl.docs.kubernetes.io/).

With Kustomize properly installed, you are now ready to explore its powerful features for managing Kubernetes configurations. Enjoy customizing your Kubernetes deployments!

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/031e84b8-bcbc-4f39-94d6-66d93b05bddc/lesson/14461618-374d-4ca2-983d-5ef86944661d" />
</CardGroup>
