# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_course_dergreecourse_pricepolicy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricepolicy',
            old_name='table_name',
            new_name='content_type',
        ),
    ]
