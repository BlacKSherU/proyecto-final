# Generated by Django 5.0.2 on 2024-02-17 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tienda_app', '0004_remove_producto_categorias_producto_categorias'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='LineaPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_app.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
            ],
            options={
                'verbose_name': 'linea_pedido',
                'verbose_name_plural': 'linea_pedidos',
            },
        ),
    ]
