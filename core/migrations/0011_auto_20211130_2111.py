# Generated by Django 3.2.9 on 2021-11-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20211130_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productparam',
            name='param',
        ),
        migrations.AddField(
            model_name='productparam',
            name='name',
            field=models.CharField(default='hi', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productparam',
            name='property',
            field=models.CharField(default='hi', max_length=255),
            preserve_default=False,
        ),
    ]