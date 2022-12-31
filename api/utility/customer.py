from sqlalchemy.orm import Session
from datetime import datetime

from database.models.people import CustomerModel
from pydantic_schemas.people import CustomerCreate, CustomerUpdate


def get_customer(db: Session, customer_id: int):
    return db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CustomerModel).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: CustomerCreate):
    db_customer = CustomerModel(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def update_customer(db: Session, customer_id:int, customer: CustomerUpdate):
    db_customer_up = db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()
    db_customer_up.first_name = customer.first_name
    db_customer_up.last_name = customer.last_name
    db_customer_up.gender = customer.gender
    db_customer_up.dobirth = customer.dobirth
    db_customer_up.email = customer.email
    db_customer_up.phone = customer.phone
    db_customer_up.updated_at = datetime.utcnow()

    db.commit()
    db.close()
    return db_customer_up


def delete_customer(db: Session, customer_id:int):
    db_customer_dt = db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()
    db.delete(db_customer_dt)
    db.commit()
    db.close()