# Generated by Django 4.1.7 on 2023-02-25 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_agent_rename_type_room_room_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.agent'),
        ),
    ]