# Generated by Django 3.2.16 on 2023-02-08 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bayashat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(default=datetime.date(2023, 2, 8)),
        ),
    ]
