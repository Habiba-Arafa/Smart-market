import sqlite3


#  Convert image file to binary data
def convert_to_binary(filename):

    with open(filename, "rb") as file:
        return file.read()

def insert_product_image(product_name, image_path, db_name):
   
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        query = '''INSERT INTO Products (product_name, photo) VALUES (?, ?)'''
        product_img = convert_to_binary(image_path) 
        cursor.execute(query, (product_name, product_img))
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert product image:", error)
    finally:
        if connection:
            connection.close()

def insert_category_image(category_name, image_path, db_name):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        query = '''INSERT INTO Categories (category_name, photo) VALUES (?, ?)'''
        category_img = convert_to_binary(image_path) 
        cursor.execute(query, (category_name, category_img))
        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert category image:", error)
    finally:
        if connection:
            connection.close()

