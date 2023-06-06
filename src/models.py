import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(250), nullable=False)
    id_favorites= Column(Integer, ForeignKey('favorites.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey('planets.id'))
    name_planet = Column(String(250), nullable=False)
    id_character = Column(Integer, ForeignKey('characters.id'))
    name_character = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name_character = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    haircolor = Column(String(250), nullable=False)
    age = Column(String(250), nullable=False)
    favorites = relationship(Favorites)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planet = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    favorites = relationship(Favorites)

    def to_dict(self):
        return {}

# Dibujar el diagrama a partir de la base de datos de SQLAlchemy
render_er(Base, 'diagram.png')
## Draw from SQLAlchemy base