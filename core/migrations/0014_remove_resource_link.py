# Generated by Django 3.2.4 on 2022-04-12 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_submission_resubmitted_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='link',
        ),
    ]