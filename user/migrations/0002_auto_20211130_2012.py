# Generated by Django 3.2.9 on 2021-11-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address_uz',
            field=models.TextField(null=True),
        ),
    ]
