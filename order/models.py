from django.db import models
from stock.models import Pizza, Menu, Product

# Create your models here.

class Panier(models.Model):

    pizzas = models.ManyToManyField(
        Pizza,
        through='PanierPizza',
        related_name='paniers',
    )

    menus = models.ManyToManyField(
        Menu,
        through='PanierMenu',
        related_name='paniers',
    )

    products = models.ManyToManyField(
        Product,
        through='PanierProduct',
        related_name='paniers',
    )


class PanierPizza(models.Model):

    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    quantity = models.IntegerField()

class PanierMenu(models.Model):

    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    quantity = models.IntegerField()

class PanierProduct(models.Model):

    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

