# Generated by Django 3.2.9 on 2022-01-12 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20220112_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catalog',
        ),
    ]
