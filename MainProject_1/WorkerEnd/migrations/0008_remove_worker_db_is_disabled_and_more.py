# Generated by Django 4.2.6 on 2023-12-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkerEnd', '0007_worker_db_is_disabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker_db',
            name='is_disabled',
        ),
        migrations.AddField(
            model_name='worker_login_db',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
