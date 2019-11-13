from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

import datetime

from database import Base

class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    buildings = relationship("Building", back_populates="org")


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, ForeignKey(Org.id))
    name = Column(String, unique=True, index=True)
    address = Column(String)

    org = relationship("Org", back_populates="buildings")
    groups = relationship("Group", back_populates="building")


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey(Building.id))
    name = Column(String, index=True)

    building = relationship("Building", back_populates="groups")
    points = relationship("Point", back_populates="building")


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey(Building.id))
    device_id = Column(Integer, index=True)
    name = Column(String)
    location = Column(String)
    
    building = relationship("Group", back_populates="points")