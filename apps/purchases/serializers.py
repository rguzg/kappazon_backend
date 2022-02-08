from rest_framework import serializers
from .models import Purchase, PurchaseItem
from ..products.serializers import ProductSerializer


class PurchaseItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = PurchaseItem
        fields = ['product', 'quantity']
        read_only_fields = ['product', 'quantity']

    def to_representation(self, instance):

        return super().to_representation(instance.purchaseitem_set.first())


class PurchaseSerializer(serializers.ModelSerializer):
    products = PurchaseItemSerializer(many=True)

    class Meta:
        model = Purchase
        exclude = ["user", "id"]
