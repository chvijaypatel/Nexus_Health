# Generated by Django 4.0.6 on 2022-07-08 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0013_opening_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
                ('header_image', models.ImageField(upload_to='Header/About_Img')),
            ],
        ),
        migrations.CreateModel(
            name='Mission_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='About_Img')),
                ('paragraph', models.CharField(max_length=1000)),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_health.about_us')),
            ],
        ),
        migrations.CreateModel(
            name='Care_Provider_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('paragraph', models.TextField(max_length=1000)),
                ('team_member_photo', models.ImageField(upload_to='About_Img/Team_Care_Provider_Img')),
                ('team_member_name', models.CharField(max_length=200)),
                ('department_name', models.CharField(max_length=200)),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_health.about_us')),
            ],
        ),
        migrations.CreateModel(
            name='About_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='About_Img')),
                ('paragraph', models.CharField(max_length=1000)),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nexus_health.about_us')),
            ],
        ),
    ]
