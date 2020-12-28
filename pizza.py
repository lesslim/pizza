class Pizza:
    """
    Базовый класс пицц.
    """

    def __init__(self, size="L"):
        if size not in ["L", "XL"]:
            raise TypeError("Wrong pizza size - must be L or XL only.")
        self.size = size
        self._ingredients = {
            "tomato sauce": 100,
            "salt": 20,
            "mozzarella": 100,
            "dough": 300,
        }
        if size == "XL":
            for key in self.__dict__['_ingredients']:
                self.__dict__['_ingredients'][key] = int(2 * self.__dict__['_ingredients'][key])

    def dict(self) -> dict:
        return self._ingredients

    def __eq__(self, other) -> bool:
        if isinstance(other, Pizza):
            return self.dict() == other.dict()
        raise TypeError(f"{other} is not a pizza.")

    def __repr__(self) -> str:
        return self.__class__.__name__


class Margherita(Pizza):
    """
    Класс пиццы Маргарита.
    """

    def __init__(self, size="L"):
        super().__init__(size)
        self._ingredients.update({"mozzarella": 150, "parmesan": 150, "tomatoes": 100})

    def __repr__(self):
        return f"{super().__repr__()} 🧀"


class Pepperoni(Pizza):
    """
    Класс Пепперони.
    """

    def __init__(self, size="L"):
        super().__init__(size)
        self._ingredients.update({"pepperoni": 200, "onion": 50})

    def __repr__(self):
        return f"{super().__repr__()} 🍕"


class Hawaiian(Pizza):
    """
    Класс Гавайской пиццы.
    """

    def __init__(self, size="L"):
        super().__init__(size)
        self._ingredients.update({"chicken": 200, "pineapples": 100})

    def __repr__(self):
        return f"{super().__repr__()} 🍍"


if __name__ == "main":
    print("sgfg")
