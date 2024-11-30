import sqlite3

def insert_items(db_name):
    # Connect to the database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Insert item data (use actual CategoryIDs and ProductIDs)
    items = [
        (1, 1, 15.99, 100, "Women's T-shirt", None),  # No image for now
        (1, 2, 39.99, 150, "Women's Jeans", None),
        (1, 3, 29.99, 200, "Women's Shoes", None),
        (2, 1, 17.99, 120, "Men's T-shirt", None),
        (2, 2, 45.99, 100, "Men's Jeans", None),
        (2, 3, 35.99, 250, "Men's Shoes", None),
        (3, 1, 10.99, 300, "Children's T-shirt", None),
        (3, 2, 25.99, 180, "Children's Jeans", None),
        (3, 3, 18.99, 400, "Children's Shoes", None)
    ]
    cursor.executemany("INSERT INTO Items (CategoryID, ProductID, Price, Stock, Description, Image) VALUES (?, ?, ?, ?, ?, ?)", items)

    # Commit and close connection
    connection.commit()
    connection.close()

# Insert items into the database
db_name = "instance/MainDB.db"
insert_items(db_name)
print("Items inserted successfully.")
