# Generated by Django 4.1 on 2022-09-28 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_tasklist_is_finished_alter_tasklist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 28, 8, 39, 11, 38588, tzinfo=datetime.timezone.utc)),
        ),
    ]
