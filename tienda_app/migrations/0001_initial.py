# Generated by Django 5.0.2 on 2024-02-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('imagen', models.ImageField(upload_to='tienda')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('categorias', models.ManyToManyField(to='tienda_app.categoria')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]
