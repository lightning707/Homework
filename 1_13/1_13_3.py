class Product:
    def __init__(self, type_, name, price):
        self.type_ = type_
        self.name = name
        self.price = price
        self.amount = 0

    def __repr__(self):
        return f"> Type: {self.type_}, name: {self.name}, price:{self.price}, amount:{self.amount} <"


class ProductStore:
    def __init__(self):
        self.product_list = []
        self.price_premium = 30
        self.income = 0

    def add(self, product, amount):
        if not isinstance(amount, int):
            raise ValueError("Cannot add a non-integer amount of products")
        elif amount <= 0:
            raise ValueError("Cannot add a non-positive amount of products")
        else:
            product.price *= 1 + (self.price_premium / 100)
            product.amount += amount
            self.product_list.append(product)

    def set_discount(self, identifier, percent, identifier_type="name"):
        if identifier_type.lower() == "name":
            for product in self.product_list:
                if product.name == identifier:
                    product.price -= product.price * (percent / 100)
        elif identifier_type.lower() == "type":
            for product in self.product_list:
                if product.type_ == identifier:
                    product.price -= product.price * (percent / 100)
        else:
            raise ValueError("Unknown identifier type")

    def sell_product(self, product_name, amount):
        for product in self.product_list:
            if product.name == product_name:
                if product.amount >= amount:
                    product.amount -= amount
                    self.income += amount * product.price
                else:
                    raise ValueError("Not enough products in stock")
        result_prod_list = [product for product in self.product_list if product.amount != 0]
        self.product_list = result_prod_list

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.product_list

    def get_product_info(self, product_name):
        for product in self.product_list:
            if product.name == product_name:
                return product.name, product.amount


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product("Food", 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
print(s.get_all_products())
