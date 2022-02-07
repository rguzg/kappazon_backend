from rest_framework import serializers

def IsPositive(value):
    """
    Throws a ValidationError if the value is not positive. Accepts both int and float values.
    """

    if value < 0:
        raise serializers.ValidationError("Value must be bigger or equal to 0")
