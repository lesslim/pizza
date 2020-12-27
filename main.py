import click
from pizza import Margherita, Pepperoni, Hawaiian
from stuff import bake, pickup, delivery

MENU = {"margherita": Margherita(), "pepperoni": Pepperoni(), "hawaiian": Hawaiian()}

@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', 'delivery_flag', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
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
    print("sdf")
    for pizza in MENU.values():
        print(f'- {pizza}: {", ".join(pizza.dict())}')


if __name__ == 'main':
    cli()

