#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import Column, String, Float, Integer, Table


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """ Getter attribute for cities in FileStorage """
        from models import storage
        city_list = [city for city in storage.all("City").values() if city.state_id == self.id]
        return city_list
