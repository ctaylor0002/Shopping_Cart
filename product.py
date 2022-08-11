#As a developer, I want the Product class to have class properties to keep track of the Product’s name, price, and category.

#As a developer, I want the Product class’s initializer to take in the initial values for the name, price, and category via parameters


class Product:
    
    def __init__(self, product_name, product_price, category):
        self.product = product_name
        self.price = product_price
        self.category = category