# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 00:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0004_auto_20160418_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='virtualmachinetype',
            old_name='cores_price',
            new_name='core_price',
        ),
    ]
