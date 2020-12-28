from random import randint
from functools import wraps
from typing import Callable
from pizza import Pizza


def log(template: str) -> Callable:
    def deco(func: Callable) -> Callable:
        if not isinstance(template, str):
            raise TypeError("Template should be a string.")

        @wraps(func)
        def wrap(*args, **kwargs) -> Callable:
            ans = func(*args, **kwargs)
            print(template.format(randint(1, 5)))
            return ans

        return wrap

    return deco


@log("Приготовили за {} мин")
def bake(pizza: Pizza) -> str:
    """Сообщение о готовке пиццы."""
    pass


@log("Доставили за {} мин")
def delivery(pizza: Pizza) -> str:
    """Сообщение о доставке пиццы."""
    pass


@log("Забрали за {} мин")
def pickup(pizza: Pizza) -> str:
    """Сообщение о самовывозе пиццы."""
    pass
