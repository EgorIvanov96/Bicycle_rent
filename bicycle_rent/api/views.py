from django.shortcuts import render
from djoser.views import UserViewSet

from .serializers import UserSerialiser
from users.models import User


class UserCustomViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
