# Generated by Django 3.2.9 on 2022-01-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220110_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
