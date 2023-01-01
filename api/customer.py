from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.db_setup import get_session
from pydantic_schemas.people import Customer, CustomerCreate, CustomerUpdate
from pydantic_schemas.products import Order
from api.utility.customer import get_customer, get_customers, get_customer_by_email, get_customer_orders, create_customer, update_customer, delete_customer

router = fastapi.APIRouter()


@router.post("/customer", response_model=Customer)
async def create_new_customer(customer: CustomerCreate, db: Session = Depends(get_session)):
    customer_email = get_customer_by_email(db=db, email=customer.email)
    if customer_email:
        raise HTTPException(status_code=404, detail="Email is already registered")
    return create_customer(db=db, customer=customer)


@router.get("/customer", response_model=List[Customer])
async def read_customers(db: Session = Depends(get_session)):
    return get_customers(db=db)


@router.get("/customer{customer_id}", response_model=Customer)
async def read_customer(customer_id: int, db: Session = Depends(get_session)):
    customer = get_customer(db=db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer does not exist")
    return customer


@router.get("/customer{customer_id}/orders", response_model=List[Order])
async def read_customer_orders(customer_id: int, db: Session = Depends(get_session)):
    customer = get_customer(db=db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer does not exist")
    orders = get_customer_orders(db=db, customer_id=customer_id)
    if orders is None:
        raise HTTPException(status_code=404, detail="Customer doesn't have any order")
    return orders


@router.patch("/customer{customer_id}")
async def update_customers(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_session)):
    return update_customer(db=db, customer_id=customer_id, customer=customer)


@router.delete("/customer{customer_id}")
async def delete_customers(customer_id: int, db: Session = Depends(get_session)):
    customer = get_customer(db=db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer does not exist")
    return delete_customer(db=db, customer_id=customer_id)