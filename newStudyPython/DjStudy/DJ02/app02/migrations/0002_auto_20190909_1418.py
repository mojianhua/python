# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-09 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author2book',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='author2book',
            old_name='book_id',
            new_name='book',
        ),
    ]
