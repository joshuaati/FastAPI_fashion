from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..db_setup import Base
from.people import EmployeeModel, CustomerModel
from .mixins import Timestamp


class InventoryModel(Base, Timestamp):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300), nullable = False)
    brand = Column(String(100), nullable = False)
    colour = Column(String(50), nullable = False)
    size = Column(Integer, nullable = False)
    type = Column(String(300), nullable = True)
    description = Column(Text, nullable = True)

    order = relationship("OrderModel", back_populates="item")


class OrderModel(Base, Timestamp):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable = False)
    unit_price = Column(Float, nullable = False)
    order_description = Column(Text, nullable = True)
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)

    item = relationship("InventoryModel", back_populates="order")

    employee = relationship(EmployeeModel, back_populates="order")
    customer = relationship(CustomerModel, back_populates="order")