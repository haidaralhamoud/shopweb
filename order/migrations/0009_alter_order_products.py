# Generated by Django 4.0.1 on 2022-02-15 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_description2'),
        ('order', '0008_order_id_products_remove_order_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]