from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.db_setup import get_session
from pydantic_schemas.people import Employee, EmployeeCreate, EmployeeUpdate
from pydantic_schemas.products import Order
from api.utility.employee import get_employee, get_employees, get_employee_by_email, get_employee_orders, create_employee, update_employee, delete_employee

router = fastapi.APIRouter()


@router.post("/employees", response_model=Employee)
async def create_new_employee(employee: EmployeeCreate, db: Session = Depends(get_session)):
    employee_email = get_employee_by_email(db=db, email=employee.email)
    if employee_email:
        raise HTTPException(status_code=404, detail="Email is already registered")
    return create_employee(db=db, employee=employee)


@router.get("/employees", response_model=List[Employee])
async def read_employees(db: Session = Depends(get_session)):
    return get_employees(db=db)


@router.get("/employees/{employee_id}", response_model=Employee)
async def read_employee(employee_id: int, db: Session = Depends(get_session)):
    employee = get_employee(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    return employee


@router.get("/employees/{employee_id}/orders", response_model=List[Order])
async def read_employees_orders(employee_id: int, db: Session = Depends(get_session)):
    employee = get_employee(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    orders = get_employee_orders(db=db, employee_id=employee_id)
    if orders == []:
        raise HTTPException(status_code=404, detail="Employee doesn't have any orders yet")
    return orders


@router.patch("/employees/{employee_id}")
async def update_employees(employee_id:int, employee: EmployeeUpdate, db: Session = Depends(get_session)):
    return update_employee(db=db, employee_id=employee_id, employee=employee)


@router.delete("/employees/{employee_id}")
async def delete_employees(employee_id:int, db: Session = Depends(get_session)):
    employee = get_employee(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee does not exist")
    return delete_employee(db=db, employee_id=employee_id)