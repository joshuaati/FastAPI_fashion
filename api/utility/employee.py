from sqlalchemy.orm import Session
from datetime import datetime

from database.models.people import EmployeeModel
from pydantic_schemas.people import EmployeeCreate, EmployeeUpdate


def get_employee(db: Session, employee_id):
    return db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EmployeeModel).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = EmployeeModel(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, employee_id:int, employee: EmployeeUpdate):
    db_employee_up = db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id).first()
    db_employee_up.first_name = employee.first_name
    db_employee_up.last_name = employee.last_name
    db_employee_up.gender = employee.gender
    db_employee_up.dobirth = employee.dobirth
    db_employee_up.email = employee.email
    db_employee_up.phone = employee.phone
    db_employee_up.role = employee.role
    db_employee_up.updated_at = datetime.utcnow()

    db.commit()
    db.close()
    return db_employee_up

def delete_employee(db: Session, employee_id:int):
    db_employee_dt = db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id).first()
    db.delete(db_employee_dt)
    db.commit()
    db.close()