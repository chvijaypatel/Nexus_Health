# Generated by Django 4.0.6 on 2022-07-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0008_delete_services_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]