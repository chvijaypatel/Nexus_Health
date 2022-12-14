# Generated by Django 4.0.6 on 2022-07-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0041_job_application_forms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Now',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phoneno', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact_Page',
        ),
    ]
