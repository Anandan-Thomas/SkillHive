# Generated by Django 4.2.6 on 2023-12-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminEnd', '0002_request_reps_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_reps_db',
            name='ping_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='request_reps_db',
            name='waiver_black',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
