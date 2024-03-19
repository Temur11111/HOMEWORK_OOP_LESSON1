class Category:
    name: str
    descriptions: str
    products: list
    counter_categories: int
    original_product: int


    counter_categories = 0####количество категории
    original_product = 0#####количество оригинальных продуктов


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



    def __init__(self, name, descriptions, price, quantity_in_stock):
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_in_stock = quantity_in_stock




