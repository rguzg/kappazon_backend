from django.db import models
from ..users.models import User
from ..products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0)
    total_items = models.PositiveIntegerField(default=0)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'product'], name='unique_cart_item')
        ]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
