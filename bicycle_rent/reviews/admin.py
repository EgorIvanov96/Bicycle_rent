from django.contrib import admin

from .models import Bike, Rental


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name', 'price')
    search_fields = ('name', 'price')


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'bike', 'start_time', 'end_time', 'total')
    list_filter = ('user', 'bike', 'start_time', 'end_time', 'total')
    search_fields = ('user', 'bike', 'start_time', 'end_time', 'total')


admin.site.empty_value_display = 'Не задано'
