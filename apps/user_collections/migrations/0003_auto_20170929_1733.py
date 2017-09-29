# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_collections', '0002_auto_20170929_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionitemmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectionitemmodel',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
