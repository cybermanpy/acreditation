# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-19 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluators', '0003_auto_20161216_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluator',
            name='curriculum',
            field=models.FileField(blank=True, upload_to='curriculums/%Y_%m_%d/'),
        ),
    ]
