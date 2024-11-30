import sqlite3

# def insert_categories(db_name):
#     # Connect to the database
#     connection = sqlite3.connect(db_name)
#     cursor = connection.cursor()

#     # Insert category data
#     categories = [
#         ("Women",),
#         ("Men",),
#         ("Children",)
#     ]
#     cursor.executemany("INSERT INTO Categories (CategoryName) VALUES (?)", categories)

#     # Commit and close connection
#     connection.commit()
#     connection.close()

# # Insert categories into the database
# db_name = "instance/MainDB.db"
# insert_categories(db_name)
# print("Categories inserted successfully.")



# def insert_categories(db_name):
#     # Connect to the database
#     connection = sqlite3.connect(db_name)
#     cursor = connection.cursor()

#     # Insert category data if not already existing
#     categories = [
#         ("Women",),
#         ("Men",),
#         ("Children",)
#     ]
    
#     # Insert categories that don't exist yet
#     for category in categories:
#         cursor.execute("INSERT OR IGNORE INTO Categories (CategoryName) VALUES (?)", category)

#     # Commit and close connection
#     connection.commit()

#     # Verify the insertion
#     cursor.execute("SELECT * FROM Categories")
#     print("Categories in the database:")
#     for row in cursor.fetchall():
#         print(row)

#     connection.close()

# # Insert categories into the database
# db_name = "instance/MainDB.db"
# insert_categories(db_name)
# print("Categories inserted successfully.")





import sqlite3

def insert_data(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Insert categories (Women, Men, Children)
    cursor.executemany('''
        INSERT OR IGNORE INTO Categories (CategoryName) VALUES (?)
    ''', [('Women',), ('Men',), ('Children',)])

    # Insert products for each category (Shirts, Trousers, Shoes)
    cursor.executemany('''
        INSERT OR IGNORE INTO Products (ProductName, CategoryID) 
        VALUES (?, (SELECT CategoryID FROM Categories WHERE CategoryName = ?))
    ''', [
        ('Shirts', 'Women'),
        ('Trousers', 'Women'),
        ('Shoes', 'Women'),
        ('Shirts', 'Men'),
        ('Trousers', 'Men'),
        ('Shoes', 'Men'),
        ('Shirts', 'Children'),
        ('Trousers', 'Children'),
        ('Shoes', 'Children')
    ])

    # Insert items for each product (3 items for each category)
    cursor.executemany('''
        INSERT OR IGNORE INTO Items (ProductID, Price, Stock, Description)
        VALUES ((SELECT ProductID FROM Products WHERE ProductName = ?), ?, ?, ?)
    ''', [
        # Items for Women
        ('Shirts', 19.99, 100, 'A stylish red shirt'),
        ('Shirts', 24.99, 150, 'A trendy blue shirt'),
        ('Shirts', 29.99, 200, 'A classic white shirt'),
        ('Trousers', 29.99, 50, 'Blue denim jeans'),
        ('Trousers', 39.99, 80, 'Black formal trousers'),
        ('Trousers', 34.99, 120, 'Grey casual trousers'),
        ('Shoes', 49.99, 75, 'Comfortable white sneakers'),
        ('Shoes', 59.99, 60, 'Stylish black boots'),
        ('Shoes', 69.99, 90, 'Sporty running shoes'),

        # Items for Men
        ('Shirts', 19.99, 100, 'A casual plaid shirt'),
        ('Shirts', 24.99, 120, 'A formal dress shirt'),
        ('Shirts', 29.99, 150, 'A graphic t-shirt'),
        ('Trousers', 35.99, 70, 'Slim fit blue jeans'),
        ('Trousers', 40.99, 100, 'Chinos for a sharp look'),
        ('Trousers', 45.99, 80, 'Relaxed fit khaki trousers'),
        ('Shoes', 59.99, 50, 'Leather dress shoes'),
        ('Shoes', 49.99, 70, 'Casual loafers'),
        ('Shoes', 79.99, 90, 'Sporty sneakers'),

        # Items for Children
        ('Shirts', 9.99, 150, 'Cute cartoon t-shirt'),
        ('Shirts', 12.99, 100, 'Animal print shirt'),
        ('Shirts', 14.99, 120, 'Striped t-shirt for kids'),
        ('Trousers', 15.99, 80, 'Comfortable kids jeans'),
        ('Trousers', 18.99, 90, 'Stretchable kids trousers'),
        ('Trousers', 20.99, 110, 'Cargo pants for children'),
        ('Shoes', 19.99, 150, 'Colorful kids sneakers'),
        ('Shoes', 22.99, 120, 'Slip-on shoes for toddlers'),
        ('Shoes', 25.99, 100, 'Comfortable sandals for children')
    ])

    connection.commit()
    connection.close()

# Insert sample data
db_name = "instance/MainDB.db"
insert_data(db_name)
print("Data inserted successfully.")
