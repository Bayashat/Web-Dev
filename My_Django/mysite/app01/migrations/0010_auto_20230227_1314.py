# Generated by Django 3.2.16 on 2023-02-27 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20230226_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_Admin',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='last_login_time',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='register_time',
        ),
    ]