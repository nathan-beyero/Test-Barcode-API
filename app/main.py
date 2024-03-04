from fastapi import FastAPI, HTTPException
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


@app.get("/barcode/{barcode}", status_code=200, tags=["Barcode Lookup"])
async def barcode(barcode: str):
    
    product = db.get_product(barcode.zfill(13)) # pad zeroes to make it 13 digits
    
    if product is None:
        try:
            product = upc_item_db.get_product(barcode)
            
        except Exception as e:
            return {"error": str(e)}
        
        if product is None:
            return {"error": "Product not found."}
        
        product = Product(**product)
        db.create_product(product)

    return product


@app.post("/api/add_item", status_code=201, tags=["Database Management"])
async def add_item(item: Item):
    db.add_item(item)
    return


@app.get('/api/get_all_items', tags=["Database Management"])
async def get_all_items():
    return db.get_all_items()


@app.get('/api/get_all_products', tags=["Database Management"])
async def get_all_products():
    return db.get_all_products()


@app.get("/test/delete_tables", tags=["Test"])
async def test_drop_tables():
    db.drop_tables()
    return


@app.get("/test/upc", tags=["Test"])
async def test_upc():
    item = upc_item_db.get_product("0885909950805")

    if item is None:
        return {"error": "UPC API is down."}
    
    return {"upc": item}