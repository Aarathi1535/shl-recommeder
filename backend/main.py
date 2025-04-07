from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search")
def search(query: str = Query(...)):
    return {"query": query, "results": [f"Result for '{query}'", f"Another result for '{query}'"]}
