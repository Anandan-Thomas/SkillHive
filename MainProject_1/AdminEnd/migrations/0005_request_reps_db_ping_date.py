# Generated by Django 4.2.6 on 2023-12-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminEnd', '0004_request_reps_db_prof_resp_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_reps_db',
            name='ping_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
