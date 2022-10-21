#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""

        @property
        def cities(self):
            ''' Return the cities linkes to the current state '''
            dic = FileStorage().all()
            cities = []
            for key, value in dic.items():
                try:
                    if value.state_id == self.id:
                        cities.append(value)
                except:
                    pass
            return (cities)

    def __init__(self, *argv, **kargs):
        """initialization"""
        super().__init__(*argv, **kargs)
