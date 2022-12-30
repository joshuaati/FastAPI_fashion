import fastapi

router = fastapi.APIRouter()

@router.post("/inventory")
async def create_new_inventory():
    ...


@router.get("/inventory")
async def read_inventory():
    ...


@router.get("/inventory{inventory_id}")
async def read_inventory():
    ...


@router.patch("/inventory{inventory_id}")
async def update_inventory():
    ...


@router.delete("/inventory{inventory_id}")
async def delete_inventory():
    ...