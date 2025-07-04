from pydantic import BaseModel
from typing import List

class ProductModel(BaseModel):
    id: int
    name: str
    price: int
    
class CategoryModel(BaseModel):
    id: int
    name: str

class OrderModel(BaseModel):
    id: int
    customer_name: str
    total: int

class OrderItemModel(BaseModel):
    id: int
    order_id: int
    product_id: int