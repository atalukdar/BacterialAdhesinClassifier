# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adhesin', '0005_auto_20160623_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='pub_date',
            field=models.CharField(default=b'06_24_', max_length=12),
        ),
        migrations.AlterField(
            model_name='proteindata',
            name='pub_date',
            field=models.CharField(default=b'06_24_', max_length=10),
        ),
    ]