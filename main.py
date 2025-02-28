import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
async def search_duckduckgo(query: str):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url).json()
    
    results = []
    for item in response.get("RelatedTopics", []):
        if "FirstURL" in item and "Text" in item:
            results.append({
                "title": item["Text"],
                "url": item["FirstURL"]
            })

    return {"query": query, "results": results}