# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0005_auto_20180126_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='comment',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
