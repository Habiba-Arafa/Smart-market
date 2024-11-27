import sqlite3

def create_payment_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Payments (
                    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER,
                    amount REAL NOT NULL,
                    status TEXT NOT NULL,
                    transaction_date TEXT NOT NULL,
                    transaction_id TEXT UNIQUE NOT NULL,
                    payment_method TEXT NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
                )'''
    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_payment_table(db_name)
    print("Payments table created successfully.")
