# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 08:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_collections', '0009_auto_20170930_0655'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='collectionitemmodel',
            unique_together=set([('collection', 'order_index')]),
        ),
    ]
