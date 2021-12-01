# Generated by Django 3.2.9 on 2021-12-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_address_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Moderator', 'Moderator'), ('User', 'User')], default='User', max_length=255),
        ),
    ]