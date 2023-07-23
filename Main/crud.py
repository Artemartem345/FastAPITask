from sqlalchemy.orm import Session
from models import *
from schema import *

# Блюда
# Получение блюда
def get_dish(db:Session):
    if db is None:
        return []
    return db
# Получение блюда по айдишнику
def get_dish_by_id(db:Session, dish_id):
    return db.query(DishResponse).filter(Dish.id == dish_id).first()
# Создание блюда
def create_dish(db:Session, dish: DishCreate):
    _dish = Dish(title=dish.title,description=dish.description)
    db.add(_dish)
    db.commit()
    db.refresh(_dish)
    return _dish
# Удаление блюда
def remove_dish(db:Session, dish_id: Dish):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    db.delete(_dish)
    db.commit()
# Обновление блюда
def update_dish(db:Session, dish_id: DishUpdate, title:str, description:str):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    _dish.title = title
    _dish.description = description
    db.commit()
    db.refresh(_dish)
    return _dish
    
    

# Меню

def get_menu(db:Session):
    if db is None:
        return []
    return db

def get_menu_by_id(db:Session, menu_id: int):
    return db.query(Menu).filter(menu_id == menu_id).first()

def create_menu(db: Session, menu):
    _menu = menu(title=menu.title, description=menu.description)
    db.add(_menu)
    db.commit()
    db.refresh(_menu)
    return _menu

def remove_menu(db:Session, menu_id):
    _menu = get_menu_by_id(title=menu_id.title, description=menu_id.description)
    db.delete(_menu)
    db.commit()
    
def update_menu(db:Session, menu_id:uuid.UUID, title:str, description:str):
    _menu = get_menu_by_id(db=db, menu_id=menu_id)
    _menu.title = title
    _menu.description = description
    db.commit()
    db.refresh(_menu)
    return _menu


# СабМеню

def get_menu(db:Session):
    if db is None:
        return []
    return db

def get_submenu_by_id(db:Session, menu_id: int):
    return db.query(Menu).filter(SubmenuResponse.id == menu_id).first()

def create_menu(db: Session, menu):
    _menu = SubmenuCreate(title=menu.title, description=menu.description)
    db.add(_menu)
    db.commit()
    db.refresh(_menu)
    return _menu

def remove_menu(db:Session, submenu_id):
    _menu = get_submenu_by_id(title=submenu_id.title, description=submenu_id.description)
    db.delete(_menu)
    db.commit()
    
def update_menu(db:Session, submenu_id:SubmenuUpdate, title:str, description:str):
    _submenu = get_submenu_by_id(db=db, submenu_id=submenu_id)
    _submenu.title = title
    _submenu.description = description
    db.commit()
    db.refresh(_submenu)
    return _submenu




    
    
