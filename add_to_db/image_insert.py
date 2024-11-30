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
image_path_1 = "clothes/women/T-shirts/T-shirts_women_1.jpg" 
image_path_2 = "clothes/women/Jeans/Jeans_women_1.jpg" 
image_path_3= "clothes/women/Shoes/Shoes_women_1.jpg" 
image_path_4= "clothes/men/T-shirts/T-shirts_men_1.jpg" 
image_path_5= "clothes/men/Jeans/Jeans_men_1.jpg" 
image_path_6= "clothes/men/Shoes/Shoes_men_1.jpg" 
image_path_7= "clothes/children/T-shirts_/T-shirts_children_1.jpg" 
image_path_8= "clothes/children/Jeans/Jeans_children_1.jpg" 
image_path_9= "clothes/children/Shoes/Shoes_children_1.jpg" 

insert_image(db_name, image_path,1)
insert_image(db_name, image_path,2)
insert_image(db_name, image_path,3)
insert_image(db_name, image_path,4)
insert_image(db_name, image_path,5)
insert_image(db_name, image_path,6)
insert_image(db_name, image_path,7)
insert_image(db_name, image_path,9)

