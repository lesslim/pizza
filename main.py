import click
from pizza import Margherita, Pepperoni, Hawaiian, Pizza
from stuff import bake, pickup, delivery

MENU = {
    "margherita": Margherita(),
    "pepperoni": Pepperoni(),
    "hawaiian": Hawaiian(),
    "pizza": Pizza(),
}


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", "delivery_flag", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery_flag: bool):
    """Готовит и доставляет пиццу"""
    pizza = pizza.lower()
    if pizza not in MENU:
        click.echo("This pizza is not on the menu")
        return
    bake(MENU[pizza])
    if delivery_flag:
        delivery(MENU[pizza])
    else:
        pickup(MENU[pizza])


@cli.command()
def menu():
    """Выводит меню"""
    for p in MENU.values():
        click.echo(f'{p}: {", ".join(f"{k} - {v} gram" for k, v in p.dict().items())}')


if __name__ == "__main__":
    cli()
