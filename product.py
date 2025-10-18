"""
Product Class
-------------
product.py
Represents a product in the system.
"""

class Product:
    def __init__(self, product_id, name, price, category):
        # save values into instance variables
        self.id = product_id
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, new_price):
        # check that price is not negative
        if new_price < 0:
            print("Price cannot be negative!")
            return
        self.price = new_price

    def update_name(self, new_name):
        # update the product name
        self.name = new_name

    def __str__(self):
        # format how product looks when printed
        return f"ID: {self.id} | Name: {self.name} | Category: {self.category} | Price: {self.price}"

