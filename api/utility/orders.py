from sqlalchemy.orm import Session
from datetime import datetime

from database.models.products import OrderModel
from pydantic_schemas.products import OrderCreate, OrderUpdate


def get_order(db: Session, order_id):
    return db.query(OrderModel).filter(OrderModel.order_id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(OrderModel).offset(skip).limit(limit).all()


def create_order(db: Session, order: OrderCreate):
    db_order = OrderModel(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id:int, order: OrderUpdate):
    db_order_up = db.query(OrderModel).filter(OrderModel.order_id == order_id).first()
    db_order_up.quantity = order.quantity
    db_order_up.unit_price = order.unit_price
    db_order_up.order_description = order.order_description
    db_order_up.inventory_id = order.inventory_id
    db_order_up.employee_id = order.employee_id
    db_order_up.customer_id = order.customer_id
    db_order_up.updated_at = datetime.utcnow()

    db.commit()
    db.close()
    return db_order_up


def delete_order(db: Session, order_id:int):
    db_order_dt = db.query(OrderModel).filter(OrderModel.order_id == order_id).first()
    db.delete(db_order_dt)
    db.commit()
    db.close()