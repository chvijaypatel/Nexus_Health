# Generated by Django 4.0.6 on 2022-07-15 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_blog', '0020_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]