# Generated by Django 4.0.5 on 2022-07-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0019_resources_page_resources_detail'),
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
    ]