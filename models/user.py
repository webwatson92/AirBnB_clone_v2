#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user', cascade='all, delete')
        reviews = relationship("Review", backref="user", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """ Initialitation """
        super().__init__(*args, **kwargs)
