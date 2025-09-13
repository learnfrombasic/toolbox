`toolbox`

# Introduction

This repository is a sandbox for developers and DevOps engineers to test, learn, and experiment with a wide range of open-source tools. Everything in this repo is designed to be deployed and run easily using Docker, Docker Compose, or Kubernetes.

My goal is to simplify the process of setting up and evaluating different technologies without the headache of complex configurations. Whether you're exploring a new data storage solution like MinIO, integrating a tracing tool like Langfuse, or spinning up a message broker like Kafka, you'll find everything you need to get started right here.


# Usage

Deploy services in `/docker` via cli:

```
docker compose -f ./docker/<filename> up 
```

or using detach mode:

```
start:
docker compose -f ./docker/<filename> up -d

logs:
docker compose -f ./docker/<filename> logs -f

stop:
docker compose -f ./docker/<filename> down
```