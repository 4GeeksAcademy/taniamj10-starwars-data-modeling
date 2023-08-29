import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)
    fav_characters = relationship('Fav_characters', backref='user', lazy=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250), nullable=False)
    eyes_color = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    birth_year = Column(Integer, nullable=False)
    fav_characters = relationship('Fav_characters', backref='user', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250))
    climate = Column(String(250))
    name = Column(String(250), nullable=False)
    terrain = Column(Integer, nullable=False)
    Height = Column(Integer, nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


class Fav_characters(Base):
    __tablename__ = 'fav_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
