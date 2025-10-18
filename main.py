from product import Product
from product_manager import ProductManager
from report import Report
from exceptions import DuplicateProductIDError, ProductNotFoundError

def main():
    manager = ProductManager()
    report = Report()

    while True:
        print("\n--- Product Management System ---")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. List Products")
        print("5. Generate Report")
        print("6. Report by Category")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                pid = input("Product ID: ")
                name = input("Name: ")
                price = float(input("Price: "))
                category = input("Category: ")
                manager.add_product(Product(pid, name, price, category))
                print("✅ Product added successfully.")

            elif choice == '2':
                pid = input("Product ID to update: ")
                name = input("New Name (leave blank to skip): ")
                price = input("New Price (leave blank to skip): ")
                category = input("New Category (leave blank to skip): ")
                kwargs = {}
                if name: kwargs['name'] = name
                if price: kwargs['price'] = float(price)
                if category: kwargs['category'] = category
                manager.update_product(pid, **kwargs)
                print("✅ Product updated successfully.")

            elif choice == '3':
                pid = input("Product ID to remove: ")
                manager.remove_product(pid)
                print("🗑️ Product removed successfully.")

            elif choice == '4':
                report.generate_report(manager)

            elif choice == '5':
                report.generate_report(manager)

            elif choice == '6':
                report.report_by_category(manager)

            elif choice == '7':
                print("👋 Exiting Product Management System.")
                break

            else:
                print("⚠️ Invalid choice. Please try again.")

        except (DuplicateProductIDError, ProductNotFoundError, ValueError) as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()