from typing import Any
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer
from .models import Product
from kappazon.custom_permissions import IsAccountAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset holds actions related to the Product model
    """

    serializer_class = ProductSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
    pagination_class = PageNumberPagination

    def destroy(self, request, pk=None):
        """
        Overrides the default destroy method to archive the product instead of deleting it
        """
        instance = self.get_object()
        instance.is_archived = True
        instance.save()
        return Response(data=ProductSerializer(instance).data, status=200)

    def get_queryset(self):
        if self.action == 'list':
            return self.GetListQuerySet(self.request)
        else:
            return Product.objects.all()

    def GetListQuerySet(self, request: Any):
        """
        Returns a queryset of products filtered according to the request's query parameters:

        - show_archived: If set to true, archived products will be included in the queryset. Default is false.
        - show_nostock: If set to true, products with no stock will be included in the queryset. Default is false.
        """
        productQuerySet = Product.objects

        shouldHideArchived = request.query_params.get(
            "show_archived", "false") != "true"
        shouldHideNoStock = request.query_params.get(
            "show_nostock", "false") != "true"

        if shouldHideNoStock:
            productQuerySet = productQuerySet.filter(inventory__gt=0)
        else:
            productQuerySet = productQuerySet.filter(inventory__gte=0)

        if shouldHideArchived:
            productQuerySet = productQuerySet.filter(is_archived=False)

        return productQuerySet
