# Generated by Django 3.2.9 on 2022-01-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20220112_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catalogs',
            field=models.ManyToManyField(to='core.Catalog'),
        ),
    ]
