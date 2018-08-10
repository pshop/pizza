from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from stock.models import Pizza, Menu, Product, Restaurant
from user_profile.models import PostalAddress

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

class CardPayment(models.Model):

    transaction_id = models.CharField(max_length=255, null=False)
    bank_name = models.CharField(max_length=100, null=False)

class Status(models.Model):
    label = models.CharField(max_length=100)

class Invoice(models.Model):

    paid_by_card = models.BooleanField()
    date = models.DateTimeField(default=timezone.now())

    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_payment = models.ForeignKey(CardPayment, on_delete=models.CASCADE)

    invoice_address = models.ForeignKey(PostalAddress, on_delete=models.CASCADE, related_name='Invoices')
    delivery_address = models.ForeignKey(PostalAddress, on_delete=models.CASCADE)

    status = models.ManyToManyField(
        Status,
        through='History',
        related_name='Invoices'
    )

class History(models.Model):

    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())
