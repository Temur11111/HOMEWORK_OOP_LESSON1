from home_work import Category, Product


class Smartphone(Product):
    def __init__(self, name, descriptions, price, quantity_in_stock , capacity, model, memory, color):
        capacity: int ##производительность
        model: str ##модель
        memory: int ##обьем памяти
        color: str ##цвет
        super().__init__(name, descriptions, price, quantity_in_stock)
        self.capacity = capacity
        self.model = model
        self.memory = memory
        self.color = color




class Lawn_Graas(Product):
    def __init__(self, name, descriptions, price, quantity_in_stock , country, germination_period, color):
        country: str ##страна производитель
        germination_period: int ##срок прорастания
        color: str ##цвет
        super().__init__(name, descriptions, price, quantity_in_stock)
        self.counry = country
        self.germination_period = germination_period
        self.color = color



