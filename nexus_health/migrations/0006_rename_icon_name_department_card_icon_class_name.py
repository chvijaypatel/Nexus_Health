# Generated by Django 4.0.6 on 2022-07-06 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0005_department_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department_card',
            old_name='icon_name',
            new_name='icon_class_name',
        ),
    ]
