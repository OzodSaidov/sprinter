# Generated by Django 3.2.9 on 2021-12-17 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_region_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='is_active',
        ),
    ]