# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolutions', '0002_auto_20160729_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolution',
            name='document',
            field=models.ImageField(upload_to='media/resolutions/'),
        ),
    ]
