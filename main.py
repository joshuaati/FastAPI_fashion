from fastapi import FastAPI
from api import customer, employee, inventory, orders



app = FastAPI()


app.include_router(customer.router)
app.include_router(employee.router)
app.include_router(inventory.router)
app.include_router(orders.router)