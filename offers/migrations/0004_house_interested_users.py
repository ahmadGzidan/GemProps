# Generated by Django 4.1.6 on 2023-09-06 10:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offers', '0003_remove_house_is_interested'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='interested_users',
            field=models.ManyToManyField(blank=True, related_name='interested_houses', to=settings.AUTH_USER_MODEL),
        ),
    ]
