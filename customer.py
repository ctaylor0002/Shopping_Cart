#As a developer, I want the Customer class to have class instance variables to keep track of the Customer’s name and shopping cart object. (Set the shopping cart instance variable equal to a new ShoppingCart object in the initializer HINT: You will have to import the ShoppingCart class into the customer.py file)

#As a developer, I want the Customer class’s initializer to take in the initial value for the customer’s name via a parameter.

#As a developer, I want the Customer class to have a method to add a new product to the customer’s shopping cart (within this method you will call the shopping cart’s add product method)

#As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over the shopping cart’s products list and print each product to the terminal)

#As a developer, I want to import the Customer and Product classes into main.py so I can instantiate a customer object as well as three Product objects and interact with the object’s methods:


class Customer:
    
    def __init__(self, customer_name, shopping_cart):
        self.name = customer_name
        self.cart = shopping_cart
