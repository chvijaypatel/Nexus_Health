# Generated by Django 4.0.6 on 2022-07-12 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus_blog', '0003_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='publish_date',
        ),
    ]
