# create_notifications_table.py

import sqlite3

def create_notifications_table(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    table = '''CREATE TABLE IF NOT EXISTS Notifications (
                    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,             
                    message TEXT,               
                    type TEXT CHECK(type IN ('Order Update', 'Feedback', 'Promotion')) NOT NULL,  
                    read BOOLEAN DEFAULT 0,     
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
)
'''
    cursor.execute(table)
    connection.commit()
    connection.close()



if __name__ == "__main__":
    db_name = "instance/MainDB.db"
    create_notifications_table(db_name)
    print("Notifications table created successfully.")
