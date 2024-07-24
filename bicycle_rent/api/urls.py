from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import UserCustomViewSet, BikeViewSet, RentBikeViewSet


app_name = 'api'

router = DefaultRouter()
router.register('users', UserCustomViewSet, basename='users')
router.register('bikes', BikeViewSet, basename='bikes')
# router.register('rent', RentBikeViewSet, basename='rent_bike')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('rent/', RentBikeViewSet.as_view(), name='rent_bike'),
]
