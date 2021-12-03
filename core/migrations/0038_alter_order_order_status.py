# Generated by Django 3.2.9 on 2021-12-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_alter_productprice_param'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Opened', 'Opened'), ('Ordered', 'Ordered'), ('Approved', 'Approved'), ('Declined', 'Declined'), ('Cancelled', 'Cancelled'), ('Delivering', 'Delivering'), ('Completed', 'Completed')], default='Opened', max_length=255),
        ),
    ]
