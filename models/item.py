from pydantic import BaseModel 

class Item(BaseModel):
    barcode_id: str
    name: str
    available: bool
    amount: int
    category: list[str]
    tags: list[str]
