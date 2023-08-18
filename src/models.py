import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    fav_planets = relationship('Fav_planets', backref='person', lazy=True)
    fav_characters = relationship('Fav_characters', backref='person', lazy=True)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    character_gender = Column(String(250))
    character_hair_color = Column(String(250), nullable=False)
    fav_characters = relationship('Fav_characters', backref='person', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planets_diameter = Column(String(250))
    planets_climate = Column(String(250))
    planets_name = Column(String(250), nullable=False)
    fav_planets = relationship('Fav_planets', backref='person', lazy=True)

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer,ForeignKey('person.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


class Fav_characters(Base):
    __tablename__ = 'fav_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer,ForeignKey('person.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
