# Generated by Django 3.2.9 on 2021-12-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0088_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_slider',
            field=models.BooleanField(default=False),
        ),
    ]
