from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    expiration_date: datetime
    
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    barcode_id: str = Field(index=True)
    name: str
    description: str
    category: str
