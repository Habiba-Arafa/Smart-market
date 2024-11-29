import sqlite3

def add_records_to_users(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Sample records to insert into Users table
    users_data = [
        ("john_doe", "john@example.com", "hashed_password1", "Admin", "Approved"),
        ("jane_smith", "jane@example.com", "hashed_password2", "Vendor", "Pending"),
        ("alex_k", "alex@example.com", "hashed_password3", "Customer", "Approved"),
        ("peter_p", "peter@example.com", "hashed_password5", "Customer", "Pending"),
        ("linda_h", "linda@example.com", "hashed_password6", "Admin", "Approved"),
        ("tom_r", "tom@example.com", "hashed_password7", "Vendor", "Approved"),
        ("mark_z", "mark@example.com", "hashed_password9", "Admin", "Pending"),
        ("sarah_b", "sarah@example.com", "hashed_password10", "Vendor", "Approved")
    ]

    insert_query = '''
        INSERT INTO Users (username, email, password_hash, role, status)
        VALUES (?, ?, ?, ?, ?)
    '''
    cursor.executemany(insert_query, users_data)

    connection.commit()
    connection.close()
    print("Records added successfully.")

if __name__ == "__main__":
    db_name = "instance/MainDB.db" 
    add_records_to_users(db_name)
