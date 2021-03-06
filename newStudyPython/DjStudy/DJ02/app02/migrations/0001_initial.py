# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-09-09 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Author2Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Author')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default='99.99', max_digits=5)),
                ('kuncun', models.IntegerField(default=1000)),
                ('maichu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('addr', models.CharField(default='广州市', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='back_book', to='app02.Publisher'),
        ),
        migrations.AddField(
            model_name='author2book',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(to='app02.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app02.AuthorDetial'),
        ),
    ]
