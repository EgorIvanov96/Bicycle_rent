# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import UserSerialiser, BikeSerialiser, RentalSerialiser
from users.models import User
from reviews.models import Bike, Rental


class UserCustomViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialiser


class BikeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bike.objects.filter(free=True)
    serializer_class = BikeSerialiser


"""class RentBikeViewSet(CreateAPIView):
    serializer_class = RentalSerialiser
    # permission_classes = IsAuthenticated

    def perform_create(self, serializer):
        bike_id = self.request.data.get('bike_id')
        bike = Bike.objects.get(id=bike_id)
        if bike.free:
            user = self.request.user
            rental = serializer.save(user=user, bike=bike)
            bike.free = False
            bike.save()
            return Response(
                {'message': 'Велосипед арендован'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'error': 'Велосипед занят'},
            status=status.HTTP_400_BAD_REQUEST
        )"""


class RentBikeViewSet(APIView):
    def post(self, request):
        user = request.user
        if Rental.objects.filter(user=user, condition=False).exists():
            return Response(
                {'error': 'Вы уже арендовали велосипед'},
                status=status.HTTP_400_BAD_REQUEST
            )
        bike_id = request.data.get('bike_id')
        bike = get_object_or_404(Bike, id=bike_id)
        if bike.free:
            rental = Rental.objects.create(user=user, bike=bike)
            bike.free = False
            bike.save()
            rental.condition = False
            rental.save()
            return Response(
                {'message': 'Вы арендовали велосипед'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'error': 'Велосипед занят'},
            status=status.HTTP_400_BAD_REQUEST
            )
