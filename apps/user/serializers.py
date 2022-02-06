from rest_framework import serializers
from ..users.models import User


class UserTypeField(serializers.Field):
    """
    Field that returns if the user is an admin or a customer
    """

    def get_attribute(self, instance):
        return instance

    def to_representation(self, user):
        return 'admin' if user.is_staff == 1 else 'customer'


class UserSerializer(serializers.ModelSerializer):
    """
    Used for getting or updating the current user's information. This serializer cannot be used to change the user's password or to update its user type.
    """

    user_type = UserTypeField()

    class Meta:
        model = User
        fields = ['email', 'first_name',
                  'last_name', 'birthdate', 'gender', 'image_url', 'user_type']
        read_only_fields = ["email", "user_type"]
