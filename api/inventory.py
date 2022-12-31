import fastapi

router = fastapi.APIRouter()

@router.post("/inventories")
async def create_new_inventory():
    ...


@router.get("/inventories")
async def read_inventory():
    ...


@router.get("/inventories/{inventory_id}")
async def read_inventory():
    ...


@router.patch("/inventories/{inventory_id}")
async def update_inventory():
    ...


@router.delete("/inventories/{inventory_id}")
async def delete_inventory():
    ...