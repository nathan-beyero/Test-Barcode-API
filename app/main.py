from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from wrappers.upcitemdb import UPCItemDB

from models import Item

app = FastAPI()

upc_item_db = UPCItemDB()

@app.get("/", tags=["Root"], include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/barcode/{barcode}", status_code=200, tags=["Barcode Lookup"])
async def barcode(barcode: str):
    try:
        item = {
            "upc_database": upc_item_db.get_item(barcode)
        }
    except Exception as e:
        return {"error": str(e)}

    return item

@app.post("/api/add_item", tags=["Database Management"])
async def add_item(item: Item):
    return

@app.post("/api/check_out_item", tags=["Database Management"])
async def checkout_item(barcode_id: str, amount: int):
    return

@app.get("/test/upc", tags=["Test"])
async def test():
    item = upc_item_db.get_item("0885909950805")

    if item is None:
        return {"error": "Item not found"}
    
    return {"upc": item}