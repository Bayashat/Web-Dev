# Generated by Django 3.2.16 on 2023-02-26 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_department_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_login_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='register_time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]