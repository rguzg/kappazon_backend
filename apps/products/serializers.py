from rest_framework import serializers
from .models import Product
from kappazon.validators import IsPositive


class ProductSerializer(serializers.ModelSerializer):
    """
    Handles serialization and deserialization of Product objects

    Fields:
    - id: The unique identifier of the product. Read-only, assigned automatically when the product is created.
    - name: The name of the product. Required.
    - description: A description of the product. Required.
    - price: The price of the product. Required, must be a positive number.
    - inventory: The number of items in stock. Required, must be a positive number.
    - image_url: The URL of the product's image. Required.
    - is_archived: Whether the product is archived. Default value is False.
    - created_at: The date and time the product was created. Read-only.
    - updated_at: The date and time the product was last updated. Read-only.
    """

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

        extra_kwargs = {
            "name": {"required": True},
            "description": {"required": True},
            "price": {"required": True, "validators": [IsPositive]},
            "inventory": {"default": 0, "validators": [IsPositive]},
            "image_url": {"required": True},
            "is_archived": {"default": False},
        }
