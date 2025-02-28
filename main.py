
import requests  
from fastapi import FastAPI  

app = FastAPI()  

# کلید API و CX را جایگزین کن
GOOGLE_API_KEY = "AIzaSyCNC_HYgzwb9O4VURp1a5Mez6fhwHsH5qI"  
SEARCH_ENGINE_ID = "93935e66217854acd"  

@app.get("/search/")
async def search_google(query: str):  
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}"  
    response = requests.get(url)  
    return response.json()
