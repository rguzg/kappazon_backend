from typing import Any
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import CartSerializer
from .models import CartItem
from ..products.models import Product


class CartViewSet(viewsets.ModelViewSet):
    """
    This viewset holds actions related to the Product model
    """

    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def destroy(self, request, pk=None):
        """
        Overrides the default destroy method. Deletes an item from the current user's cart.
        """
        cart = self.get_queryset()

        try:
            CartItem.objects.get(cart=cart, product=pk).delete()
            return Response(data=CartSerializer(cart).data, status=200)
        except:
            return Response(data="{'error': 'Product doesn't exist in user's cart'}", status=404)

    def create(self, request, pk=None):
        """
        Overrides the default create method. Adds/Modifies an item on the current user's cart.
        """
        cart = self.get_queryset()

        try:
            product = Product.objects.get(pk=request.data['product'])

            if(product.is_archived):
                return Response(data={"message": "Product is archived"}, status=400)

            if(product.inventory < request.data['quantity']):
                return Response(data={"message": "Not enough inventory"}, status=400)

            cart_item, _ = CartItem.objects.get_or_create(
                cart=cart, product=product, defaults={"cart": cart, "product": product})

            if(request.data['quantity'] == 0):
                cart_item.delete()
            else:
                cart_item.quantity = request.data['quantity']
                cart_item.save()
        except:
            return Response(data="{'error': 'Product doesn't exist'}", status=404)

        cart.total_price += product.price * request.data['quantity']
        cart.total_items += request.data['quantity']

        cart.save()

        return Response(data=CartSerializer(cart).data, status=200)

    def list(self, request):
        return Response(data=CartSerializer(self.get_queryset()).data, status=200)

    def get_queryset(self):
        user: Any = self.request.user

        return user.cart
