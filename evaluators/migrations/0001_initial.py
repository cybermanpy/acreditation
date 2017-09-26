# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-06 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resolutions', '0005_auto_20160729_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('curriculum', models.FileField(upload_to='curriculum/%Y_%m_%d/')),
                ('fkresolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resolutions.Resolution')),
            ],
            options={
                'verbose_name': 'Evaluator',
                'verbose_name_plural': 'Evaluators',
            },
        ),
    ]
