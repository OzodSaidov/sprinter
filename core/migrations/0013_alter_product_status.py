# Generated by Django 3.2.9 on 2022-01-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_product_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', 'Есть в наличии'), ('2', 'Нет в наличии'), ('3', 'Скоро')], default='1', max_length=255),
        ),
    ]
