# Generated by Django 4.1.6 on 2023-09-06 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_interested_houses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='interested_houses',
        ),
    ]
