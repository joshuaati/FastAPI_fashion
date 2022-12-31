from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class InventoryBase(BaseModel):
    name: str
    brand: str
    colour: str
    size: int
    type: Optional[str] = None
    description: Optional[str] = None


class InventoryCreate(InventoryBase):
    ...

class InventoryUpdate(InventoryBase):
    ...


class Inventory(InventoryBase):
    inventory_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True



class OrderBase(BaseModel):
    quantity:int
    unit_price:float
    order_description:Optional[str] = None
    inventory_id:str
    employee_id:str
    customer_id:str


class OrderCreate(OrderBase):
    ...


class OrderUpdate(OrderBase):
    ...


class Order(OrderBase):
    order_id: int
    created_at: datetime
    updated_at: datetime
    

    class Config:
        orm_mode = True



