# Generated by Django 3.2.4 on 2023-07-15 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('payment', '0005_alter_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='game',
        ),
        migrations.AddField(
            model_name='order',
            name='content_type',
            field=models.ForeignKey(default=28, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
