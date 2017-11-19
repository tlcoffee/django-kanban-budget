# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20171117_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True, help_text='HTML url for repository', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='github_url',
            field=models.URLField(blank=True, editable=False, null=True, unique=True),
        ),
    ]