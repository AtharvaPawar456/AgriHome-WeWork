#  tut : https://www.tutorialspoint.com/sqlite/sqlite_python.htm
import sqlite3

DATABASE = 'data.db'


def createDB(DATABASE):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS accountlogins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email_id TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("accountlogins db created")

def insertData(DATABASE):
  conn = sqlite3.connect(DATABASE)
  conn.execute("INSERT INTO accountlogins (username, email_id, password) VALUES ('atharva_pawar', 'talktoatharva14@gmail.com', '123')")
  conn.commit()
  print("Records created successfully")
  conn.close()

def Show_Data(DATABASE):
  conn = sqlite3.connect(DATABASE)
  print("Opened database successfully")
  c = conn.cursor()
  c.execute("SELECT * FROM accountlogins")
#   c.execute("SELECT * FROM products WHERE id = 1")  

  data = c.fetchall()
  for rowdata in data:
    print(f"{rowdata}\n")
  conn.close()


def update_data(DATABASE, name, email):
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("UPDATE accountlogins SET email = ? WHERE name = ?", (email, name))
  conn.commit()
  conn.close()


def delete_data(DATABASE, id):
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("DELETE FROM accountlogins WHERE id = ?", (id, ))
  conn.commit()
  conn.close()


# =============================================================================

# Show_Data(DATABASE)

# createDB(DATABASE)
# insertData(DATABASE)
# update_data(DATABASE, "Paul", "PaulABCmyabc@gmail.com")
# delete_data(DATABASE, "1")

Show_Data(DATABASE)


