import sqlite3

def create_tables(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Categories (
                        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                        CategoryName TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                        ProductName TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Items (
                        ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
                        CategoryID INTEGER,
                        ProductID INTEGER,
                        Price REAL NOT NULL,
                        Stock INTEGER NOT NULL,
                        Description TEXT,
                        Image BLOB,  
                        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
                        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
                    )''')

    connection.commit()
    connection.close()

db_name = "instance/MainDB.db"
create_tables(db_name)
print("Tables created successfully.")
