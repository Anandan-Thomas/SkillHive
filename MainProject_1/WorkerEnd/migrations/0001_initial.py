# Generated by Django 4.2.6 on 2023-10-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='worker_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('desc', models.CharField(blank=True, max_length=400, null=True)),
                ('skill', models.CharField(blank=True, max_length=400, null=True)),
                ('mobile', models.CharField(blank=True, max_length=400, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='workers_pic')),
            ],
        ),
    ]
