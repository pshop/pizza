from django.test import TestCase
from .models import\
    Restaurant,\
    Ingredient,\
    IngredientStock,\
    Product,\
    ProductStock,\
    Pizza,\
    Recipe,\
    Menu

def add_ingredient_to_base():

    Ingredient.objects.create(label='salade').save()

def add_restaurant_label_to_base():

    Restaurant.objects.create(label='Paris centre').save()

def add_ingredient_to_restaurant_stock(ingredient, restaurant):

    IngredientStock.objects.create(
        ingredient=ingredient,
        restaurant=restaurant,
        quantity=100.0,
        unit='sac de 4kg',
    ).save()

def add_product_to_base():

    Product.objects.create(
        label='Coca-Cola',
        description='Bouteille de Coca-Cola de 50cl',
        price=4.0
    ).save()

    Product.objects.create(
        label='Evian',
        description='L\'eau de source',
        price=3.0
    )

def add_product_to_restaurant_stock(product,restaurant):

    ProductStock.objects.create(
        product=product,
        restaurant=restaurant,
        quantity=10
    ).save()

def add_pizza_to_base():

    Pizza.objects.create(
        label='margherita',
        description = 'On a pas su faire plus simple',
        price = 10.0,
        nb_sold = 130,
    ).save()

def add_recipe_to_base(ingredient, pizza):

    Recipe.objects.create(
        ingredient = ingredient,
        pizza = pizza,
        amount = 3.5,
        unit = 'tranches'
    ).save()

def add_menu_to_base():

    add_pizza_to_base()
    pizza = Pizza.objects.get(pk=1)

    add_product_to_base()
    prod = Product.objects.get(pk=1)

    Menu.objects.create(
        price=12.0,
        label='petite faim',
        description= 'Un menu simple pour des envies simples'
    ).save()

# Create your tests here.

class StockTest(TestCase):

    def test_adding_ingredient_to_base(self):

        add_ingredient_to_base()

        ingredient = Ingredient.objects.get(pk=1)

        self.assertEqual(ingredient.label, 'salade')

    def test_adding_restaurant_to_base(self):

        add_restaurant_label_to_base()

        resto = Restaurant.objects.get(pk=1)

        self.assertEqual(resto.label, 'Paris centre')

    def test_adding_ingredient_stock_to_base(self):

        add_ingredient_to_base()
        add_restaurant_label_to_base()

        ingredient = Ingredient.objects.get(pk=1)
        restaurant = Restaurant.objects.get(pk=1)


        add_ingredient_to_restaurant_stock(ingredient, restaurant)
        ing_stck = IngredientStock.objects.get(pk=1)

        self.assertEqual(ing_stck.ingredient.label, 'salade')
        self.assertEqual(ing_stck.restaurant.label, 'Paris centre')
        self.assertEqual(ing_stck.quantity, 100.0)
        self.assertEqual(ing_stck.unit, 'sac de 4kg')

    def test_adding_product_to_base(self):

        add_product_to_base()

        prod = Product.objects.get(pk=1)

        self.assertEqual(prod.label, 'Coca-Cola')
        self.assertEqual(prod.description, 'Bouteille de Coca-Cola de 50cl')
        self.assertEqual(prod.price, 4.0)

    def test_adding_product_stock_to_base(self):

        add_restaurant_label_to_base()
        resto = Restaurant.objects.get(pk=1)

        add_product_to_base()
        prod = Product.objects.get(pk=1)

        add_product_to_restaurant_stock(prod,resto)
        prod_stock = ProductStock.objects.get(pk=1)

        self.assertEqual(prod_stock.quantity, 10)
        self.assertEqual(prod_stock.restaurant.label, 'Paris centre')
        self.assertEqual(prod_stock.product.label, 'Coca-Cola')

    def test_adding_pizza_to_base(self):

        add_pizza_to_base()

        pizza = Pizza.objects.get(pk=1)

        self.assertEqual(pizza.label, 'margherita')
        self.assertEqual(pizza.description, 'On a pas su faire plus simple')
        self.assertEqual(pizza.price, 10.0)
        self.assertEqual(pizza.nb_sold, 130)

    def test_adding_recipe_to_base(self):

        add_ingredient_to_base()
        ingredient = Ingredient.objects.get(pk=1)

        add_pizza_to_base()
        pizza = Pizza.objects.get(pk=1)

        add_recipe_to_base(ingredient, pizza)
        recipe = Recipe.objects.get(pk=1)

        self.assertEqual(recipe.ingredient.label, 'salade')
        self.assertEqual(recipe.pizza.label, 'margherita')
        self.assertEqual(recipe.amount, 3.5)
        self.assertEqual(recipe.unit, 'tranches')

    def test_adding_menu_to_base(self):

        add_menu_to_base()
        menu = Menu.objects.get(pk=1)

        self.assertEqual(menu.label, 'petite faim')
        self.assertEqual(menu.description, 'Un menu simple pour des envies simples')
        self.assertEqual(menu.price, 12.0)

    def test_adding_one_pizza_and_two_products_to_menu(self):

        add_pizza_to_base()
        pizza = Pizza.objects.get(pk=1)

        add_product_to_base()
        prod = Product.objects.get(pk=1)
        prod2 = Product.objects.get(pk=2)

        add_menu_to_base()
        menu = Menu.objects.get(pk=1)

        pizza.menus.add(menu)
        prod.menus.add(menu)
        prod2.menus.add(menu)

        petite_faim_prods = list(Product.objects.filter(menus__label__contains='faim'))


        self.assertEqual(petite_faim_prods[0].label, 'Coca-Cola')
        self.assertEqual(petite_faim_prods[1].label, 'Evian')










