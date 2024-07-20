from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    """Модель юзера."""
    username = models.CharField(
        max_length=256,
        verbose_name='Имя пользователя',
        help_text='Укажите свое имя',
        validators=[
            RegexValidator(
                r'^[\w.@+-]+\Z',
                'Поле username содержит недопустимые символы.'
            )
        ],
        unique=True
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Email',
        help_text='Укажите свой email',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
