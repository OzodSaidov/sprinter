# Generated by Django 3.2.9 on 2021-12-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20211201_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='productgroup',
            name='title_en',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]