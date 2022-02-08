from typing import Any
from rest_framework import serializers
from .models import Cart, CartItem
from ..products.serializers import ProductSerializer
from kappazon.validators import IsPositive


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
        read_only_fields = ['product', 'quantity']

    def to_representation(self, instance):

        return super().to_representation(instance.cartitem_set.first())


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True)
    total_price = serializers.IntegerField(read_only=True)
    total_items = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart
        exclude = ["user", "id"]
