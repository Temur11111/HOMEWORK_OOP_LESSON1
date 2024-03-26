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
        self.__products = products
        Category.counter_categories += 1
        if len(products) == len(set(products)):
            Category.original_product = len(products)
        else:
            Category.original_product = len(set(products))


    def append_products(self,product):
        return self.__products.append(product)

    @property
    def return_pruducts(self):
        """Возвращает список товаров в форме: Продукт, 80 руб. Остаток: 15 шт.. К атрибуту можно обращаться без ()."""
        result = ""
        for product in self.__products:
            result+=f'{Product.name}, {Product.price} руб. Остаток {Product.quantity_in_stock} шт.'
            return result


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




