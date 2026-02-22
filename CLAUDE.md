# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What Is This

ShopFlow — an e-commerce inventory management API (FastAPI + Supabase). Workshop project for implementing inventory workflows: stock tracking per warehouse, price history, low-stock alerts, and inventory transfers.

## Commands

```bash
# Setup
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then fill in SUPABASE_URL and SUPABASE_KEY

# Run server
uvicorn app.main:app --reload --port 8000

# Database setup (run in Supabase SQL Editor)
# 1. schema.sql — creates tables
# 2. data/sample_data.sql — loads test data
```

No tests exist yet. No linter configured.

## Architecture

```
Request → routes/api.py → models/database_models.py (DAO) → Supabase client
                        → schemas/schemas.py (Pydantic validation)
```

- **`app/database.py`** — Singleton Supabase client via `get_supabase()`. All DB access goes through this.
- **`app/models/database_models.py`** — DAO layer. `update_inventory_quantity()` is the reference pattern: fetch current state, validate, update, log movement. New features should follow this pattern.
- **`app/routes/api.py`** — All endpoint handlers. Some inline DB logic (e.g., `list_products`) that should be refactored into the DAO.
- **`app/schemas/schemas.py`** — Pydantic models for all request/response types. All endpoint schemas are already defined here, including for unimplemented endpoints.

## Database Schema

Seven tables: `categories` (self-referencing hierarchy), `suppliers`, `warehouses`, `products` (FK to category + supplier), `inventory` (unique per product+warehouse, has `reorder_level`), `inventory_movements` (audit log), `price_history` (price change audit).

## Current State

| Endpoint | Status | Notes |
|----------|--------|-------|
| `GET /products` | **Buggy** | References `product_name` column but DB column is `name` |
| `POST /inventory/update` | Working | Uses DAO pattern correctly |
| `GET /inventory/low_stock` | TODO | Query where `quantity < reorder_level` |
| `POST /price/bulk_update` | TODO | Update prices + write to `price_history` |
| `POST /inventory/transfer` | TODO | Atomic move between warehouses |
| `GET /inventory/valuation` | TODO | Sum `quantity * base_price` per warehouse |

## Key Patterns

- DAO functions take the Supabase `Client` as first argument and return `{"success": bool, "message": str}` dicts
- Inventory changes must always log to `inventory_movements`
- Price changes must always log to `price_history`
- The Supabase client uses PostgREST query builder syntax: `.table().select().eq().execute()`
