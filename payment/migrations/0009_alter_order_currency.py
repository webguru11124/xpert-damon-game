# Generated by Django 3.2.4 on 2023-07-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(default='USD', max_length=10),
        ),
    ]
