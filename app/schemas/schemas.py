from pydantic import BaseModel, Field
from typing import List, Optional

class CategoryInfo(BaseModel):
    id: int
    name: str
    parent_id: Optional[int]

class SupplierInfo(BaseModel):
    id: int
    name: str
    rating: Optional[int]

class WarehouseInfo(BaseModel):
    id: int
    name: str
    location: str

class ProductInfo(BaseModel):
    id: int
    name: str
    description: Optional[str]
    base_price: float
    category: Optional[CategoryInfo]
    supplier: Optional[SupplierInfo]
    inventory: List[dict] = []  # {warehouse_id, quantity}

class ProductListResponse(BaseModel):
    products: List[ProductInfo]
    total: int

class InventoryUpdateRequest(BaseModel):
    product_id: int
    warehouse_id: int
    quantity_delta: int  # +ve for in, -ve for out
    movement_type: str  # 'in','out','adjustment','transfer'
    reference: Optional[str]
    notes: Optional[str]

class InventoryUpdateResponse(BaseModel):
    success: bool
    message: Optional[str]

class LowStockAlert(BaseModel):
    product_id: int
    product_name: str
    warehouse_id: int
    available: int
    reorder_level: int
    suggested_reorder: int

class LowStockAlertResponse(BaseModel):
    alerts: List[LowStockAlert]

class BulkPriceUpdateItem(BaseModel):
    product_id: int
    new_price: float
    reason: Optional[str]

class BulkPriceUpdateRequest(BaseModel):
    updates: List[BulkPriceUpdateItem]
    user: str

class BulkPriceUpdateResult(BaseModel):
    product_id: int
    success: bool
    message: Optional[str]

class BulkPriceUpdateResponse(BaseModel):
    results: List[BulkPriceUpdateResult]

class WarehouseTransferRequest(BaseModel):
    product_id: int
    source_warehouse_id: int
    dest_warehouse_id: int
    quantity: int
    user: str
    reference: Optional[str]
    notes: Optional[str]

class WarehouseTransferResponse(BaseModel):
    success: bool
    message: Optional[str]

class WarehouseValuation(BaseModel):
    warehouse_id: int
    warehouse_name: str
    inventory_value: float

class InventoryValuationResponse(BaseModel):
    valuations: List[WarehouseValuation]
