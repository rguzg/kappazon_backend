from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(GenericViewSet):
    """
    This viewset holds actions related to the current user. For actions related to all users check the Users app
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        updated_user = UserSerializer(
            self.get_queryset(), data=request.data, partial=True)

        if(updated_user.is_valid()):
            updated_user.save()
            return Response(data=updated_user.data, status=200)
        else:
            return Response(data=updated_user.errors, status=400)

    def list(self, request):
        return Response(data=UserSerializer(self.get_queryset()).data, status=200)

    def get_queryset(self):
        return self.request.user
