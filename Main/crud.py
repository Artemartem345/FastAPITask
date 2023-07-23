from sqlalchemy.orm import Session
from models import *
from schema import MenuSchema
# Получение блюда
def get_dish(db:Session):
    if db is None:
        return []
    return db
# Получение блюда по айдишнику
def get_dish_by_id(db:Session, dish_id):
    return db.query(MenuSchema).filter(Menu.id == dish_id).first()
# Создание блюда
def create_dish(db:Session, dish: Menu):
    _dish = Menu(title=dish.title,description=dish.description)
    db.add(_dish)
    db.commit()
    db.refresh(_dish)
    return _dish
# Удаление блюда
def remove_dish(db:Session, dish_id: Menu):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    db.delete(_dish)
    db.commit()
# Обновление блюда
def update_dish(db:Session, dish_id: Menu, title:str, description:str):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    _dish.title = title
    _dish.description = description
    db.commit()
    db.refresh(_dish)
    return _dish
    

