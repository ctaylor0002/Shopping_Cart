#As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list).

#As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.

#As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)

#As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.

#from product import Product





class ShoppingCart:

    def __init__(self, product):
        self.products = [product]
    
    def calculate_price(self, products_to_count):
        total_price = 0
        print(len(products_to_count))
        for item in products_to_count:
            price_to_add = item.price
            total_price = total_price + price_to_add
        return(total_price)

    def add_item_to_cart(self, item):
        self.products.append(item)
        print(self.products)