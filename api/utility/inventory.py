from datetime import datetime

from sqlalchemy.orm import Session

from database.models.products import InventoryModel
from pydantic_schemas.products import InventoryCreate, InventoryUpdate


def get_inventory(db: Session, inventory_id: int):
    return db.query(InventoryModel).filter(InventoryModel.inventory_id == inventory_id).first()


def get_inventories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InventoryModel).offset(skip).limit(limit).all()


def create_inventory(db: Session, inventory: InventoryCreate):
    db_inventory = InventoryModel(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory


def update_inventory(db: Session, inventory_id: int, inventory: InventoryUpdate):
    db_inventory_up = db.query(InventoryModel).filter(InventoryModel.inventory_id == inventory_id).first()
    db_inventory_up.name = inventory.name
    db_inventory_up.brand = inventory.brand
    db_inventory_up.colour = inventory.colour
    db_inventory_up.size = inventory.size
    db_inventory_up.type = inventory.type
    db_inventory_up.description = inventory.description
    db_inventory_up.updated_at = datetime.utcnow()

    db.commit()
    db.close()
    return db_inventory_up


def delete_inventory(db: Session, inventory_id: int):
    db_inventory_dt = db.query(InventoryModel).filter(InventoryModel.inventory_id == inventory_id).first()
    db.delete(db_inventory_dt)
    db.commit()
    db.close()