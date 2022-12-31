from datetime import date, datetime
from pydantic import BaseModel
from database.models.people import Role, Gender


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    dobirth: date
    email: str
    phone: str


class CustomerCreate(CustomerBase):
    ...

class CustomerUpdate(CustomerBase):
    updated_at: datetime


class Customer(CustomerBase):
    customer_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True



class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    dobirth: date
    email: str
    phone: str
    role: Role


class EmployeeCreate(EmployeeBase):
    ...


class EmployeeUpdate(EmployeeBase):
    ...


class Employee(EmployeeBase):
    employee_id:int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True





