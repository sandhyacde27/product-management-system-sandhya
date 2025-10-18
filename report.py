class Report:
    def generate_report(self, product_manager):
        """
        Print details of all products.
        """
        products = product_manager.list_products()
        print("\n=== Product Summary ===")
        for product in products:
            print(product)

    def report_by_category(self, product_manager):
        """
        Group products by category.
        """
        products = product_manager.list_products()
        category_map = {}

        for product in products:
            category_map.setdefault(product.category, []).append(product)

        print("\n=== Products by Category ===")
        for category, items in category_map.items():
            print(f"\nCategory: {category}")
            for item in items:
                print(f"  {item}")

