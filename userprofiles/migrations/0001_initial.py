# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-04 12:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=140)),
                ('number', models.IntegerField()),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'Users Profiles',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Profile')),
                ('fkuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='profiles',
            field=models.ManyToManyField(through='userprofiles.UserProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
