from typing import List

from pydantic import BaseModel

class PointBase(BaseModel):
    name: str
    group_id: int
    device_id: str
    name: str


class PointCreate(PointBase):
    pass


class Point(PointBase):
    id: int

    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    name: str
    building_id: int


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    points: List[Point] = []

    class Config:
        orm_mode = True


class BuildingBase(BaseModel):
    org_id: int
    name: str
    address: str


class BuildingCreate(BuildingBase):
    pass


class Building(BuildingBase):
    id: int
    groups: List[Group] = []

    class Config:
        orm_mode = True


class OrgBase(BaseModel):
    name: str


class OrgCreate(OrgBase):
    pass


class Org(OrgBase):
    id: int
    name: str
    buildings: List[Building] = []

    class Config:
        orm_mode = True

