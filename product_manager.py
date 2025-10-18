from db_config import get_connection
from exceptions import DuplicateProductIDError, ProductNotFoundError

class ProductManager:
    def add_product(self, product):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM products WHERE id = %s", (product.id,))
        if cursor.fetchone():
            raise DuplicateProductIDError(f"Product ID {product.id} already exists.")
        cursor.execute("INSERT INTO products (id, name, price, category) VALUES (%s, %s, %s, %s)",
                       (product.id, product.name, product.price, product.category))
        conn.commit()
        conn.close()

    def update_product(self, product_id, **kwargs):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM products WHERE id = %s", (product_id,))
        if not cursor.fetchone():
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        if 'name' in kwargs:
            cursor.execute("UPDATE products SET name = %s WHERE id = %s", (kwargs['name'], product_id))
        if 'price' in kwargs:
            cursor.execute("UPDATE products SET price = %s WHERE id = %s", (kwargs['price'], product_id))
        if 'category' in kwargs:
            cursor.execute("UPDATE products SET category = %s WHERE id = %s", (kwargs['category'], product_id))
        conn.commit()
        conn.close()

    def remove_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM products WHERE id = %s", (product_id,))
        if not cursor.fetchone():
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()
        conn.close()

    def list_products(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category FROM products")
        rows = cursor.fetchall()
        conn.close()
        return [Product(*row) for row in rows]



