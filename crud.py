from sqlalchemy.orm import Session

import models
import schemas

def get_org(db: Session, org_id: int):
    return db.query(models.Org).filter(models.Org.id == org_id).first()


def get_org_by_name(db: Session, name: str):
    return db.query(models.Org).filter(models.Org.name == name).first()


def get_orgs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Org).offset(skip).limit(limit).all()


def create_org(db: Session, org: schemas.OrgCreate):
    db_org = models.Org(name=org.name)
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org


def get_building(db: Session, building_id: int):
    return db.query(models.Building).filter(models.Building.id == building_id).first()


def get_buildings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Building).offset(skip).limit(limit).all()


def create_org_building(db: Session, building: schemas.BuildingCreate, org_id: int):
    db_building = models.Building(**building.dict(), org_id=org_id)
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building

