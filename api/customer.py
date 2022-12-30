import fastapi

router = fastapi.APIRouter()

@router.post("/customer")
async def create_new_customer():
    ...


@router.get("/customer")
async def read_customer():
    ...


@router.get("/customer{customer_id}")
async def read_customer():
    ...

@router.get("/customer{customer_id}/orders")
async def read_customer_orders():
    ...


@router.patch("/customer{customer_id}")
async def update_customer():
    ...


@router.delete("/customer{customer_id}")
async def delete_customer():
    ...