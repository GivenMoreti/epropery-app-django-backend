# Generated by Django 4.1.7 on 2023-02-21 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_alter_customer_booking_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='booking_days',
            field=models.DateTimeField(default=datetime.date(2023, 2, 21)),
        ),
    ]