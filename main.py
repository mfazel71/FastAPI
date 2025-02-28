import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
async def search_duckduckgo(query: str):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    return response.json()