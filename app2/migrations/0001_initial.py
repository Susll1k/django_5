# Generated by Django 5.0.6 on 2024-05-19 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(4, 'Длина должна быть более 4 символов.')])),
                ('address', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(4, 'Длина должна быть более 4 символов.')])),
                ('ratingg', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Принимается только положительные числа и ноль')])),
            ],
        ),
    ]
