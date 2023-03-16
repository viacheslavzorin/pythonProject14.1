import pytest
from item import Item, Phone, Keyboard


# item = Item("Смартфон", 20, 10000)
def test_calculate_total_prise():
    item = Item("Смартфон", 20, 10000)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    item = Item("Смартфон", 20, 10000)
    assert item.apply_discount == 8500.0


def test_instantiate_from_csv():
    assert len(Item.instantiate_from_csv()) == 5
    item4 = Item.instantiate_from_csv()[2]
    assert item4._Item__product == 'Кабель'


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.8) is False


def test_long_name():
    item7 = Item('eee', 1000, 10)
    assert item7.long_name == 'eee'

    with pytest.raises(Exception):
        assert item7.long_name("aaaaaaaaaaa")


def test_repr():
    item5 = Item('sos', 30, 6)
    assert item5.__repr__() == "Item('sos', '30', '6,)"


def test_str():
    item6 = Item('kkk', 80, 33)
    assert item6.__str__() == "kkk"


def test_init_phone():
    phone = Phone("Смартфон", 20, 10000, 2)
    assert phone.number_of_sim == 2


def test_quantity_sim():
    phone7 = Phone('eee', 1000, 10, 2)
    with pytest.raises(Exception):
        assert phone7.quantity_sim("a")
    assert phone7.number_of_sim == 2


def test_add():
    phone7 = Phone('eee', 1000, 10, 2)
    item7 = Item('eee', 100, 10)
    assert phone7 + item7 == 1100

    class Book:
        def __init__(self, quanity):
            self.quanity = quanity

    book = Book(2)
    with pytest.raises(ValueError):
        assert phone7 + book

def test_change_lang():
    item1 = Keyboard("Клавиатура", 100, 5)
    assert item1.language == "EN"
    item1.change_lang()
    assert item1.language == "RU"
