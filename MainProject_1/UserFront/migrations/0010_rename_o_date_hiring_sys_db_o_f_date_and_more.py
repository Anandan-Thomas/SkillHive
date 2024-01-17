# Generated by Django 4.2.6 on 2023-12-10 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserFront', '0009_alter_hiring_sys_db_o_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiring_sys_db',
            old_name='o_date',
            new_name='o_f_date',
        ),
        migrations.AddField(
            model_name='hiring_sys_db',
            name='o_fixed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hiring_sys_db',
            name='o_l_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='rej_rs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=True, max_length=300, null=True)),
                ('rej_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rej_order', to='UserFront.hiring_sys_db')),
            ],
        ),
    ]