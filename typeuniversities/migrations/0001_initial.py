# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-16 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'TypeUniversity',
                'verbose_name_plural': 'TypesUniversities',
            },
        ),
    ]
