# Generated by Django 3.1.2 on 2020-12-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default='', max_length=100),
        ),
    ]
