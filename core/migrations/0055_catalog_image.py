# Generated by Django 3.2.9 on 2021-12-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_auto_20211207_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='image',
            field=models.ImageField(default='d', upload_to='photos/catalogs'),
            preserve_default=False,
        ),
    ]
