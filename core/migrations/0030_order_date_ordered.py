# Generated by Django 3.2.9 on 2021-12-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_rename_reviewattachment_reviewimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(blank=True, null=True),
        ),
    ]
