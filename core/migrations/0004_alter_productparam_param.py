# Generated by Django 3.2.9 on 2021-11-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productparam',
            name='param',
            field=models.JSONField(default=dict),
        ),
    ]
