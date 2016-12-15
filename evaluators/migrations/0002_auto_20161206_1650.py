# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-06 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaltypes', '0001_initial'),
        ('namecareers', '0003_auto_20160929_1203'),
        ('evaluators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeEvaluator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkevaltype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaltypes.EvalType')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'TypeEvaluator',
                'verbose_name_plural': 'TypeEvaluators',
            },
        ),
        migrations.AlterField(
            model_name='evaluator',
            name='curriculum',
            field=models.FileField(blank=True, upload_to='curriculum/%Y_%m_%d/'),
        ),
        migrations.AddField(
            model_name='typeevaluator',
            name='fkevaluator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluators.Evaluator'),
        ),
        migrations.AddField(
            model_name='typeevaluator',
            name='fknamecareer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='namecareers.NameCareer'),
        ),
        migrations.AddField(
            model_name='evaluator',
            name='types',
            field=models.ManyToManyField(through='evaluators.TypeEvaluator', to='evaltypes.EvalType'),
        ),
    ]