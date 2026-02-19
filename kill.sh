#!/bin/bash
set -e

echo "[1/7] Stopping and removing containers..."
docker-compose -f /root/task/docker-compose.yml down --volumes --remove-orphans || true

echo "[2/7] Removing docker images (shopflow_api, postgres:15-alpine)..."
docker rmi -f $(docker images -q | grep -E 'shopflow_api|postgres:15-alpine' || true) || true

echo "[3/7] Pruning all unused system resources..."
docker system prune -a --volumes -f

echo "[4/7] Deleting project folder /root/task..."
rm -rf /root/task

echo "[5/7] Removing Python cache and miscellaneous files..."
rm -rf /root/task/__pycache__/ /root/task/app/__pycache__/ /root/task/app/routes/__pycache__/ /root/task/app/models/__pycache__/ /root/task/app/schemas/__pycache__/ /root/task/*.pyc /root/task/*.pyo /root/task/*.pytest_cache /root/task/*.mypy_cache /root/task/data/pgdata/ || true

echo "[6/7] Verifying cleanup..."
ls /root/task 2>/dev/null && echo "Directory still exists!" || echo "Directory removed as expected."

echo "[7/7] Cleanup completed successfully! Droplet is now clean."
