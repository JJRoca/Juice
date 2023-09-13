# Generated by Django 4.2.5 on 2023-09-13 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Producto', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediente', models.CharField(blank=True, max_length=50, null=True)),
                ('extras', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.PositiveIntegerField(blank=True, null=True)),
                ('precio_venta', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fecha_venta', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('codProductoIn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.productointerno')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ventas.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toke_user', models.CharField(max_length=50)),
                ('ingredientes', models.CharField(default='Sin ingredientes', max_length=50)),
                ('extras', models.CharField(default='S/E', max_length=50)),
                ('tamaño', models.CharField(max_length=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paraLlevar', models.CharField(default='No', max_length=50)),
                ('categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.categoriaproducto')),
                ('codProductoIn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.productointerno')),
            ],
        ),
    ]