from django.test import TestCase
from .models import\
    Restaurant,\
    Ingredient,\
    IngredientStock,\
    Product,\
    ProductStock

def add_ingredient_to_base():

    Ingredient(label='salade').save()

def add_restaurant_label_to_base():

    Restaurant(label='Paris centre').save()

def add_ingredient_to_restaurant_stock(ingredient, restaurant):

    IngredientStock(
        ingredient=ingredient,
        restaurant=restaurant,
        quantity=100.0,
        unit='sac de 4kg',
    ).save()

def add_product_to_base():

    Product(
        label='Coca-Cola',
        description='Bouteille de Coca-Cola de 50cl',
        price=4.0
    ).save()

def add_product_to_restaurant_stock(product,restaurant):

    ProductStock(
        product=product,
        restaurant=restaurant,
        quantity=10
    ).save()

def add_pizza_to_base():
    pass

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




