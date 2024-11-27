import sqlite3

def create_categories_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Categories (
                    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category_name TEXT NOT NULL,
                    photo BLOB,
                    description TEXT
                )'''
    cursor.execute(table)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_categories_table(db_name)
    print("Categories table created successfully.")
