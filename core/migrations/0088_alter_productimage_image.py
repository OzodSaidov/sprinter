# Generated by Django 3.2.9 on 2021-12-21 18:18

import core.models.product
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0087_alter_rating_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(error_messages={'extension': 'File extension must be jpeg or jpg or png'}, upload_to=core.models.product.ProductImage.get_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])]),
        ),
    ]
