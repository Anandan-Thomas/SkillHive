# Generated by Django 4.2.6 on 2023-10-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkerEnd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker_db',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='worker_db',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
