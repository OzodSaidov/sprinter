# Generated by Django 3.2.9 on 2021-12-03 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_merge_0033_alter_order_basket_0034_alter_order_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='core.productparam'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='core.product'),
        ),
    ]