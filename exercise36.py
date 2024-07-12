import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE category(
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL)
"""
)

cur.executescript(
    """
INSERT INTO category (category_name) VALUES ('technology');
INSERT INTO category (category_name) VALUES ('e-commerce');
INSERT INTO category (category_name) VALUES ('gaming');
"""
)

conn.commit()

categories = []
for row in cur.execute("SELECT * FROM category"):
    categories.append(row)

print(categories)
