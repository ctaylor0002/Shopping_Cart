#As a developer, I want to use Python’s proper snake_case for variable names.

#As a developer, I want to create a Customer, ShoppingCart, and Product class.

#As a developer, I want the Product class to have class properties to keep track of the Product’s name, price, and category.

#As a developer, I want the Product class’s initializer to take in the initial values for the name, price, and category via parameters

#As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list).

#As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.

#As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)

#As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.

#As a developer, I want the Customer class to have class instance variables to keep track of the Customer’s name and shopping cart object. (Set the shopping cart instance variable equal to a new ShoppingCart object in the initializer HINT: You will have to import the ShoppingCart class into the customer.py file)

#As a developer, I want the Customer class’s initializer to take in the initial value for the customer’s name via a parameter.

#As a developer, I want the Customer class to have a method to add a new product to the customer’s shopping cart (within this method you will call the shopping cart’s add product method)

#As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over the shopping cart’s products list and print each product to the terminal)

#As a developer, I want to import the Customer and Product classes into main.py so I can instantiate a customer object as well as three Product objects and interact with the object’s methods:

#1. Print the customer’s name to the terminal

#2. Call the customer’s add product to shopping cart method three times and add the three products objects you created

#3. Call the customer’s view products method

#4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal

#5. Call the customer’s shopping cart’s empty cart method

#6. Check if all products have been removed from the shopping cart

from shopping_cart import ShoppingCart
from product import Product
from customer import Customer

#We will not instantiate the shopping cart object until a product is being added to avoid confusion
first_item = Product('Apples', 2.50, 'Fruit')
shopping_cart = ShoppingCart(first_item)


products_to_count = shopping_cart.products
value_of_cart = shopping_cart.calculate_price(products_to_count)
print(f"The amount you will have to pay at check out is, ${value_of_cart:.2f}")

#Add items to the cart
second_item = Product('Squash', 3.00, 'Vegatable')
shopping_cart.add_item_to_cart(second_item)

#Empty items in the cart
shopping_cart.empty_shopping_cart()
products_to_count = shopping_cart.products
value_of_cart = shopping_cart.calculate_price(products_to_count)
print('All items have been removed!')

#Create a customer and add the shopping cart to them
customer_name = 'Robin'
customer = Customer(customer_name, shopping_cart)

