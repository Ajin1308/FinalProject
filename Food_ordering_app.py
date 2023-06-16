import sys

class login:

    def __init__(self,login_as_admin_or_user):
        self.login_as_admin_or_user=login_as_admin_or_user
        
    def login_as(self):
        login_input=self.login_as_admin_or_user
        if login_input == 1:
            Admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
            Admin.add_food_item("Vegan Burger", "1 piece", 320, 10, 20)
            Admin.add_food_item("Truffle Cake", "500gm", 900, 5, 5)     

            Admin.view_food_items()

            Admin.edit_food_item(2, "BURGER KING", "2 pieces", 350, 0, 15)

            Admin.view_food_items()

            Admin.remove_food_item(1)

            Admin.view_food_items()

            Login=login(int(input("Enter 1 to Login for Admin\nEnter 2 Login as User:\n")))
            Login.login_as()
                

        elif login_input == 2:
            User.register("Edyoda", "1234567890", "edyoda@example.com", "123 Main St", "password")

            user = User.login("edyoda@example.com", "password")
            while user:
                user_command=int(input("1. Place New Order\n2. Order History\n3. Update Profile\n4. Exit\n"))
                if user_command == 1:
                    user.place_new_order()
                elif user_command == 2:    
                    user.view_order_history()
                elif user_command == 3:
                    user.update_profile()
                elif user_command == 4:
                    sys.exit()
            
            Login=login(int(input("Enter 1 to Login for Admin\nEnter 2 Login as User:\n")))
            Login.login_as()

        elif login_input == 3:
            Print("Thankyou!")

        else:
            print("Enter valid number!")
        

class FoodItem:
    food_id = 0

    def __init__(self, name, quantity, price, discount, stock):
        FoodItem.food_id += 1
        self.food_id = FoodItem.food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    food_items = []

    @staticmethod
    def add_food_item(name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        Admin.food_items.append(food_item)
        print("Food item added successfully!")

    @staticmethod
    def edit_food_item(food_id, name, quantity, price, discount, stock):
        for item in Admin.food_items:
            if item.food_id == food_id:
                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                print("Food item edited successfully!")
                return
        print("Food item not found!")

    @staticmethod
    def view_food_items():
        print("Food Items:")
        for item in Admin.food_items:
            print(f"FoodID: {item.food_id}")
            print(f"Name: {item.name}")
            print(f"Quantity: {item.quantity}")
            print(f"Price: {item.price}")
            print(f"Discount: {item.discount}")
            print(f"Stock: {item.stock}")
            print("------------------------")

    @staticmethod
    def remove_food_item(food_id):
        for item in Admin.food_items:
            if item.food_id == food_id:
                Admin.food_items.remove(item)
                print("Food item removed successfully!\n")
                return
        print("Food item not found!")


class User:
    registered_users = []

    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    @staticmethod
    def register(full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        User.registered_users.append(user)
        print("User registered successfully!\n")

    @staticmethod
    def login(email, password):
        for user in User.registered_users:
            if user.email == email and user.password == password:
                print("Login Success!\n")
                return user
        print("Invalid email or password!")
        return None

    def place_new_order(self):
            print("Available Food Items:")
            for item in Admin.food_items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")

            selected_items = input("Enter the item numbers you want to order (comma-separated): ")
            item_numbers = list(map(int, selected_items.split(",")))

            selected_food_items = []
            total_cost = 0

            for number in item_numbers:
                if 1 <= number <= len(Admin.food_items):
                    food_item = Admin.food_items[number - 1]
                    selected_food_items.append(food_item)
                    total_cost += food_item.price
                else:
                    print(f"Invalid item number: {number}")

            print("Selected Food Items:\n")
            for item in selected_food_items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")

            place_order = input("Do you want to place the order? (yes/no): ")
            if place_order.lower() == "yes":
                self.order_history.append(selected_food_items)
                print(f"Order placed successfully! Total cost: INR {total_cost}\n")
            else:
                print("Order cancelled!")
            

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No order history found!")
        else:
            print("Order History:")
            for index, order in enumerate(self.order_history):
                print(f"Order {index + 1}:")
                for item in order:
                    print(f"{item.name} ({item.quantity}) [INR {item.price}]")
                print("------------------------")

    def update_profile(self):
        print("Update Profile")
        self.full_name = input("Full Name: ")
        self.phone_number = input("Phone Number: ")
        self.email = input("Email: ")
        self.address = input("Address: ")
        self.password = input("Password: ")
        print("Profile updated successfully!")
    
            

Login=login(int(input("Enter 1 to Login for Admin\nEnter 2 Login as User:\n")))
Login.login_as()