# Generated by Django 4.1 on 2022-09-28 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_tasklist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 28, 15, 33, 33, 4893)),
        ),
    ]
