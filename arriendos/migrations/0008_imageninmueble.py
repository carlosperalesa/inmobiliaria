# Generated by Django 4.2.13 on 2024-05-23 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arriendos', '0007_alter_usuario_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenInmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='inmuebles/')),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='arriendos.inmueble')),
            ],
        ),
    ]
