# Generated by Django 4.0.1 on 2022-02-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='done',
            field=models.IntegerField(default=2),
        ),
    ]
