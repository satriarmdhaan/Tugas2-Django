# Generated by Django 4.1 on 2022-09-28 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_alter_tasklist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 28, 16, 21, 43, 785516, tzinfo=datetime.timezone.utc)),
        ),
    ]
