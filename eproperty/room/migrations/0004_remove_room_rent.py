# Generated by Django 4.1.7 on 2023-02-21 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_room_rent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='rent',
        ),
    ]
