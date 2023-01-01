from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.db_setup import get_session
from pydantic_schemas.products import Inventory, InventoryCreate, InventoryUpdate
from api.utility.inventory import get_inventory, get_inventories, create_inventory, delete_inventory, update_inventory


router = fastapi.APIRouter()

@router.post("/inventories", response_model=Inventory)
async def create_new_inventory(inventory: InventoryCreate, db: Session = Depends(get_session)):
    return create_inventory(db=db, inventory=inventory)


@router.get("/inventories", response_model=List[Inventory])
async def read_inventory(db: Session = Depends(get_session)):
    return get_inventories(db=db)


@router.get("/inventories/{inventory_id}", response_model=Inventory)
async def read_inventory(inventory_id: int, db: Session = Depends(get_session)):
    inventory = get_inventory(db=db, inventory_id=inventory_id)
    if inventory is None:
        raise HTTPException(status_code=404, detail="Item does not exist")
    return inventory        


@router.patch("/inventories/{inventory_id}")
async def update_inventories(inventory_id: int, inventory: InventoryUpdate, db: Session = Depends(get_session)):
    return update_inventory(db=db, inventory_id=inventory_id, inventory=inventory)


@router.delete("/inventories/{inventory_id}")
async def delete_inventories(inventory_id: int, db: Session = Depends(get_session)):
    inventory = get_inventory(db=db, inventory_id=inventory_id)
    if inventory is None:
        raise HTTPException(status_code=404, detail="Item does not exist")
    return delete_inventory(db=db, inventory_id=inventory_id)