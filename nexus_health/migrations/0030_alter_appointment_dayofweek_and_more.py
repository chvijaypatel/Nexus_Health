# Generated by Django 4.0.6 on 2022-07-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0029_remove_appointment_appointment_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dayofweek',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='timeofday',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='waytoreach',
            field=models.CharField(max_length=200),
        ),
    ]