# Generated by Django 2.2.2 on 2021-05-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_karma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='karma',
            field=models.IntegerField(default=0),
        ),
    ]
