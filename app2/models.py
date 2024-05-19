from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

class Shop(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(4, "Длина должна быть более 4 символов.")])
    address = models.CharField(max_length=255, validators=[MinLengthValidator(4, "Длина должна быть более 4 символов.")])
    ratingg = models.IntegerField( validators=[MinValueValidator(0, 'Принимается только положительные числа и ноль')], null=True)
