import sqlite3

def insert_categories(db_name):
    # Connect to the database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Insert category data
    categories = [
        ("Women",),
        ("Men",),
        ("Children",)
    ]
    cursor.executemany("INSERT INTO Categories (CategoryName) VALUES (?)", categories)

    # Commit and close connection
    connection.commit()
    connection.close()

# Insert categories into the database
db_name = "instance/MainDB.db"
insert_categories(db_name)
print("Categories inserted successfully.")
