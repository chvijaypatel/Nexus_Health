# Generated by Django 4.0.5 on 2022-07-09 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0023_delete_appointment_delete_appointment_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
                ('header_image', models.ImageField(upload_to='Header/Appointment_Page_Img')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phoneno', models.IntegerField()),
                ('message', models.TextField()),
                ('appointment_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_health.appointment_page')),
            ],
        ),
    ]