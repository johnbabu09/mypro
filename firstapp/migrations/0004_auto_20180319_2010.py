# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-20 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_student_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date_time',
            new_name='date',
        ),
    ]
