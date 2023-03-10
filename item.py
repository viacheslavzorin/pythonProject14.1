import csv

class Item:
    instances = []
    num_of_item = 0
    pay_rate = 0.85
    def __init__(self, product: str, quanity: int, price: int):
        self.__product = product
        self.quanity = quanity
        self.price = price
        self.instances.append(self)
        Item.num_of_item += 1
    def calculate_total_price(self):
        return self.quanity * self.price
    @property
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price
    @classmethod
    def instantiate_from_csv(cls):
        results = []
        with open('items.csv', encoding='windows - 1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                __product = row['name']
                price = cls.is_integer(int(row['price']))
                quanity = cls.is_integer(int(row['quantity']))
                results.append(cls(__product, quanity, price))
        return results
    @staticmethod
    def is_integer(number):
        if number % 1 == 0:
            return True
        else:
            return False
    @property
    def long_name(self):
        return self.__product
    @long_name.setter
    def long_name(self, name):
        try:
            if len(name) > 10:
                raise Exception('name must be less than 10')
        except Exception:
            print('Длина наименования товара превышает 10 символов')
        self.__product = name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__product}', '{self.quanity}', '{self.price},)"

#item1 = Item("Смартфон", 10000, 20)
#item1
    def __str__(self):
        return f'{self.__product}'

class Phone(Item):
        def __init__(self, product: str, quanity: int, price: int, number_of_sim ):
            super(). __init__(product, quanity, price)
            self.number_of_sim = number_of_sim

        @property
        def quantity_sim(self):
            return self.number_of_sim

        @quantity_sim.setter
        def quantity_sim(self, name):
            try:
                if self.number_of_sim > 0 or type(self.number_of_sim) is  int:
                    raise Exception('неправильный ввод')
            except Exception:
                print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
            self.number_of_sim = name
        def __add__(self, other):
            """Проверка возможности сложения"""
            if not isinstance(other. Item):
                raise ValueError('Складывать можно только объекты Item и дочерние от них.')
            return True

