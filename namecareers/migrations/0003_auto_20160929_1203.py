# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-29 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('namecareers', '0002_auto_20160811_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='namecareer',
            options={'ordering': ('id',), 'verbose_name': 'Name Career', 'verbose_name_plural': 'Name Careers'},
        ),
    ]
