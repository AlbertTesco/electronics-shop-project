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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self) -> str:
        """
        Getter для имени товара в магазине.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Setter для имени товара в магазине.
        """
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

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
