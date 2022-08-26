# Generated by Django 4.0.6 on 2022-07-10 12:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_health', '0034_alter_appointment_dayofweek_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dayofweek',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], default=2, max_length=100),
            preserve_default=False,
        ),
    ]