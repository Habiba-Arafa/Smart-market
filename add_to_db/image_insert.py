import sqlite3

def insert_image(db_name, image_path, item_id):
    try:
        # Open the image and convert it into binary data
        with open(image_path, 'rb') as file:
            img_data = file.read()

        # Connect to the database
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        # Update the item with the image binary data
        cursor.execute("UPDATE Items SET Image = ? WHERE ItemID = ?", (img_data, item_id))

        # Commit and close connection
        connection.commit()
        connection.close()
        print("Image inserted successfully.")
    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example: Insert an image for item with ID 1
db_name = "instance/MainDB.db"
image_path = "clothes/children/Jeans/Jeans_children_1.jpg"  # Adjust this path if necessary
insert_image(db_name, image_path,8)
