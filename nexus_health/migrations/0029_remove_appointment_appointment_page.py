# Generated by Django 4.0.6 on 2022-07-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0028_alter_appointment_dayofweek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_page',
        ),
    ]
