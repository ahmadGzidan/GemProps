# Generated by Django 4.1.6 on 2023-09-06 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_house_is_interested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='is_interested',
        ),
    ]