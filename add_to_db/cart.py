
import sqlite3

def create_cart_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Cart (
                    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES Users(user_id),
                    FOREIGN KEY (product_id) REFERENCES Products(product_id)
                )'''
    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_cart_table(db_name)
    print("Cart table created successfully.")
