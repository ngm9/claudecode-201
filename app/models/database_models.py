from supabase import Client


def update_inventory_quantity(supabase: Client, product_id: int, warehouse_id: int, quantity_delta: int, movement_type: str, reference: str | None = None, notes: str | None = None, user_name: str | None = None) -> dict:
    """Update inventory for a product in a warehouse and log the movement.

    Returns dict with 'success' (bool) and 'message' (str).
    """
    # Get current inventory row
    result = supabase.table("inventory").select("id, quantity").eq(
        "product_id", product_id
    ).eq("warehouse_id", warehouse_id).execute()

    if not result.data:
        return {"success": False, "message": f"No inventory record for product {product_id} in warehouse {warehouse_id}"}

    current = result.data[0]
    new_quantity = current["quantity"] + quantity_delta

    # Block negative stock for 'out' movements
    if movement_type == "out" and new_quantity < 0:
        return {
            "success": False,
            "message": f"Insufficient stock. Available: {current['quantity']}, requested: {abs(quantity_delta)}",
        }

    # Update the quantity
    supabase.table("inventory").update({"quantity": new_quantity}).eq(
        "id", current["id"]
    ).execute()

    # Log the movement
    movement = {
        "product_id": product_id,
        "warehouse_id": warehouse_id,
        "movement_type": movement_type,
        "quantity_delta": quantity_delta,
        "reference": reference,
        "notes": notes,
        "user_name": user_name,
    }
    supabase.table("inventory_movements").insert(movement).execute()

    return {"success": True, "message": f"Inventory updated. New quantity: {new_quantity}"}
