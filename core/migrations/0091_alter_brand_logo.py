# Generated by Django 3.2.9 on 2021-12-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0090_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/brands'),
        ),
    ]
