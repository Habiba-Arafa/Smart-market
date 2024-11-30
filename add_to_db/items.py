import sqlite3

def create_tables(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()


    cursor.execute("DROP TABLE IF EXISTS Items")


    

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Items_new (
        ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryID INTEGER,
        ProductID INTEGER,
        VendorID INTEGER,  
        Price REAL NOT NULL,
        Stock INTEGER NOT NULL,
        Description TEXT,
        Image BLOB,
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
        FOREIGN KEY (VendorID) REFERENCES Users(user_id) 
    )''')

    connection.commit()
    connection.close()

db_name = "instance/MainDB.db"
create_tables(db_name)
print("Tables created successfully.")
