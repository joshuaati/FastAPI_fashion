from sqlalchemy import Column, Integer, String, Text, Date, Enum
from sqlalchemy.orm import relationship

from ..db_setup import Base



class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
    Others = "Others"

class Role(str, Enum):
    Manager = "Manager"
    Supervisor = "Supervisor"
    Worker = "Worker"
    Intern = "Intern"

class CustomerModel(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index = True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Gender, nullable=False)
    dobirth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)

    order = relationship("Orders", back_populates="customer")


class EmployeeModel(Base):
    __tablename__ = "employees"
    
    employee_id = Column(Integer, primary_key=True, index = True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Gender, nullable=False)
    dobirth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)
    role = Column(Role, nullable = False)

    order = relationship("Orders", back_populates="employee")
