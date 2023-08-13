from src.item import Item


class MixinKeyboard:
    def __init__(self):
        self._language = "EN"

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"
        return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self) -> str:
        return self.name
