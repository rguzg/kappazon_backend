from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CreateCustomerSerializer


class UsersViewSet(viewsets.ViewSet):
    """
    This viewset holds actions related to the User model. For actions related to a specific user check the User app
    """

    @action(detail=False, methods=['post'])
    def create_customer(self, request):
        """
        Create a new customer
        """

        serializer = CreateCustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        else:
            return Response(data=serializer.errors, status=400)
