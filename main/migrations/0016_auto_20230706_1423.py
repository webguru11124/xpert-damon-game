# Generated by Django 3.2.4 on 2023-07-06 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20230620_1416'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CoinbaseOrder',
        ),
        migrations.DeleteModel(
            name='StripeOrder',
        ),
    ]