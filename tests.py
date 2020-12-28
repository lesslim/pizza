from pizza import Pizza, Margherita, Pepperoni, Hawaiian
import random


random.seed(42)


def test_pizza_name():
    assert str(Margherita()) == "Margherita 🧀"


def test_pizza_size():
    assert Pepperoni().size == "L"


def test_pizza_dict():
    exp = {
        "chicken": 200,
        "dough": 300,
        "mozzarella": 100,
        "pineapples": 100,
        "salt": 20,
        "tomato sauce": 100,
    }
    assert Hawaiian().dict() == exp


def test_pizza_eq():
    assert Pepperoni() != Pizza()


def test_eq_size():
    assert Margherita() != Margherita("XL")
