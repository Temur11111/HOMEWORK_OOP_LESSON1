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

    def __len__(self):
        return len(self.__products)

    def append_products(self,product):
        return self.__products.append(product)

    @property
    def return_products(self):
        """Возвращает список товаров в форме: Продукт, 80 руб. Остаток: 15 шт. К атрибуту можно обращаться без ()."""
        result = ""
        for product in self.__products:
            result+=f'{product.name}, {product.price} руб. Остаток {product.quantity_in_stock} шт.'
        return result


    def __str__(self):
        return f"Название категории: {self.name}, количество продуктов: {len(self)}"

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
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    def __add__(self, other):
        return float(self.__price) * int(self.quantity_in_stock) + float(other.__price) * int(other.quantity_in_stock)

    def __str__(self):
        return f"Продукт: {self.name}, Цена: {self.price}, остаток: {self.quantity_in_stock} шт."




    @classmethod
    def product_init(cls,product_atribut):
        ###Создаем товар
        name, descriptions, price, quantity_in_stock = product_atribut.split(" ")
        return cls(name, descriptions, price, quantity_in_stock)


    @property
    def price(self):
        return f"{self.__price}"

    @price.setter
    def price_change(self,new_price):
        if new_price <= 0:
            print("Некорректная цена")
        else:
            self.__price = new_price




product1 = Product.product_init("Айфон хороший 10 50")

product2 = Product.product_init("Самсунг отличный 10 12")


category1 = Category("Телефоны", "Смартфоны", ["fe","effe","f",'EFF',"f"])

