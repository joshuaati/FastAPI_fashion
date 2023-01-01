import enum
from sqlalchemy import Column, Integer, String, Text, Date, Enum
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp


class Gender(str, enum.Enum):
    Male = "Male"
    Female = "Female"
    Others = "Others"

class Role(str, enum.Enum):
    Manager = "Manager"
    Supervisor = "Supervisor"
    Worker = "Worker"
    Intern = "Intern"

class CustomerModel(Base, Timestamp):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index = True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    dobirth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)

    order = relationship("OrderModel", back_populates="customer")


class EmployeeModel(Base, Timestamp):
    __tablename__ = "employees"
    
    employee_id = Column(Integer, primary_key=True, index = True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    dobirth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)
    role = Column(Enum(Role), nullable = False)

    order = relationship("OrderModel", back_populates="employee")
