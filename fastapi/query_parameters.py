from typing import Optional

from fastapi import FastAPI, Query


app = FastAPI()

# Add regular expressions¶
# ^: starts with the following characters, doesn't have characters before.
# fixedquery: has the exact value fixedquery.
# $: ends there, doesn't have any more characters after fixedquery.

@app.get("/items/")  #q]  it's of type str but could also be None, and indeed, the default value is None, so FastAPI will know it's not required.
# async def read_items(q: Optional[str] = None):
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")): # Query serves the same purpose of defining that default value.
async def read_items(q: str = Query("fixedquery", min_length=3)):    
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

