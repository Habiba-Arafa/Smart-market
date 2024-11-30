import sqlite3
import os

DATABASE_PATH = r"D:\year 3\semester 1\SWE\smart_market\Smart-market\instance\MainDB.db"


# Base database class
class database_base_model:
    def __init__(self, database_name=DATABASE_PATH):
        self.database_name = database_name
        self.establish_connection()

    def establish_connection(self):
        self.connection = sqlite3.connect(self.database_name, timeout=5000)
        print(f"Connected to database at: {self.database_name}")

    def cursor(self):
        return self.connection.cursor()

    def close(self):
        self.connection.close()

    def commit(self):
        try:
            print("Committing transaction...")
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error committing transaction: {e}")

    def fetch_all(self, table_name):
        try:
            data = self.cursor().execute(f"SELECT * FROM {table_name}")
            return data.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching all data from {table_name}: {e}")
            return []

    def l_tuple_to_list(self, tuple_list):
        flattened_list = []
        for tuple_item in tuple_list:
            for element in tuple_item:
                flattened_list.append(element)
        return flattened_list

    def execute_query(self, query, params=()):
        try:
            print(f"Executing query: {query} with params {params}")
            self.cursor().execute(query, params)
            self.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")


# Vendor class to manage vendor operations
class VendorDatabase(database_base_model):
    def __init__(self, database_name=DATABASE_PATH):
        super().__init__(database_name)

    def update_vendor_info(self, user_id, username=None, email=None):
        try:
            if username:
                print(f"Executing: UPDATE Users SET username = '{username}' WHERE user_id = {user_id}")
                self.cursor().execute("UPDATE Users SET username = ? WHERE user_id = ?", (str(username), str(user_id)))
            if email:
                print(f"Executing: UPDATE Users SET email = '{email}' WHERE user_id = {user_id}")
                self.cursor().execute("UPDATE Users SET email = ? WHERE user_id = ?", (str(email), str(user_id)))
            self.commit()
            print("Vendor info update committed.")
        except sqlite3.Error as e:
            print(f"Error updating vendor info: {e}")

    def get_vendor_info(self, user_id):
        try:
            result = self.cursor().execute(
                "SELECT user_id, username, email FROM Users WHERE user_id = ?", 
                (str(user_id),)
            )
            vendor = result.fetchone()
            if vendor:
                return {
                    "username": vendor[1],
                    "email": vendor[2],
                }
            return None
        except sqlite3.Error as e:
            print(f"Error fetching vendor info: {e}")
            return None
        
    def add_item(self, category_name, product_name, price, stock, vendor_id, description=None, image=None):
        try:
        # Get the CategoryID based on the category_name
         self.cursor().execute("SELECT CategoryID FROM Categories WHERE CategoryName = ?", (category_name,))
         category_id = self.cursor().fetchone()

         if not category_id:
            print(f"Category '{category_name}' does not exist.")
            return

         category_id = category_id[0] 

        # Get the ProductID based on the product_name
         self.cursor().execute("SELECT ProductID FROM Products WHERE ProductName = ?", (product_name,))
         product_id = self.cursor().fetchone()

         if not product_id:
            print(f"Product '{product_name}' does not exist.")
            return

         product_id = product_id[0] 

        # Insert the new item into the Items table with VendorID
         self.cursor().execute(
            '''INSERT INTO Items_new (CategoryID, ProductID, VendorID, Price, Stock, Description, Image)
               VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (category_id, product_id, vendor_id, price, stock, description, image)
        )
         self.commit()
         print(f"Item added successfully: {product_name} in category {category_name} by Vendor {vendor_id}")
    
        except sqlite3.Error as e:
         print(f"Error adding item: {e}")

        
    


# Customer class to manage customer operations
class CustomerDatabase(database_base_model):
    def __init__(self, database_name=DATABASE_PATH):
        super().__init__(database_name)

    def update_customer_info(self, user_id, username=None, email=None):
        try:
            if username:
                print(f"Executing: UPDATE Users SET username = '{username}' WHERE user_id = {user_id}")
                self.cursor().execute("UPDATE Users SET username = ? WHERE user_id = ?", (str(username), str(user_id)))
            if email:
                print(f"Executing: UPDATE Users SET email = '{email}' WHERE user_id = {user_id}")
                self.cursor().execute("UPDATE Users SET email = ? WHERE user_id = ?", (str(email), str(user_id)))
            self.commit()
            print("Customer info update committed.")
        except sqlite3.Error as e:
            print(f"Error updating customer info: {e}")

    def get_customer_info(self, user_id):
        try:
            result = self.cursor().execute(
                "SELECT user_id, username, email FROM Users WHERE user_id = ?", 
                (str(user_id),)
            )
            customer = result.fetchone()
            if customer:
                return {
                    "username": customer[1],
                    "email": customer[2],
                }
            return None
        except sqlite3.Error as e:
            print(f"Error fetching customer info: {e}")
            return None


# Test the functions for updating and retrieving user info
# def test_vendor_and_customer_info():
#     vendor_db = VendorDatabase()
#     customer_db = CustomerDatabase()

#     print("Updating vendor info...")
#     vendor_db.update_vendor_info(user_id=5, username="new_vendor_name_twice", email="new_vendor_email@example.com")
    
#     vendor_info = vendor_db.get_vendor_info(user_id=5)
#     print(f"Vendor Info (After Update): {vendor_info}")

#     print("\nUpdating customer info...")
#     customer_db.update_customer_info(user_id=3, username="new_customer_name_twice", email="new_customer_email@example.com")
    
#     customer_info = customer_db.get_customer_info(user_id=3)
#     print(f"Customer Info (After Update): {customer_info}")

    
#     category_name = "Children"
#     product_name = "Jeans"
#     price = 17.99
#     stock = 120
#     vendor_id = 5 
#     description = "Comfortable cotton t-shirt"
#     image = None  
#     vendor_db.add_item(category_name, product_name, price, stock, vendor_id, description, image)


# test_vendor_and_customer_info()




