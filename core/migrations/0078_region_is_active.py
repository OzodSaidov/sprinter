# Generated by Django 3.2.9 on 2021-12-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_auto_20211217_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
