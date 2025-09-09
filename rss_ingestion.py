import feedparser
import requests
from bs4 import BeautifulSoup

def fetch_rss_articles(feed_urls, limit=5):
    articles = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            content = fetch_article_content(entry.link)
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "content": content
            })
    return articles

def fetch_article_content(url):
    
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return " ".join(paragraphs[:20])  # first 20 paragraphs
    except Exception as e:
        return f"Error fetching content: {e}"