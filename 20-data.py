import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Mani', 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Sahar', 30))

conn.commit()
cursor.execute("SELECT * from USERS")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
