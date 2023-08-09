import pytest

from src.item import Item
from src.phone import Phone


# Fixtures for testing Item class

@pytest.fixture(scope="session")
def data_for_test_item():
    instance = Item("Смартфон", 10000, 20)
    return [instance.name, instance.price, instance.quantity], ["Смартфон", 10000, 20]


@pytest.fixture(scope="session")
def data_for_calculate_total_price():
    instance = Item("Смартфон", 10000, 20)
    tested = instance.calculate_total_price()
    expected = instance.price * instance.quantity

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_apply_discount():
    instance = Item("Смартфон", 10000, 20)

    expected = instance.price * 2

    Item.pay_rate = 2
    instance.apply_discount()

    tested = instance.price

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_name_get():
    instance = Item("Смартфон", 10000, 20)
    expected = "Смартфон"
    tested = instance.name

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_set_name():
    instance = Item("Смартфон", 10000, 20)
    instance.name = "Новый смартфон"

    tested = instance.name
    expected = "Новый смар"

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_string_to_number():
    instance = Item("Смартфон", 10000, 20)
    tested = instance.string_to_number("100")
    expected = 100

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_instantiate_from_csv():
    Item.instantiate_from_csv()

    expected = "Смартфон"
    tested = Item.all[0].name

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_repr():
    instance = Item("Смартфон", 10000, 20)

    tested = repr(instance)
    expected = "Item('Смартфон', 10000, 20)"

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_str():
    instance = Item("Смартфон", 10000, 20)

    tested = str(instance)
    expected = "Смартфон"

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_add_method():
    instance_1 = Item("Смартфон", 10000, 20)
    instance_2 = Item("ПК", 10000, 10)

    expected = 30
    tested = instance_1 + instance_2

    return tested, expected


# Fixtures for testing Phone class
@pytest.fixture(scope="session")
def data_for_test_str_method():
    instance = Phone("Смартфон", 10000, 20, 2)

    tested = str(instance)
    expected = "Смартфон"

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_repr_method():
    instance = Phone("Смартфон", 10000, 20, 2)

    tested = repr(instance)
    expected = "Phone('Смартфон', 10000, 20, 2)"

    return tested, expected


@pytest.fixture(scope="session")
def data_for_test_get_number_of_sim():
    instance = Phone("Смартфон", 10000, 20, 2)

    tested = instance.number_of_sim
    expected = 2

    return tested, expected
