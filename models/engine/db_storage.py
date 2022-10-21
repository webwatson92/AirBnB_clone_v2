#!/usr/bin/python3
"""module that contain DBStorage"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import scoped_session
from os import getenv

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """ declaration class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ declaration class DBStorage """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = 'localhost'
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ''' show all class'''
        my_dict = {}
        if cls is None:
            for my_class in classes:
                my_query = self.__session.query(eval(my_class)).all()
                for obj in my_query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    my_dict[key] = obj
        else:
            my_query = self.__session.query(cls).all()
            for obj in my_query:
                key = obj.__class__.__name__ + '.' + obj.id
                my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """new obj add table"""
        self.__session.add(obj)

    def save(self):
        """save obj with commit"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete node """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload data"""
        Base.metadata.create_all(self.__engine)
        sessionFactory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session

    def close(self):
        ''' Close session '''
        self.__session.close()
