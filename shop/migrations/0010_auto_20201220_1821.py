# Generated by Django 3.1.2 on 2020-12-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]