from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

database_name = 'database.sqlite'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/publish', methods=['POST'])
def publish():
    title = request.form.get('title')
    content = request.form.get('content')
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO posts (title, content, created_at, author) VALUES (title, content, {now_str},)
        """)

    return 201

if __name__ == "__main__":
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                created_at TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """)

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )
                """)

    app.run(debug=True)