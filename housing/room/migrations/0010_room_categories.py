# Generated by Django 4.1.3 on 2023-02-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_alter_room_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='categories',
            field=models.CharField(choices=[('vacant_land', 'land'), ('House', 'House'), ('Farm', 'Farm'), ('Apartment', 'Apartment'), ('Student', 'Student'), ('Industrial', 'Industrial'), ('Townhouse', 'Townhouse')], default=None, max_length=300),
        ),
    ]