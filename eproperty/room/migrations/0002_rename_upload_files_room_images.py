# Generated by Django 4.1.7 on 2023-02-21 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='upload_files',
            new_name='images',
        ),
    ]
