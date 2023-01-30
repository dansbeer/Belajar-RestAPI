from fastapi import FastAPI

app = FastAPI(title="My First Rest API")


@app.get("/items/{item_id}", tags=["items"], summary="Read Item Only", description="Read Item Cooler")
async def read_item(item_id: int):
    return {"item_id": item_id}
