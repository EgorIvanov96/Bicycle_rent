from rest_framework import serializers

from users.models import User
from reviews.models import Bike, Rental


class UserSerialiser(serializers.ModelSerializer):
    """Сериализатор для модели пользователя."""

    class Meta:
        model = User
        fields = (all,)


class BikeSerialiser(serializers.ModelSerializer):
    """Сериализатор для модели велосипеда."""

    class Meta:
        model = Bike
        fields = ('name',
                  'description',
                  'price',
                  'free')


class RentalSerialiser(serializers.ModelSerializer):
    """Сериалезатор для модели аренды."""

    class Meta:
        model = Rental
        fields = (all, )
