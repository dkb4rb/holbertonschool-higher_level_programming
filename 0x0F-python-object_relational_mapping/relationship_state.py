#!/usr/bin/python3
"""
Create ne function to conect MySQLdb
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

Base = declarative_base()


class State(Base):
    """ This is State Model Representation
    Values for the connect to the database
    __tablename__ (str): reference to name table
    id (Integer): value the id
    name (String): value the name state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
