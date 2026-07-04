# DevBox
A hands-on project for learning **Podman** by building a real multi-container application instead of running isolated demo containers.
Instead of focusing on Podman containers; DevBox demonstrates how backend services communicate using containers, pods, custom networks and persistent storage.

## Current Architecture

Browser -> localhost:8080 -> nginx reverse proxy -> Flask backend -> PostgreSQL Database, Redis (future cache support)

## Features
- Rootless Podman containers
- Custom Flask image
- Custom nginx image
- Podman pods
- Custom bridge network
- Persistent PostgreSQL volume
- Flask+PostgreSQL integration
- Reverse proxy using nginx
- Git feature-branch based development

## Running
Build the images:
`./scripts/build.sh`

Start the containers(current manual workflow): PostgreSQL, podman pod, redis, flask backend, nginx

Verify backend:
`curl http://localhost:8080/health`
