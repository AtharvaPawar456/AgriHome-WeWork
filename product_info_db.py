#  tut : https://www.tutorialspoint.com/sqlite/sqlite_python.htm
import sqlite3

DATABASE = 'data.db'


def createDB(DATABASE):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT,
            product_img_name TEXT,
            description TEXT,
            benefits TEXT,
            how_to_use TEXT,
            category TEXT,
            slug TEXT,
            mrp INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insertData(DATABASE):
  conn = sqlite3.connect(DATABASE)
  print("Opened database successfully")
  conn.execute("INSERT INTO products (product_title, product_img_name, description, benefits, how_to_use, category,slug, mrp) VALUES ('DXN 2 in 1 Coffee',\
               'gano-tea.jpg',\
               'DXN Reishi Gano Tea is blended with high quality Ganoderma powder. It has no added preservatives, artificial colouring and flavourings. DXN Reishi Gano Tea invigorates your mind and body and delights you with its exceptional flavour and pleasant aroma.',\
               'provides refreshment, help to relieve stress, promotes energy & wellness, strengthens immune system, helps in detoxification, supports in maintaining balance of the body',\
               'To prepare DXN Reishi Gano Tea, boil water, open a sachet of the tea, pour hot water over the tea powder, and stir. Let it steep for 3-5 minutes before enjoying its exceptional flavor and aroma. No preservatives or artificial additives are included in this tea.',\
               'Beverages','dxn-reishi-gano-tea','360')")
  conn.commit()
  print("Records created successfully")
  conn.close()

def Show_Data(DATABASE):
  conn = sqlite3.connect(DATABASE)
  print("Opened database successfully")
  c = conn.cursor()
  c.execute("SELECT * FROM products")
#   c.execute("SELECT * FROM products WHERE id = 1")  
  # Modify the WHERE clause to specify the desired ID

  data = c.fetchall()
  for rowdata in data:
    print(f"{rowdata}\n")
  conn.close()


def update_data(DATABASE, name, email):
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("UPDATE users SET email = ? WHERE name = ?", (email, name))
  conn.commit()
  conn.close()


def delete_data(DATABASE, id):
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("DELETE FROM products WHERE id = ?", (id, ))
  conn.commit()
  conn.close()


# =============================================================================

# Show_Data(DATABASE)

# createDB(DATABASE)
# insertData(DATABASE)
# update_data(DATABASE, "Paul", "PaulABCmyabc@gmail.com")
# delete_data(DATABASE, "1")

Show_Data(DATABASE)


"""
(1, 
'DXN Reishi Gano Tea', 
'gano-tea.jpg', 
'DXN Reishi Gano Tea is blended with high quality Ganoderma powder. It has no added preservatives, artificial colouring and flavourings. DXN Reishi Gano Tea invigorates your mind and body and delights you with its exceptional flavour and pleasant aroma.', 
'provides refreshment, help to relieve stress, promotes energy & wellness, strengthens immune system, helps in detoxification, supports in maintaining balance of the body', 
'To prepare DXN Reishi Gano Tea, boil water, open a sachet of the tea, pour hot water over the tea powder, and stir. Let it steep for 3-5 minutes before enjoying its exceptional flavor and aroma. No preservatives or artificial additives are included in this tea.', 
'Beverage', 
450, 360, 135, 195)

(1, 
'DXN 2 in 1 Coffee', 
'gano-tea.jpg', 
'DXN Reishi Gano Tea is blended with high quality Ganoderma powder. It has no added preservatives, artificial colouring and flavourings. DXN Reishi Gano Tea invigorates your mind and body and delights you with its exceptional flavour and pleasant aroma.', 
'provides refreshment, help to relieve stress, promotes energy & wellness, strengthens immune system, helps in detoxification, supports in maintaining balance of the body', 
'To prepare DXN Reishi Gano Tea, boil water, open a sachet of the tea, pour hot water over the tea powder, and stir. Let it steep for 3-5 minutes before enjoying its exceptional flavor and aroma. No preservatives or artificial additives are included in this tea.', 
'Beverage', 
450, 360, 135, 195)

"""