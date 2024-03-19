from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse

from wrappers.upcitemdb import UPCItemDB

from models.models import Item, Product
import db.db as db

app = FastAPI()

upc_item_db = UPCItemDB()


db.create_tables()


@app.get("/", tags=["Root"], include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.get("/products/{barcode}", status_code=status.HTTP_200_OK, tags=["Barcode Lookup"])
async def get_product_by_barcode(barcode: str):
    """Get product by barcode. If product is not found in the database, it will be fetched from the UPC API."""
    
    barcode = barcode.strip().zfill(13) # pad zeroes to make it 13 digits
    product = db.get_product(barcode) 
    
    if product is None:
        try:
            product = upc_item_db.get_product(barcode)
            
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="UPC API is down.")
        
        if product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.")
        
        product = Product(**product)
        
        # Do we want to automatically add the product to the database?
        
        # product.barcode = barcode
        # db.create_product(product)

    return product


@app.post("/products", status_code=status.HTTP_201_CREATED, tags=["Database Management"])
async def create_product(product: Product):
    """Create a new product."""
    return db.create_product(product)


@app.get('/products', status_code=status.HTTP_200_OK, tags=["Database Management"])
async def get_all_products():
    """Get all products."""
    return db.get_all_products()


@app.post("/items", status_code=status.HTTP_201_CREATED, tags=["Database Management"])
async def add_items(items: List[Item]):
    """Add items to the database."""
    for item in items:
        db.add_item(item)
    return


@app.get('/items', status_code=status.HTTP_200_OK, tags=["Database Management"])
async def get_all_items():
    """Get all items."""
    return db.get_all_items()


@app.get("/inventory/summary", status_code=status.HTTP_200_OK, tags=["Database Management"])
async def get_inventory_summary():
    """Get a summary of the inventory."""
    summary = {
        "total_items": db.get_num_items(),
        "total_products": db.get_num_products(),
    }
    
    return summary


@app.get("/reset", status_code=status.HTTP_200_OK, tags=["Test"])
async def wipe_all_data():
    """Drop all tables in the database. For testing purposes only."""
    db.drop_tables()
    return
