# Generated by Django 4.1.7 on 2023-02-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='booking_days',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, choices=[('AA', 'AA'), ('BB', 'BB'), ('CC', 'CC')], max_length=30, null=True),
        ),
    ]
