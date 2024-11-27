
import sqlite3

def create_order_details_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Order_Details (
                    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    discount REAL DEFAULT 0,
                    total_price REAL NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                    FOREIGN KEY (product_id) REFERENCES Products(product_id)
                )'''
    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_order_details_table(db_name)
    print("Order Details table created successfully.")
