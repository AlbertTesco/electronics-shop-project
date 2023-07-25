import pytest
from src.item import Item

instance = Item("Смартфон", 10000, 20)


# Test module
def test_item():
    assert instance.name == "Смартфон"
    assert instance.price == 10000
    assert instance.quantity == 20


def test_calculate_total_price():
    assert instance.calculate_total_price() == 200000


def test_apply_discount():
    instance.apply_discount()
    Item.pay_rate = 2
    instance.price = 20000
