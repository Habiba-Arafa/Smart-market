import sqlite3

def create_shipping_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Shipping (
                    shipping_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vendor_id INTEGER,
                    order_id INTEGER,
                    status TEXT NOT NULL,
                    tracking_number TEXT,
                    FOREIGN KEY (vendor_id) REFERENCES Users(user_id),
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
                )'''
    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_shipping_table(db_name)
    print("Shipping table created successfully.")
