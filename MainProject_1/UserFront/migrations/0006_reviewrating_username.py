# Generated by Django 4.2.6 on 2023-11-23 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserFront', '0005_alter_reviewrating_user_alter_reviewrating_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]