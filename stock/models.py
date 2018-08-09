from django.db import models

# Create your models here.


class Restaurant(models.Model):

    label = models.CharField(max_length=50, null=False)


class Ingredient(models.Model):

    label = models.CharField(max_length=50, null=False)
    restaurant = models.ManyToManyField(
        Restaurant,
        through='IngredientStock',
        related_name='ingredients')


class IngredientStock(models.Model):
    """
    parameters:
    Ingredient object
    Restaurant object
    quantity decimal(8.2)
    unit varchar(50)
    Defines the stock of ingredient for every restaurant
    """
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=50)


class Product(models.Model):

    description = models.CharField(max_length=300)
    label = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ManyToManyField(
        Restaurant,
        through='ProductStock',
        related_name='products'
    )

class ProductStock(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    quantity = models.IntegerField()

class Pizza(models.Model):

    label = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    picture = models.ImageField(upload_to="photos/")
    nb_sold = models.IntegerField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Recipe',
        related_name='pizzas'
    )

class Recipe(models.Model):

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=50)


