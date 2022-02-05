from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['image_url'] = user.image_url
        token['user_type'] = 'admin' if user.is_staff == 1 else 'customer'

        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
