#!/bin/bash
set -e

echo "[1/6] Starting Docker containers..."
docker-compose -f /root/task/docker-compose.yml up -d

echo "[2/6] Waiting for PostgreSQL to be ready..."
MAX_RETRIES=30
for retry in $(seq 1 $MAX_RETRIES); do
  docker exec shopflow_pg pg_isready -U shopuser -d shopflow && break
  sleep 2
done
if [ $retry -eq $MAX_RETRIES ]; then
  echo "Postgres did not become ready in time."; exit 1
fi

echo "[3/6] Creating database roles and users (if needed)..."
docker exec -u postgres shopflow_pg psql -c "CREATE USER shopuser WITH PASSWORD 'shoppass';" 2>/dev/null || true
docker exec -u postgres shopflow_pg psql -c "CREATE DATABASE shopflow OWNER shopuser;" 2>/dev/null || true

echo "[4/6] Running schema.sql..."
docker exec -i shopflow_pg psql -U shopuser -d shopflow < /root/task/schema.sql || true

echo "[5/6] Running sample_data.sql..."
docker exec -i shopflow_pg psql -U shopuser -d shopflow < /root/task/data/sample_data.sql || true

echo "[6/6] Validating FastAPI application..."
for retry in $(seq 1 15); do
    curl -fsS http://localhost:8000/docs && break
    sleep 2
done

echo "[done] Infrastructure and API are now live."
