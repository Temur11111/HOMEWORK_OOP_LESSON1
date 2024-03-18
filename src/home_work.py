class Category:
    name: str
    descriptions: str
    products: list

    def __init__(self, name, descriptions, products):
        self.name = name
        self.descriptions = descriptions
        self.products = products




class Product:
    name: str
    descriptions: str
    price: float
    quantity_in_stock: int ###количество в наличии
    counter_categories: int

    counter_categories = 0
    original_product = 0

    def __init__(self, name, descriptions, price, quantity_in_stock):
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_in_stock = quantity_in_stock


