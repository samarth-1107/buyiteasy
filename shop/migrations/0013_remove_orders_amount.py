# Generated by Django 3.1.2 on 2020-12-20 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20201220_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]