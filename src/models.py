import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))


    
class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastName = Column(String(250))
class FavoritoPersonajes(Base):
    __tablename__ = 'Personajes favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuarios = relationship(Usuario)
    personaje_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Personajes)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
class FavoritoPlanetas(Base):
    __tablename__ = 'Planetas favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuarios = relationship(Usuario)
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Planetas)


class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))    
class FavoritoVehiculos(Base):
    __tablename__ = 'Vehiculos favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuarios = relationship(Usuario)
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id'))
    vehiculos = relationship(Vehiculos)




    # def to_dict(self):
    #     return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')