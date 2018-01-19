# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-17 06:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_auto_20180117_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='parentid',
        ),
        migrations.RemoveField(
            model_name='tech',
            name='studenti',
        ),
        migrations.AddField(
            model_name='tech',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tech',
            name='compname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tech',
            name='room',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]