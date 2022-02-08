from django.db import models
from ..users.models import User
from ..products.models import Product
from .purchaseStates import PURCHASE_STATES


class Purchase(models.Model):
    PURCHASE_CHOICES = [
        (PURCHASE_STATES['Purchased'], 'Purchased'),
        (PURCHASE_STATES['Delivered'], 'Delivered'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(
        max_length=1, choices=PURCHASE_CHOICES, default='P')
    product_total = models.PositiveIntegerField()
    shipping_total = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, through='PurchaseItem')


class PurchaseItem(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['purchase', 'product'], name='unique_purchase_item')
        ]

    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
