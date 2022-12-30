import fastapi

router = fastapi.APIRouter()

@router.post("/order")
async def create_new_order():
    ...


@router.get("/order")
async def read_orders():
    ...


@router.get("/order{order_id}")
async def read_orders():
    ...


@router.patch("/order{order_id}")
async def update_order():
    ...


@router.delete("/order{order_id}")
async def delete_order():
    ...