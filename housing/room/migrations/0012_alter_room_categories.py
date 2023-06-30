# Generated by Django 4.1.3 on 2023-02-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_alter_room_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='categories',
            field=models.CharField(choices=[('vacant_land', 'land'), ('House', 'House'), ('Farm', 'Farm'), ('Apartment', 'Apartment'), ('Student', 'Student'), ('Industrial', 'Industrial'), ('Townhouse', 'Townhouse')], max_length=300),
        ),
    ]
