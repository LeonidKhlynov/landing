# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 04:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(max_length=150)),
                ('about', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='type_of_work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='landingpage.Work'),
        ),
    ]
