# Generated by Django 3.2.9 on 2021-11-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_promocode_product_param'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Title'),
        ),
    ]
