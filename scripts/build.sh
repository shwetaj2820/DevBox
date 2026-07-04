#!/bin/bash
set -e
podman build -t localhost/flask-app backend
podman build -t localhost/devbox-nginx nginx

echo "done"