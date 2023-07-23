from sqlalchemy import create_engine, Column, DateTime, String, Float, MetaData, Integer, ForeignKey, UUID
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
# connection_url = 'postgresql://polka:qwerty@localhost:5432/Food_menu'




metadata = MetaData()
session = Session()

connection_url = "postgresql://localhost:5432/Food_menu?user=polka&password=qwerty"
engine = create_engine(connection_url)
sessionlocal = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


# Base.metadata.create_all(bind=engine)


class Menu(Base):
    __tablename__ = 'menus'
 
    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    submenus = relationship('Submenu', back_populates='menu', cascade='all, delete')
 
 
class Submenu(Base):
    __tablename__ = 'submenus'
 
    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    menu_id = Column(UUID, ForeignKey('menus.id'))
    menu = relationship('Menu', back_populates='submenus')
    dishes = relationship('Dish', back_populates='submenu', cascade='all, delete')
 
 
class Dish(Base):
    __tablename__ = 'dishes'
 
    id = Column(UUID, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(String, nullable=False)
    menu_id = Column(UUID, ForeignKey('menus.id'))
    submenu_id = Column(UUID, ForeignKey('submenus.id'))
    submenu = relationship('Submenu', back_populates='dishes')

# dish0 = Menu(title='pivo', description='40', submenus='40', uselist=False)
Base.metadata.create_all(bind=engine)
