# Generated by Django 3.2.9 on 2021-12-01 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20211201_0839'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewFileAttachment',
            new_name='ReviewAttachment',
        ),
    ]