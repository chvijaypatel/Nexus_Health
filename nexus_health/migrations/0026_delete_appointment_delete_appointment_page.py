# Generated by Django 4.0.5 on 2022-07-09 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0025_alter_appointment_phoneno'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Appointment_Page',
        ),
    ]