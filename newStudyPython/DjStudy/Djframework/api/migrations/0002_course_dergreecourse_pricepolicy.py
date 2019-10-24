# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-15 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='DergreeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pirce', models.IntegerField()),
                ('object_id', models.IntegerField(verbose_name='关联表的数据ID')),
                ('table_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='关联表的名称')),
            ],
        ),
    ]