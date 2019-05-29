# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-30 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180930_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='fid',
        ),
        migrations.AddField(
            model_name='feedback',
            name='id',
            field=models.AutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='account',
        ),
    ]