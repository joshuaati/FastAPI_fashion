from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.db_setup import get_session
from pydantic_schemas.products import Order, OrderCreate, OrderUpdate
from api.utility.orders import get_order, get_orders, create_order, delete_order, update_order



router = fastapi.APIRouter()

@router.post("/orders", response_model=Order)
async def create_new_order(order: OrderCreate, db: Session = Depends(get_session)):
    return create_order(db=db, order=order)


@router.get("/orders", response_model=List[Order])
async def read_orders(db: Session = Depends(get_session)):
    orders = get_orders(db=db)
    return orders


@router.get("/orders/{order_id}", response_model=Order)
async def read_orders(order_id: int, db: Session = Depends(get_session)):
    order = get_order(db=db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.patch("/orders/{order_id}")
async def update_orders(order_id: int, order:OrderUpdate, db: Session = Depends(get_session)):
    order_up = update_order(db=db, order_id=order_id, order=order)
    return order_up


@router.delete("/orders/{order_id}")
async def delete_orders(order_id: int, db: Session = Depends(get_session)):
    order = get_order(db=db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    order = delete_order(db=db, order_id=order_id)