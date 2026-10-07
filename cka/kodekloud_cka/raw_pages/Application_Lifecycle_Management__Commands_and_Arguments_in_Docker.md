> ## Documentation Index
> Fetch the complete documentation index at: https://notes.kodekloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Commands and Arguments in Docker

> This article explains Docker commands, arguments, and ENTRYPOINT, focusing on container processes and their relation to Kubernetes pod definitions.

Hello and welcome to this comprehensive lesson on Docker commands, arguments, and entry points. My name is Mumshad Mannambeth, and in this session, we will dive into how containers run processes and how these concepts later translate into pod definitions in Kubernetes. Although these topics are often overlooked in certification curricula, understanding them is essential for mastering containerization.

## Understanding Container Commands

When you run a Docker container using the Ubuntu image, as shown below:

```bash theme={null}
docker run ubuntu
```

Docker launches a container based on the Ubuntu image, which starts and immediately exits since it runs a default process that completes quickly. If you inspect the currently running containers:

```bash theme={null}
docker ps
```

you will notice that the container is absent because it has already exited. However, viewing all containers—including those that have stopped—with:

```bash theme={null}
docker ps -a
```

reveals that the container is in an "exited" state:

```plaintext theme={null}
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS
45aacca36850        ubuntu              "/bin/bash"         43 seconds ago      Exited (0) 41 seconds ago
```

This behavior is different from traditional virtual machines. Containers are optimized to run a single task or process, such as hosting a web server, application server, database, or performing a specific computation. Once the task completes, the container stops because its lifecycle is tied directly to the process running inside it.

## Default Commands in Docker Images

Each Docker image contains instructions that define the process to run when a container starts. Many popular images, such as [nginx](https://www.nginx.com/) or [MySQL](https://www.mysql.com/), include a CMD instruction in their Dockerfile that sets the default command. For instance, the nginx image typically has the command `nginx`, and the MySQL image uses `mysqld`.

Consider this Dockerfile snippet for installing and configuring nginx:

```dockerfile theme={null}
# Install Nginx.
RUN \
    add-apt-repository -y ppa:nginx/stable && \
    apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/* && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    chown -R www-data:www-data /var/lib/nginx

# Define mountable directories.
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf"]

# Define working directory.
WORKDIR /etc/nginx

# Define default command.
CMD ["nginx"]
```

Now, let's examine the Ubuntu image's Dockerfile. Notice that in this example, the default command is set to Bash:

```dockerfile theme={null}
# Pull base image.
FROM ubuntu:14.04

# Install necessary packages.
RUN \
    sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential software-properties-common byobu curl git htop man unzip vim wget && \
    rm -rf /var/lib/apt/lists/*

# Add configuration files.
ADD root/.bashrc /root/.bashrc
ADD root/.gitconfig /root/.gitconfig
ADD root/.scripts /root/.scripts

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
```

<Callout icon="lightbulb" color="#1CB2FE">
  Remember: Bash is a shell, not a persistent server process. When the Ubuntu container is launched without an attached terminal, the shell exits immediately.
</Callout>

## Overriding the Default Command

To override the default command for a container, you can append a command to the end of the `docker run` command. For example, this command instructs the container to run `sleep 5`:

```bash theme={null}
docker run ubuntu sleep 5
```

In this scenario, the container executes `sleep 5`, waits for five seconds, and then exits.

If you want to permanently change the behavior of the image so that it always runs `sleep 5`, you must create a new image based on Ubuntu and specify the new default command in its Dockerfile. You can specify the command in either of two formats:

1. Shell form:
   ```dockerfile theme={null}
   FROM ubuntu
   CMD sleep 5
   ```
2. JSON array format:
   ```dockerfile theme={null}
   FROM ubuntu
   CMD ["sleep", "5"]
   ```

Build the new image with:

```bash theme={null}
docker build -t ubuntu-sleeper .
```

Then run the container using:

```bash theme={null}
docker run ubuntu-sleeper
```

By default, this container will sleep for five seconds.

## Configuring ENTRYPOINT for Runtime Arguments

Sometimes, you may want to specify only runtime arguments without changing the default command. In such cases, the ENTRYPOINT instruction is useful. This instruction sets the executable to run when the container starts, and any command-line arguments provided at runtime are appended to it.

Consider the following Dockerfile:

```dockerfile theme={null}
FROM ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```

After building and running this image:

```bash theme={null}
docker build -t ubuntu-sleeper .
docker run ubuntu-sleeper
```

the container executes `sleep 5` by default. You can override the sleep duration at runtime by specifying a new parameter:

```bash theme={null}
docker run ubuntu-sleeper 10
```

This command runs `sleep 10`.

<Callout icon="lightbulb" color="#1CB2FE">
  * With CMD alone, runtime arguments replace the default command.
  * With ENTRYPOINT, runtime arguments are appended to the specified executable, allowing you to override just the parameters.
</Callout>

## Overriding ENTRYPOINT at Runtime

At times, you might want to completely override the ENTRYPOINT. For example, if you wish to use a different command (like switching from `sleep` to `sleep2.0`), you can do so using the `--entrypoint` flag in the `docker run` command.

Given the Dockerfile:

```dockerfile theme={null}
FROM ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```

Build the image:

```bash theme={null}
docker build -t ubuntu-sleeper .
```

Running the container without modifications:

```bash theme={null}
docker run ubuntu-sleeper
```

will produce an error because `sleep` expects an operand:

```bash theme={null}
docker run ubuntu-sleeper
# Output:
# sleep: missing operand
# Try 'sleep --help' for more information.
```

However, running with a new parameter:

```bash theme={null}
docker run ubuntu-sleeper 10
```

executes `sleep 10`.

To override the ENTRYPOINT with a different executable, run:

```bash theme={null}
docker run --entrypoint sleep2.0 ubuntu-sleeper 10
```

This command starts the container with `sleep2.0 10` (provided that `sleep2.0` is a valid command).

<Frame>
  ![The image is a plain white background with no discernible objects or features.](https://kodekloud.com/kk-media/image/upload/v1752869660/notes-assets/images/CKA-Certification-Course-Certified-Kubernetes-Administrator-Commands-and-Arguments-in-Docker/frame_190.jpg)
</Frame>

## Conclusion

This lesson explained the inner workings of Docker commands, arguments, and how the ENTRYPOINT instruction allows dynamic parameter passing at runtime. These concepts not only help in managing Docker containers efficiently but also lay the groundwork for understanding how they translate into pod definitions in Kubernetes in subsequent lessons.

Happy Dockering!

For further reading, check out the following resources:

* [Docker Documentation](https://docs.docker.com/)
* [Kubernetes Basics](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
* [Nginx Official Website](https://www.nginx.com/)
* [MySQL Official Website](https://www.mysql.com/)

<CardGroup>
  <Card title="Watch Video" icon="video" cta="Learn more" href="https://learn.kodekloud.com/user/courses/cka-certification-course-certified-kubernetes-administrator/module/2ddcf79b-abb0-4aeb-ad0c-3d54c7b4fc64/lesson/c62a2a06-dffd-4669-b5eb-b98b503e0c0a" />
</CardGroup>
