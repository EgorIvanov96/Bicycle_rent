from django.db import models

from users.models import User


class Bike(models.Model):
    """Модель велосипеда."""
    name = models.CharField(
       max_length=256,
       verbose_name='Модель велосипеда'
    )
    description = models.CharField(
        max_length=256,
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Стоимость аренды велосипеда за минуту, руб'
    )

    class Meta:
        verbose_name = 'Велосипед'
        verbose_name_plural = 'велосипеды'

    def __str__(self):
        return self.name


class Rental(models.Model):
    """Модель аренды велосипеда."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    bike = models.ForeignKey(
        Bike,
        on_delete=models.CASCADE,
        verbose_name='Модель велосипеда'
    )
    start_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Начало аренды'
    )
    end_time = models.DateField(
        null=True,
        blank=True,
        verbose_name='Конец аренды'
    )
    total = models.DecimalField(
        verbose_name='Сумма аренды',
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Аренда велосипедов'
        ordering = ('-start_time',)

    def __str__(self):
        return f'{self.user} - {self.total}'
