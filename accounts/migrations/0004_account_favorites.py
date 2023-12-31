# Generated by Django 4.1.6 on 2023-09-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_favorite_delete_image_remove_house_interested_users_and_more'),
        ('accounts', '0003_remove_account_interested_houses'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='offers.favorite'),
        ),
    ]
