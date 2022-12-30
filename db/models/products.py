from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship

from ..db_setup import Base
from.people import Employee, Customer
from .mixins import Timestamp

class Inventory(Timestamp, Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300), nullable = False)
    brand = Column(String(100), nullable = False)
    colour = Column(String(50), nullable = False)
    size = Column(Integer, nullable = False)
    type = Column(String(300), nullable = True)
    description = Column(Text, nullable = True)

class Orders(Timestamp, Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable = False)
    unit_price = Column(Float, nullable = False)

    item = relationship()
    employee = relationship()
    customer = relationship()