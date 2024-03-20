class Category:
    """Класс категории"""
    counter_categories: int
    original_product: int

    counter_categories = 0####количество категории
    original_product = 0###количество оригинальных продуктов



    def __init__(self, name, descriptions, products):
        name: str
        descriptions: str
        products: list
        self.name = name
        self.descriptions = descriptions
        self.products = products
        Category.counter_categories += 1
        if len(products) == len(set(products)):
            Category.original_product = len(products)
        else:
            Category.original_product = len(set(products))




class Product:
    """Класс продуктов"""
    name: str
    descriptions: str
    price: float
    quantity_in_stock: int ###количество в наличии


    def __init__(self, name, descriptions, price, quantity_in_stock):
        name: str
        descriptions: str
        price: float
        quantity_in_stock: int  ###количество в наличии
        self.name = name
        self.descriptions = descriptions
        self.price = price
        self.quantity_in_stock = quantity_in_stock




