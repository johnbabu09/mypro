# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-20 02:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20180223_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 20, 2, 40, 32, 848000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]