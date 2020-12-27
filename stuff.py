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

@log("{} {} за ⌚ {}мин!")
def bake(pizza: Pizza) -> str:
    """Возвращает сообщение о готовке пиццы."""
    return "🍺 Приготовили"


@log("{} {} за ⌚ {}мин!")
def delivery(pizza: Pizza) -> str:
    """Возвращает сообщение о доставке пиццы."""
    return "🛵 Доставили"


@log("{} {} за ⌚ {}мин!")
def pickup(pizza: Pizza) -> str:
    """Возвращает сообщение о самовывозе пиццы."""
    return "🏡 Забрали"





