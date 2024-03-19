from typing import List, Optional
from datetime import date
from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    expiration_date: date
    
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    barcode: str = Field(index=True)
    name: str
    description: str
    brand: str
    # image: List[str]
    category: str
    # tags: List[str]
