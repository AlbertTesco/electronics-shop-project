from src.phone import Phone


def test_add_method(data_for_test_add_method):
    tested, expected = data_for_test_add_method

    assert tested == expected


def test_str_method(data_for_test_str_method):
    tested, expected = data_for_test_str_method

    assert tested == expected


def test_repr_method(data_for_test_repr_method):
    tested, expected = data_for_test_repr_method

    assert tested == expected


def test_get_number_of_sim(data_for_test_get_number_of_sim):
    tested, expected = data_for_test_get_number_of_sim

    assert tested == expected
