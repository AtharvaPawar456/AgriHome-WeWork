import sqlite3

DATABASE = 'data.db'

def show_all_tables(database):
    conn = sqlite3.connect(database)
    # print("Opened database successfully")
    c = conn.cursor()

    # Query the sqlite_master table to retrieve table names
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
  
    for table in tables:
        print(table[0])
  
    conn.close()

def remove_table(database, table_name):
    conn = sqlite3.connect(database)
    # print("Opened database successfully")
    c = conn.cursor()

    # Drop the table
    c.execute(f"DROP TABLE IF EXISTS {table_name};")
  
    print("Table removed successfully")

    conn.commit()
    conn.close()

# remove_table(DATABASE, 'category_item')
# remove_table(DATABASE, 'products')

show_all_tables(DATABASE)
