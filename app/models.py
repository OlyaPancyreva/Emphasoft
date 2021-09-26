from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
