# Generated by Django 4.2.6 on 2023-12-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminEnd', '0003_request_reps_db_ping_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_reps_db',
            name='prof_resp_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='request_reps_db',
            name='prof_response',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
