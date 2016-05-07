# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20160506_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('b', 'Blogger'), ('r', 'Reader')], default='b', max_length=1),
        ),
    ]