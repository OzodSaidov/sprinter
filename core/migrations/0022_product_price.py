# Generated by Django 3.2.9 on 2021-12-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20211201_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=123),
            preserve_default=False,
        ),
    ]
