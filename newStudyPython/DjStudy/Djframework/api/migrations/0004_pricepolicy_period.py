# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191015_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricepolicy',
            name='period',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
