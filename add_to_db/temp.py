import sqlite3

def drop_and_create_categories(db_name):
    print(f"Connecting to database: {db_name}")
    try:
        # Connect to the database
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        # Drop Categories table if it exists
        print("Dropping Categories table if it exists...")
        cursor.execute("DROP TABLE IF EXISTS Categories")

        # Create the Categories table with a unique constraint
        print("Creating Categories table with UNIQUE constraint...")
        cursor.execute("""
            CREATE TABLE Categories (
                CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                CategoryName TEXT UNIQUE
            )
        """)

        # Commit and close connection
        connection.commit()
        connection.close()

        print("Categories table recreated with UNIQUE constraint.")
    
    except sqlite3.Error as e:
        print(f"Error with SQLite operation: {e}")
    except Exception as e:
        print(f"General error: {e}")

# Call the function to drop and create Categories
db_name = "instance/MainDB.db"
drop_and_create_categories(db_name)
