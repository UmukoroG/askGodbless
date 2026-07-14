---
type: project
name: websocket-load-balancer
tags: [websockets, load-balancing, nodejs, react, distributed-systems]
github: https://github.com/UmukoroG/LoadBalancer
summary: Node.js WebSocket load balancer with round-robin routing, health checks, and a live React observability UI
---

## What it is
A WebSocket load balancer written in Node.js that distributes long-lived
connections across a pool of backend servers, with a React UI for
real-time observability into active servers and message flow.

## What I built
- Round-robin routing of WebSocket connections across a backend server
  pool.
- Periodic health checks that automatically remove failing servers from
  rotation.
- Persistence of all routed traffic to a central database for inspection
  and replay.
- Handled CORS, connection lifecycle, and graceful failover end-to-end.
- Built a React UI exposing a real-time view of active servers and message
  flow through them.

## Stack
Node.js, React, WebSockets.