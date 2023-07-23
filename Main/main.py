from fastapi import FastAPI, Response
import models
from models import *
from schema import *
from sqlalchemy.orm import Session

from crud import *


app = FastAPI()



@app.post('/api/v1/menus/', response_model=MenuCreate, status_code=201)
def post_menu(title:str, description:str, db:Session) -> Response:
    create_new_menu = create_dish(db, title, description)
    return create_new_menu
models.Base.metadata.create_all(bind=engine)