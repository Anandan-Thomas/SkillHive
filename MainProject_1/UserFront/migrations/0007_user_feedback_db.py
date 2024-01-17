# Generated by Django 4.2.6 on 2023-11-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserFront', '0006_reviewrating_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_feedback_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, max_length=100, null=True)),
                ('l_name', models.CharField(blank=True, max_length=100, null=True)),
                ('em', models.CharField(blank=True, max_length=100, null=True)),
                ('mbl', models.IntegerField(blank=True, null=True)),
                ('sub', models.CharField(blank=True, max_length=140, null=True)),
                ('msg', models.TextField(blank=True, max_length=500, null=True)),
                ('fb_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]