from fastapi import APIRouter, HTTPException, BackgroundTasks

from app.database import get_supabase
from app.models.database_models import update_inventory_quantity
from app.schemas.schemas import (
    ProductListResponse,
    InventoryUpdateRequest,
    InventoryUpdateResponse,
    LowStockAlertResponse,
    BulkPriceUpdateRequest,
    BulkPriceUpdateResponse,
    WarehouseTransferRequest,
    WarehouseTransferResponse,
    InventoryValuationResponse,
)

router = APIRouter()


@router.get("/products", response_model=ProductListResponse)
async def list_products(category_id: int = None, skip: int = 0, limit: int = 20):
    supabase = get_supabase()

    query = supabase.table("products").select(
        "id, product_name, description, base_price, "
        "categories(id, name, parent_id), "
        "suppliers(id, name, rating), "
        "inventory(warehouse_id, quantity)"
    )

    if category_id:
        query = query.eq("category_id", category_id)

    result = query.range(skip, skip + limit - 1).execute()

    # Inline response construction (no DAO — messy on purpose)
    products = []
    for row in result.data:
        products.append({
            "id": row["id"],
            "name": row["product_name"],
            "description": row.get("description"),
            "base_price": float(row["base_price"]),
            "category": row.get("categories"),
            "supplier": row.get("suppliers"),
            "inventory": row.get("inventory", []),
        })

    count_result = supabase.table("products").select("id", count="exact").execute()

    return {"products": products, "total": count_result.count or 0}


@router.post("/inventory/update", response_model=InventoryUpdateResponse)
async def update_inventory(update: InventoryUpdateRequest, background_tasks: BackgroundTasks):
    supabase = get_supabase()
    result = update_inventory_quantity(
        supabase,
        product_id=update.product_id,
        warehouse_id=update.warehouse_id,
        quantity_delta=update.quantity_delta,
        movement_type=update.movement_type,
        reference=update.reference,
        notes=update.notes,
    )
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result


@router.get("/inventory/low_stock", response_model=LowStockAlertResponse)
async def get_low_stock_alerts():
    # TODO: Implement low stock alerts
    # - Query products where inventory.quantity < inventory.reorder_level
    # - Include product name, warehouse, current stock, reorder_level
    # - Calculate suggested_reorder as (reorder_level * 2) - current quantity
    # - Follow the DAO pattern in models/database_models.py
    raise NotImplementedError("Low-stock alert not implemented.")


@router.post("/price/bulk_update", response_model=BulkPriceUpdateResponse)
async def bulk_price_update(req: BulkPriceUpdateRequest):
    # TODO: Update product prices in bulk, record all changes in price_history
    raise NotImplementedError("Bulk price update not implemented.")


@router.post("/inventory/transfer", response_model=WarehouseTransferResponse)
async def warehouse_transfer(req: WarehouseTransferRequest, background_tasks: BackgroundTasks):
    # TODO: Atomically move inventory from one warehouse to another
    raise NotImplementedError("Warehouse transfer not implemented.")


@router.get("/inventory/valuation", response_model=InventoryValuationResponse)
async def inventory_valuation():
    # TODO: Calculate current inventory value per warehouse
    raise NotImplementedError("Inventory valuation report not implemented.")
