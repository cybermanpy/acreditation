# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'ordering': ('id',), 'verbose_name': 'University', 'verbose_name_plural': 'Universities'},
        ),
    ]
