from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from sqlalchemy import UUID

T = TypeVar('T')

class MenuSchema(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    description: Optional[str]=None
    
    
    class Config:
        orm_mode = True
        
class SubMenuSchema(BaseModel):
    parameter: MenuSchema = Field(...)
    id: Optional[int]=None
    title: Optional[str]=None
    description: Optional[str]=None
    
        
        
class MenuSubmenusSchema(BaseModel):
    parameter: SubMenuSchema = Field(...) 
    id: Optional[str]=None 
    title: Optional[str]=None
    description: Optional[str]=None
    submenus: List[SubMenuSchema]=None
    