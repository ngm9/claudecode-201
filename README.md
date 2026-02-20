> **Real Engineering Task** — created with [Utkrusht.ai](https://utkrusht.ai)

# ShopFlow — E-Commerce Inventory Management API

## Overview

ShopFlow is an e-commerce platform managing products across multiple suppliers, categories, and warehouses. Your task is to design the database logic and implement FastAPI endpoints for inventory workflows: stock tracking per warehouse, price changes with historical tracking, low-stock detection, and movement logging.

## Tech Stack

- **Python 3.10+**, FastAPI, Uvicorn
- **Supabase** (hosted PostgreSQL) — no local database needed
- **Pydantic** for request/response validation

## Setup

### 1. Clone and install

```bash
git clone https://github.com/ngm9/claudecode-201.git
cd claudecode-201
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment

Copy `.env.example` to `.env` and fill in your Supabase credentials:

```bash
cp .env.example .env
```

We'll share a `.env` file with Supabase credentials at the workshop.

### 3. Run the server

```bash
uvicorn app.main:app --reload --port 8000
```

## Project Structure

```
app/
├── main.py                  # FastAPI app entry point
├── database.py              # Supabase client initialization
├── models/
│   └── database_models.py   # DAO layer (database access functions)
├── routes/
│   └── api.py               # API endpoint handlers
└── schemas/
    └── schemas.py           # Pydantic request/response models
schema.sql                   # Database schema (run in Supabase SQL editor)
data/sample_data.sql         # Sample data for testing
```

## Endpoints

| Endpoint | Method | Status |
|----------|--------|--------|
| `/products` | GET | Implemented (has a bug!) |
| `/inventory/update` | POST | Working |
| `/inventory/low_stock` | GET | TODO |
| `/price/bulk_update` | POST | TODO |
| `/inventory/transfer` | POST | TODO |
| `/inventory/valuation` | GET | TODO |

## Objectives

- Establish relational integrity across products, categories, warehouses, and inventory
- Implement async FastAPI endpoints using the Supabase client
- Include inventory adjustment tracking via the movements table
- Maintain reliable behavior in core workflows

## How to Verify

- `GET /products` — currently returns a 500 (there's a bug to find!)
- `POST /inventory/update` — update stock for a product in a warehouse
- `GET /inventory/low_stock` — should return 501 (not yet implemented)
- Load schema and sample data into Supabase and inspect tables
- Test boundary conditions (negative quantities, unknown categories)

## Helpful Tips

- Explore the FastAPI project structure in `app/` to understand routing and data access
- The Supabase client is initialized in `database.py` — use `get_supabase()` everywhere
- Focus on the core flow: list products, check stock, update inventory
- The DAO pattern in `models/database_models.py` is the reference for new features
