# Generated by Django 3.2.9 on 2021-12-26 08:00

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='core.ProductOrder'),
        ),
    ]
