from sqlalchemy import Column, Integer, String, Text, Date, Enum

from ..db_setup import Base


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHERS = "Others"

class Role(Enum):
    MANAGER = "Manager"
    SUPERVISOR = "Supervisor"
    WORKER = "Worker"
    INTERN = "Intern"

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index = True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Gender, nullable=False)
    dobirth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)


class Employee(Base):
    __tablename__ = "employees"
    
    employee_id = Column(Integer, primary_key=True, index = True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(Gender, nullable=False)
    dobirth = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)
    role = Column(Role, nullable = False)
