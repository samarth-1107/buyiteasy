# Generated by Django 3.1.2 on 2020-12-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20201220_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amnt',
        ),
        migrations.AddField(
            model_name='orders',
            name='the_amount',
            field=models.IntegerField(default=0),
        ),
    ]
