import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self._price = float(price)
        self._quantity = int(quantity)
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {int(self._price)}, {self._quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item) or issubclass(other.__class__, Item):
            return self._quantity + other._quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self._price * self._quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self._price *= Item.pay_rate

    @property
    def name(self) -> str:
        """
        Getter для имени товара в магазине.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Setter для имени товара в магазине.
        """
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    @classmethod
    def instantiate_from_csv(cls):

        try:
            with open('../src/items.csv', 'r', encoding='utf-8') as f:
                csv_dict = csv.DictReader(f)
                for row in csv_dict:
                    Item(row["name"], cls.string_to_number(row['price']), int(row['quantity']))
        except FileNotFoundError:
            print("Файл items.csv не найден")

    @staticmethod
    def string_to_number(string: str) -> float:
        return int(float(string))

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity