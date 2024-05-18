# Generated by Django 5.0.6 on 2024-05-18 08:29

import arriendos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendos', '0003_remove_inmueble_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=10, validators=[arriendos.models.validar_formato_rut]),
        ),
    ]