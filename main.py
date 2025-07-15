from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/scrape")
def scrape():
    url = "https://www.sbs.com.au/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for link in soup.select(".titleline > a"):
        articles.append({
            "title": link.text,
            "link": link['href']
        })

    return articles
