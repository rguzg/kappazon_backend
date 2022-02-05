from rest_framework import serializers, validators
from .models import User


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name',
                  'last_name', 'birthdate', 'gender', 'image_url']
        extra_kwargs = {
            "email": {"required": True, "validators": [validators.UniqueValidator(queryset=User.objects.all(), message="This email is already assigned to another account")]},
            "password": {"required": True, "write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "birthdate": {"required": True},
            "gender": {"required": True},
            "image_url": {"required": True}
        }

    def create(self, validated_data):
        user = User(username=validated_data['email'], **validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
