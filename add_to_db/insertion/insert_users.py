import sqlite3

def insert_users(db_name, users_data):
   
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    insert_query = '''
        INSERT INTO Users (username, email, password_hash, role, status)
        VALUES (?, ?, ?, ?, ?)
    '''
    
    try:
        cursor.executemany(insert_query, users_data)
        connection.commit()
        print("Records added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    db_name = "instance/MainDB.db"

    users_data = [
        ("john_doe", "john@example.com", "hashed_password1", "Admin", None), 
        ("jane_smith", "jane@example.com", "hashed_password2", "Vendor", "Pending"), 
        ("alex_k", "alex@example.com", "hashed_password3", "Customer", None), 
        ("peter_p", "peter@example.com", "hashed_password5", "Customer", None), 
        ("tom_r", "tom@example.com", "hashed_password7", "Vendor", "Approved"), 
        ("sarah_b", "sarah@example.com", "hashed_password10", "Vendor", "Approved") 
    ]

    insert_users(db_name, users_data)
