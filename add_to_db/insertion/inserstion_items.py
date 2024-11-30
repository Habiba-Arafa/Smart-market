

import sqlite3

def insert_items(db_name):
    # Connect to the database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Vendor IDs (as mentioned, only 5 and 6)
    vendor_ids = [5, 6]

    # Insert item data (use actual CategoryIDs and ProductIDs, VendorID added)
    items = [
        (1, 1, vendor_ids[0], 15.99, 100, "Women's T-shirt", None),  # Vendor 5
        (1, 2, vendor_ids[1], 39.99, 150, "Women's Jeans", None),  # Vendor 6
        (1, 3, vendor_ids[0], 29.99, 200, "Women's Shoes", None),  # Vendor 5
        (2, 1, vendor_ids[1], 17.99, 120, "Men's T-shirt", None),  # Vendor 6
        (2, 2, vendor_ids[0], 45.99, 100, "Men's Jeans", None),  # Vendor 5
        (2, 3, vendor_ids[1], 35.99, 250, "Men's Shoes", None),  # Vendor 6
        (3, 1, vendor_ids[0], 10.99, 300, "Children's T-shirt", None),  # Vendor 5
        (3, 2, vendor_ids[1], 25.99, 180, "Children's Jeans", None),  # Vendor 6
        (3, 3, vendor_ids[0], 18.99, 400, "Children's Shoes", None)  # Vendor 5
    ]

    # Insert items into the table, including the VendorID
    cursor.executemany("INSERT INTO Items_new (CategoryID, ProductID, VendorID, Price, Stock, Description, Image) VALUES (?, ?, ?, ?, ?, ?, ?)", items)

    # Commit and close connection
    connection.commit()
    connection.close()

# Insert items into the database
db_name = "instance/MainDB.db"
insert_items(db_name)
print("Items inserted successfully.")
