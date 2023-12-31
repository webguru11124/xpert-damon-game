# Generated by Django 3.2 on 2023-05-31 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230531_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinbaseorder',
            name='up_id',
            field=models.CharField(max_length=255, unique=True, verbose_name='Unique Payment ID'),
        ),
        migrations.AlterField(
            model_name='stripeorder',
            name='up_id',
            field=models.CharField(max_length=255, unique=True, verbose_name='Unique Payment ID'),
        ),
    ]
