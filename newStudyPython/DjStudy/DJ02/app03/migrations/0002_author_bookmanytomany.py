# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-09 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bookManyToMany',
            field=models.ManyToManyField(related_name='bookManyToMany', through='app03.Author2Book', to='app03.Book'),
        ),
    ]
