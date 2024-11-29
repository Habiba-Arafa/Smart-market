# create_users_table.py

import sqlite3

def create_users_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    
    table = '''CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    role TEXT CHECK(role IN ('Admin', 'Vendor', 'Customer')) NOT NULL,
                    verification_certificate TEXT,
                    status TEXT CHECK(
                         (role = 'Vendor' AND status IN ('Approved', 'Pending')) OR 
                        (role != 'Vendor' AND status IS NULL)
    ) DEFAULT NULL
)'''
    


    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_users_table(db_name)
    print("Users table created successfully.")




