import sqlite3

def create_orders_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Orders (
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    total_amount REAL NOT NULL,
                    status TEXT CHECK(status IN ('Pending', 'Shipped', 'Delivered')) NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES Users(user_id)
                )'''
    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_orders_table(db_name)
    print("Orders table created successfully.")