# Generated by Django 4.2.6 on 2023-12-15 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminEnd', '0005_request_reps_db_ping_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_reps_db',
            old_name='ping_date',
            new_name='report_update',
        ),
    ]
