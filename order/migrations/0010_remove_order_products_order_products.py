# Generated by Django 4.0.1 on 2022-02-15 11:52

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_description2'),
        ('order', '0009_alter_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, default=order.models.all_products, null=True, to='products.Products'),
        ),
    ]
