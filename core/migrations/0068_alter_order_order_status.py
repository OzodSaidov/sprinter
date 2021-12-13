# Generated by Django 3.2.9 on 2021-12-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_alter_productcolor_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Opened', 'Opened'), ('Cancelled', 'Cancelled'), ('Approved', 'Approved'), ('Declined', 'Declined'), ('Delivering', 'Delivering'), ('Completed', 'Completed')], default='Opened', max_length=255),
        ),
    ]