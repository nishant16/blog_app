# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 15:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateField(default=datetime.datetime(2017, 8, 19, 15, 58, 48, 962156, tzinfo=utc)),
        ),
    ]
