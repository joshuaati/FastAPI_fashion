from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..db_setup import Base
from.people import Employee, Customer
from .mixins import Timestamp

class InventoryModel(Timestamp, Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300), nullable = False)
    brand = Column(String(100), nullable = False)
    colour = Column(String(50), nullable = False)
    size = Column(Integer, nullable = False)
    type = Column(String(300), nullable = True)
    description = Column(Text, nullable = True)

    order = relationship("Order", back_populates="item")


class OrderModel(Timestamp, Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable = False)
    unit_price = Column(Float, nullable = False)
    order_description = Column(Text, nullable = True)
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)

    item = relationship("Inventory", back_populates="order")

    # item = relationship()
    employee = relationship(Employee, back_populates="order")
    customer = relationship(Customer, back_populates="order")