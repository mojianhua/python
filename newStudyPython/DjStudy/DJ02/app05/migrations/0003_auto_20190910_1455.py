# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-10 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app05', '0002_dept_employeenew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeenew',
            old_name='did',
            new_name='dept',
        ),
    ]
