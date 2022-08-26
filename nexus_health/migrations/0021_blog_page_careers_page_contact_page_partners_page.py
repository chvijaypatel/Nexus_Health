# Generated by Django 4.0.5 on 2022-07-09 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0020_appointment_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
                ('header_image', models.ImageField(upload_to='Header/Blog_Page_Img')),
            ],
        ),
        migrations.CreateModel(
            name='Careers_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
                ('header_image', models.ImageField(upload_to='Header/Careers_Page_Img')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
                ('header_image', models.ImageField(upload_to='Header/Contact_Page_Img')),
            ],
        ),
        migrations.CreateModel(
            name='Partners_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=200)),
                ('header_image', models.ImageField(upload_to='Header/Partners_Page_Img')),
            ],
        ),
    ]
