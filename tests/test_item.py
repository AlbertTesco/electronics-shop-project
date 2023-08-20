import pytest
from src.item import Item, InstantiateCSVError


# Test module
def test_item(data_for_test_item):
    # instance = Item("Смартфон", 10000, 20)
    tested, expected = data_for_test_item

    assert expected[0] == tested[0]
    assert expected[1] == tested[1]
    assert expected[2] == tested[2]


def test_calculate_total_price(data_for_calculate_total_price):
    tested, expected = data_for_calculate_total_price

    assert tested == expected


def test_apply_discount(data_for_test_apply_discount):
    tested, expected = data_for_test_apply_discount

    assert tested == expected


def test_name(data_for_test_name_get):
    """
    Test getting item name
    """
    tested, expected = data_for_test_name_get

    assert tested == expected


def test_set_name(data_for_test_set_name):
    """
    Test setting item name
    """
    tested, expected = data_for_test_set_name

    assert tested == expected


def test_string_to_number(data_for_test_string_to_number):
    tested, expected = data_for_test_string_to_number

    assert tested == expected


def test_instantiate_from_csv(data_for_test_instantiate_from_csv):
    tested, expected = data_for_test_instantiate_from_csv

    assert tested == expected


def test_repr(data_for_test_repr):
    tested, expected = data_for_test_repr

    assert tested == expected


def test_str(data_for_test_str):
    tested, expected = data_for_test_str

    assert tested == expected


def test_add_method(data_for_test_add_method):
    tested, expected = data_for_test_add_method

    assert tested == expected


def test_exception_instantiate_from_csv():
    # Проверка наличия файла items.csv в данной директории
    with pytest.raises(FileNotFoundError, match="Файл items.csv не найден"):
        Item.instantiate_from_csv('items.csv')

    # Проверка заведомого битого файла test_broken.csv
    with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
        Item.instantiate_from_csv('test_broken.csv')
