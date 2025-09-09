import sqlite3

def init_db():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT,
            language TEXT,
            summary TEXT,
            sentiment TEXT,
            score REAL
        )
    """)
    conn.commit()
    conn.close()

def save_article(title, link, language, summary, sentiment, score):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO news (title, link, language, summary, sentiment, score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, link, language, summary, sentiment, score))
    conn.commit()
    conn.close()
