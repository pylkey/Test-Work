from typing import List
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: str
    description: str 
    link: str

class ProductCreate(ProductBase):
    ...

class History(BaseModel):
    price:str

class ProductHistory(ProductBase):
    id: str
    prices:List[History]

    class Config:
        orm_mode = True

class Product(ProductBase):
    id: str

    class Config:
        orm_mode = True