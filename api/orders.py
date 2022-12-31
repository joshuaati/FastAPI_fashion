from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.db_setup import get_session
from pydantic_schemas.products import OrderCreate, Order
from api.utility.orders import get_order, get_orders, create_order, delete_order, update_order, get



router = fastapi.APIRouter()

@router.post("/orders", response_model=Order)
async def create_new_order(order: OrderCreate, db: Session = Depends(get_session)):
    return create_order(db=db, order=order)


@router.get("/orders", response_model=List[Order])
async def read_orders(db: Session = Depends(get_session)):
    orders = get_orders(db=db)
    return orders


@router.get("/orders/{order_id}")
async def read_orders(order_id: int, db: Session = Depends(get_session)):
    order = get_order(db=db, order_id=order_id)


@router.patch("/orders/{order_id}")
async def update_order():
    ...


@router.delete("/orders/{order_id}")
async def delete_order():
    ...