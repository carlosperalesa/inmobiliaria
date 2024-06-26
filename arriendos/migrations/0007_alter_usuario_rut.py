# Generated by Django 5.0.6 on 2024-05-21 21:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendos', '0006_alter_inmueble_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='El formato del RUT debe ser 7 u 8 dígitos seguidos de un guión y un dígito verificador.', regex='^\\d{7,8}-[\\dKk]$')]),
        ),
    ]
