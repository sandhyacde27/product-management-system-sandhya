# 🛒 Product Management System

This is a Python project that helps you manage products using a menu-based interface. You can add, update, delete, and list products, and store everything in a MySQL database.

---

## ✅ Features

- Add new products with unique IDs
- Update product details (name, price, category)
- Remove products
- List all products
- Generate product summary
- Group products by category
- Store data using MySQL
- Handle errors with custom exceptions

---

## 🛠️ Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- Spyder IDE (recommended)

---

## 🚀 How to Run

1. **Install MySQL connector**

- pip install mysql-connector-python


2. **Create MySQL database**
```sql
CREATE DATABASE product_db;
USE product_db;
CREATE TABLE products (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT,
    category VARCHAR(50)
);

3. **Update db_config.p**

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="product_db"
    )
    
 4.  Run the program Open main.py in Spyder and click Run.
 
 📁 Project Files
 
- main.py – Menu interface
- product.py – Product class
- product_manager.py – Handles product operations
- report.py – Reporting features
- exceptions.py – Custom error handling
- db_config.py – MySQL connection setup


👩‍💻 Created By Sandhya – Python developer and learner
