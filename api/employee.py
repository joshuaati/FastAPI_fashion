import fastapi

router = fastapi.APIRouter()


@router.post("/employees")
async def create_new_employee():
    ...


@router.get("/employees")
async def read_employees():
    ...


@router.get("/employees{employee_id}")
async def read_employees():
    ...


@router.get("/employees{employee_id}/orders")
async def read_employees_orders():
    ...


@router.patch("/employees{employee_id}")
async def update_employees():
    ...


@router.delete("/employees{employee_id}")
async def delete_employees():
    ...