# Generated by Django 3.2.9 on 2022-01-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_merge_20220112_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Запрос обработан?'),
        ),
    ]
