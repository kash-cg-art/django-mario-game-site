# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-01 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20180930_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='mails',
            fields=[
                ('name', models.AutoField(primary_key=True, serialize=False)),
                ('person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
