from typing import Any
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from apps.products.serializers import ProductSerializer
from .serializers import PurchaseSerializer
from .models import Purchase, PurchaseItem, PURCHASE_STATES
from ..cart.models import Cart


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    This viewset holds actions related to the Purchase model
    """

    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def create(self, request, pk=None):
        """
        Overrides the default create method. Creates a new purchase and empties the current user's cart.
        """
        cart = Cart.objects.get(user=request.user)
        nostock_products = []
        product_total = 0

        for cartItem in cart.cartitem_set.all():
            product_total += cartItem.product.price * cartItem.quantity
            if(cartItem.quantity > cartItem.product.inventory):
                nostock_products.append(cartItem.product)

        if(len(nostock_products) > 0):
            serialized_products = ProductSerializer(
                nostock_products, many=True)

            return Response(data={"message": "Not enough stock for products", "products": serialized_products.data}, status=400)
        else:
            purchase = Purchase(
                user=request.user, state=PURCHASE_STATES['Purchased'], product_total=product_total, shipping_total=2)
            purchase.save()

            for cartItem in cart.cartitem_set.all():
                PurchaseItem(purchase_id=purchase.pk, product=cartItem.product,
                             quantity=cartItem.quantity).save()

                cartItem.product.inventory -= cartItem.quantity
                cartItem.product.save()

                cartItem.delete()

            cart.total_price = 0
            cart.total_items = 0
            cart.save()

            return Response(data=PurchaseSerializer(purchase).data, status=200)

    def list(self, request):
        return Response(data=PurchaseSerializer(self.get_queryset(), many=True).data, status=200)

    def get_queryset(self):
        user: Any = self.request.user

        return Purchase.objects.filter(user=user).all()
