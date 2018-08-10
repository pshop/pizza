from django.test import TestCase
from stock.models import Product, Pizza, Menu
from .models import Panier, PanierMenu, PanierPizza, PanierProduct

import stock.tests as test_function


def add_panier_in_base():

    Panier.objects.create().save()
    return Panier.objects.get(pk=1)

def add_product_in_panier():

    panier = add_panier_in_base()

    test_function.add_product_to_base()
    product = Product.objects.get(pk=1)

    PanierProduct.objects.create(
        panier=panier,
        product=product,
        quantity=1).save()

    return PanierProduct.objects.get(pk=1)

def add_pizza_in_panier():

    panier = add_panier_in_base()

    test_function.add_pizza_to_base()
    pizza = Pizza.objects.get(pk=1)

    PanierPizza.objects.create(
        pizza=pizza,
        panier=panier,
        quantity=2
    ).save()

    return PanierPizza.objects.get(pk=1)

def add_menu_in_panier():

    panier = add_panier_in_base()

    test_function.add_menu_to_base()
    menu = Menu.objects.get(pk=1)

    PanierMenu.objects.create(
        menu=menu,
        panier=panier,
        quantity=3
    ).save()

    return PanierMenu.objects.get(pk=1)

def add_three_items_in_panier():

    panier = add_panier_in_base()

    test_function.add_menu_to_base()
    menu = Menu.objects.get(pk=1)

    test_function.add_pizza_to_base()
    pizza = Pizza.objects.get(pk=1)

    test_function.add_product_to_base()
    product = Product.objects.get(pk=1)

    PanierMenu.objects.create(panier=panier, menu=menu, quantity=1)
    PanierPizza.objects.create(panier=panier, pizza=pizza, quantity=2)
    PanierProduct.objects.create(panier=panier, product=product, quantity=3)

    return Panier.objects.get(pk=1)

# Create your tests here.

class OrderTest(TestCase):

    def test_adding_panier_to_base(self):
        panier = add_panier_in_base()
        self.assertEqual(panier.id, 1)


    def test_adding_product_to_panier(self):
        panier_product = add_product_in_panier()

        self.assertEqual(panier_product.product.label, 'Coca-Cola')
        self.assertEqual(panier_product.quantity, 1)
        self.assertEqual(panier_product.panier.id, 1)


    def test_adding_menu_to_panier(self):
        panier_menu = add_menu_in_panier()

        self.assertEqual(panier_menu.menu.label, 'petite faim')
        self.assertEqual(panier_menu.quantity, 3)
        self.assertEqual(panier_menu.panier.id, 1)


    def test_adding_pizza_to_panier(self):
        panier_pizza = add_pizza_in_panier()

        self.assertEqual(panier_pizza.pizza.label, 'margherita')
        self.assertEqual(panier_pizza.quantity, 2)
        self.assertEqual(panier_pizza.panier.id,1)


    def test_add_get_three_items_to_panier(self):

        panier = add_three_items_in_panier()

        menu = panier.menus.get(label='petite faim')
        product = panier.products.get(label='Coca-Cola')
        pizza = panier.pizzas.get(label='margherita')

        self.assertEqual(menu.label, 'petite faim')
        self.assertEqual(product.label, 'Coca-Cola')
        self.assertEqual(pizza.label, 'margherita')

        margherita = PanierPizza.objects.get(pizza__label= 'margherita')
        self.assertEqual(margherita.quantity, 2)


