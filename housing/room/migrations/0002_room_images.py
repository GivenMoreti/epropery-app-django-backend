# Generated by Django 4.1.3 on 2023-02-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='images',
            field=models.CharField(default=None, max_length=8000),
        ),
    ]