# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-23 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stusent_name',
            new_name='student_name',
        ),
    ]
