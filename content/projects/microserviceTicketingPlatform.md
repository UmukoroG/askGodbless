---
type: project
name: microservice-ticketing-platform
tags: [microservices, kubernetes, event-driven, nats, docker]
github: https://github.com/UmukoroG/Microservice-ticketing
summary: Production-style ticketing system with 5 independently deployable microservices orchestrated on Kubernetes
---

## What it is
A production-style ticketing system composed of 5 independently deployable
microservices — auth, tickets, orders, payments, and expiration —
orchestrated on Kubernetes.

## What I built
- Event-driven communication between services using NATS streaming,
  including idempotent consumers and ordered event processing to keep
  services consistent under failure.
- Containerized every service with Docker.
- Wired up a CI pipeline for automated builds and deploys across all 5
  services.

## Stack
Kubernetes, Docker, NATS, Node.js/TypeScript.