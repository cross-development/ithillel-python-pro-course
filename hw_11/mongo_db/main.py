"""
Main script for online store management.
"""

from datetime import datetime
from bson import ObjectId

from hw_11.mongo_db.services.order_service import OrderService
from hw_11.mongo_db.services.product_service import ProductService
from hw_11.mongo_db.services.statistics_service import StatisticsService


def main() -> None:
    """
    Run the online store management system.
    """

    order_service = OrderService()
    product_service = ProductService()
    statistics_service = StatisticsService()

    while True:
        print("\n1. Add product")
        print("2. View recent orders")
        print("3. Create new order")
        print("4. Get total products sold")
        print("5. Get total amount of all customer orders")
        print("6. Exit\n")

        try:
            choice = input("Choose an option: ")
        except KeyboardInterrupt:
            print("\nExiting program...")
            break

        if choice == "1":
            name = input("Product name: ")
            price = float(input("Price: "))
            category = input("Category: ")
            stock = int(input("Stock: "))

            if stock < 0:
                print("Invalid input. Stock cannot be negative.")
                continue

            product_service.add_product(name, price, category, stock)
            print("Product added!")

        elif choice == "2":
            orders = order_service.get_recent_orders()

            if orders:
                for order in orders:
                    print(order)
            else:
                print("No orders found")

        elif choice == "3":
            order_number = input("Order number: ")
            customer = input("Customer name: ")
            items = []

            while True:
                product_id = input("Product ID: ")

                try:
                    product_id = ObjectId(product_id)
                except ValueError:
                    print("Invalid product ID")
                    continue

                quantity = int(input("Quantity: "))
                items.append({"product_id": product_id, "quantity": quantity})

                more = input("Add another item? (y/n): ")

                if more.lower() != "y":
                    break

            try:
                order_service.create_order(order_number, customer, items)
                print("Order created successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")

            total_sold = statistics_service.total_products_sold(start, end)
            print(f"Total products sold: {total_sold}")

        elif choice == "5":
            customer = input("Customer: ")

            total_amount = statistics_service.total_spent_by_customer(customer)
            print(f"Total amount: {total_amount}")

        elif choice == "6":
            print("\nExiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
