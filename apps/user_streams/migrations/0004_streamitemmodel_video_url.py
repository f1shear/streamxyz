# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_streams', '0003_auto_20170929_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamitemmodel',
            name='video_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
