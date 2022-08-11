#As a developer, I want the Customer class to have class instance variables to keep track of the Customer’s name and shopping cart object. (Set the shopping cart instance variable equal to a new ShoppingCart object in the initializer HINT: You will have to import the ShoppingCart class into the customer.py file)

#As a developer, I want the Customer class’s initializer to take in the initial value for the customer’s name via a parameter.

#As a developer, I want the Customer class to have a method to add a new product to the customer’s shopping cart (within this method you will call the shopping cart’s add product method)

#As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over the shopping cart’s products list and print each product to the terminal)

class Customer:
    
    def __init__(self, customer_name, shopping_cart):
        self.name = customer_name
        self.cart = shopping_cart

    def add_product(self, new_item):
        self.cart.add_item_to_cart(new_item)
    
    def view_items_in_cart(self):
        list = self.cart.products
        if list == []:
            print("Your cart is empty!")
        else:
            for item in list:
                print(item.product)