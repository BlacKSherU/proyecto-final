# Generated by Django 5.0.2 on 2024-02-15 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0002_producto_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categorias',
        ),
        migrations.AddField(
            model_name='producto',
            name='categorias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_app.categoria'),
        ),
    ]