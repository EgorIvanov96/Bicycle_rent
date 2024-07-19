from rest_framework import serializers

from users.models import User


class UserSerialiser(serializers.ModelSerializer):
    """Сериализатор для модели пользователя."""

    class Meta:
        model = User
        fields = (all,)
