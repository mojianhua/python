# Generated by Django 2.0.6 on 2019-09-06 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookManageAppp', '0004_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_book', to='BookManageAppp.Publisher'),
        ),
    ]