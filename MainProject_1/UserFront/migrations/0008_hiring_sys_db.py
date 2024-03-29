# Generated by Django 4.2.6 on 2023-12-03 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WorkerEnd', '0005_worker_db_dob'),
        ('UserFront', '0007_user_feedback_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiring_sys_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_sub', models.CharField(blank=True, max_length=100, null=True)),
                ('o_desc', models.TextField(blank=True, max_length=500, null=True)),
                ('o_date', models.DateField(blank=True, null=True)),
                ('o_status', models.CharField(blank=True, max_length=50, null=True)),
                ('o_completion', models.BooleanField(default=False)),
                ('user_name', models.CharField(blank=True, max_length=120, null=True)),
                ('prof_name', models.CharField(blank=True, max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ord_usr', to='UserFront.user_reg_db')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ord_wrk', to='WorkerEnd.worker_db')),
            ],
        ),
    ]
