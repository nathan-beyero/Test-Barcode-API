from typing import List, Optional
from datetime import date
from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    expiration_date: date
    
class Product(SQLModel, table=True): # make sure column names match the API response in upcitemdb.py
    id: Optional[int] = Field(default=None, primary_key=True)
    barcode: str = Field(index=True)
    name: str
    description: str
    brand: str
    image: str # image URL
    category: str
    # tags: List[str]   # do we want a separate table for tags?
    
