import sqlite3

def create_products_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vendor_id INTEGER,
                    category_id INTEGER,
                    product_name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    discount REAL DEFAULT 0,
                    photo BLOB, 
                    stock INTEGER DEFAULT 0,
                    product_colour TEXT,
                    FOREIGN KEY (vendor_id) REFERENCES Users(user_id)
                )'''
    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_products_table(db_name)
    print("Products table created successfully.")
