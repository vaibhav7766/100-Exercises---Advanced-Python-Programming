import csv
import sqlite3

product_constraints = [
    "INTEGER PRIMARY KEY",
    "TEXT NOT NULL",
    "INTEGER NOT NULL",
    "INTEGER NOT NULL",
    "TEXT NOT NULL",
    "REAL NOT NULL",
    "INTEGER NOT NULL",
    "INTEGER NOT NULL",
    "INTEGER NOT NULL",
    "INTEGER NOT NULL",
]


def generate_sql(table_name, col_names, constraints):
    cols = [
        " ".join((col, constraint)).strip()
        for col, constraint in zip(col_names, constraints)
    ]
    return f"CREATE TABLE IF NOT EXISTS {table_name} (" + ", ".join(cols) + ")"

with open("Product.csv", newline="") as f:
    reader = csv.reader(f)
    columns = next(reader)
    rows = [row for row in reader]

conn = sqlite3.connect("store.db")
cur = conn.cursor()

cur.execute(generate_sql("Product", columns, product_constraints))

insert_sql = f"INSERT INTO Product ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in columns])})"
cur.executemany(insert_sql, rows)

conn.commit()

print(cur.execute("SELECT COUNT(*) FROM Product").fetchone()[0])

cur.close()
conn.close()
