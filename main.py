from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

'''
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

'''

@app.post('/orgs/', response_model=schemas.Org)
def create_org(org: schemas.OrgCreate, db: Session = Depends(get_db)):
    db_org = crud.get_org_by_name(db, name=org.name)
    if db_org:
        raise HTTPException(status_code=400, detail="Org name already registered")
    return crud.create_org(db=db, org=org)

@app.get('/orgs/', response_model=List[schemas.Org])
def read_orgs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orgs = crud.get_orgs(db, skip=skip, limit=limit)
    return orgs

@app.get('/orgs/{org_id}', response_model=schemas.Org)
def read_org(org_id: int, db: Session = Depends(get_db)):
    db_org = crud.get_org(db, org_id=org_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Org not found")
    return db_org

@app.post('/orgs/{org_id}/buildings/', response_model=schemas.Building)
def create_building_for_org(
    org_id: int, building: schemas.BuildingCreate, db: Session = Depends(get_db)
):
    return crud.create_org_building(db=db, building=building, org_id=org_id)
