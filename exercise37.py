import sqlite3


conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE category (
    category_id   INTEGER,
    category_name TEXT    NOT NULL,
    PRIMARY KEY (category_id)
)"""
)

cur.execute("""INSERT INTO category (category_name) VALUES ('technology')""")
cur.execute("""INSERT INTO category (category_name) VALUES ('e-commerce')""")
cur.execute("""INSERT INTO category (category_name) VALUES ('gaming')""")

cur.execute(
    """UPDATE category SET category_name = 'online shop' where category_id = 2"""
)

l = cur.execute("SELECT * FROM category").fetchall()
print(*l, end="\n")

# Enter your solution here
conn.commit()
conn.close()
