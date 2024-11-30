import sqlite3

def insert_products(db_name):
    # Connect to the database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Insert product data
    products = [
        ("T-shirt",),
        ("Jeans",),
        ("Shoes",)
    ]
    cursor.executemany("INSERT INTO Products (ProductName) VALUES (?)", products)

    # Commit and close connection
    connection.commit()
    connection.close()

# Insert products into the database
db_name = "instance/MainDB.db"
insert_products(db_name)
print("Products inserted successfully.")
