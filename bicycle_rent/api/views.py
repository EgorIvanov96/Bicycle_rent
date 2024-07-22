# from django.shortcuts import render
from djoser.views import UserViewSet
from rest_framework import viewsets

from .serializers import UserSerialiser, BikeSerialiser
from users.models import User
from reviews.models import Bike, Rental


class UserCustomViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class BikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bike.objects.filter(free=True)
    serializer_class = BikeSerialiser
