from fastapi import FastAPI
from api import customer, employee, inventory, orders
from database.db_setup import engine
from database.models import people, products

people.Base.metadata.create_all(bind=engine)
products.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(customer.router)
app.include_router(employee.router)
app.include_router(inventory.router)
app.include_router(orders.router)