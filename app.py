import streamlit as st
from rss_ingestion import fetch_rss_articles
from language_detection import detect_language
from text_summarizer import summarize_text
from sentiment_analysis import analyze_sentiment
from database import init_db, save_article

# Init DB

init_db()

st.title("📰 Multilingual News Summarization & Sentiment Analysis")

feed_urls = [
    "https://techcrunch.com/feed/",
    "http://feeds.bbci.co.uk/news/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

if st.button("Fetch Latest News"):
    articles = fetch_rss_articles(feed_urls, limit=3)
    for article in articles:
        st.subheader(article['title'])
        st.write(article['link'])
        
        lang = detect_language(article['content'])
        summary = summarize_text(article['content'])
        sentiment = analyze_sentiment(article['content'])

        st.write(f"**Language:** {lang}")
        st.write(f"**Summary:** {summary}")
        st.write(f"**Sentiment:** {sentiment['label']} (Score: {sentiment['score']:.2f})")

        save_article(article['title'], article['link'], lang, summary, sentiment['label'], sentiment['score'])
