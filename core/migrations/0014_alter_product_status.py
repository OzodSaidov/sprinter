# Generated by Django 3.2.9 on 2022-01-12 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=255),
        ),
    ]
