# Generated by Django 3.1.2 on 2020-12-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20201220_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.CharField(default='', max_length=100),
        ),
    ]
