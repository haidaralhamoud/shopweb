# Generated by Django 4.0.1 on 2022-01-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_employee_fname_remove_employee_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='fname',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='lname',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
