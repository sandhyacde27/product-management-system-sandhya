"""
Category Class
--------------
category.py
Represents a category for products.
"""

class Category:
    def __init__(self, category_id, name):
        # Store category ID and name
        self.category_id = category_id
        self.name = name

    def __str__(self):
        """
        Return category details as string.
        Example: "Category ID: 1 | Name: Electronics"
        """
        return f"Category ID: {self.category_id} | Name: {self.name}"

c1 = Category(1, "Electronics")
print(c1)
