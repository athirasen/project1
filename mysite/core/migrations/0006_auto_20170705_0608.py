# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170705_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sub1',
            field=models.BooleanField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub2',
            field=models.BooleanField(max_length=10),
        ),
    ]