from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

class ItemList(BaseModel):
    items: List[Item]

@app.post("/total_price/")
async def calculate_total_price(item_list: ItemList):
    total_price = sum(item.price for item in item_list.items)
    return {"total_price": total_price}
