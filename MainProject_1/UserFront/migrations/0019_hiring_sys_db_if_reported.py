# Generated by Django 4.2.6 on 2023-12-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserFront', '0018_rename_user_message_db_sender_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiring_sys_db',
            name='if_reported',
            field=models.BooleanField(default=False),
        ),
    ]
