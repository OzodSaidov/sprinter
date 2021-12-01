# Generated by Django 3.2.9 on 2021-12-01 08:37

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_color_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='core.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='productorder',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.productcolor'),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
