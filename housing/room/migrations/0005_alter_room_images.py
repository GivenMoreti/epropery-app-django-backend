# Generated by Django 4.1.3 on 2023-02-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_alter_room_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='images',
            field=models.CharField(blank=True, max_length=8000),
        ),
    ]