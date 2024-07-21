from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import UserCustomViewSet, BikeViewSet


app_name = 'api'

router = DefaultRouter()
router.register('users', UserCustomViewSet, basename='users')
router.register('bikes', BikeViewSet, basename='bikes')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
