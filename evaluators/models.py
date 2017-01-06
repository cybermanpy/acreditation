from __future__ import unicode_literals

from django.db import models
from resolutions.models import Resolution
from typeevaluators.models import TypeEvaluator
from namecareers.models import NameCareer
from statuses.models import Status
from nationalities.models import Nationality

# Create your models here.

class Evaluator(models.Model):
    firstname = models.CharField(blank=False, max_length=100, null=False)
    lastname = models.CharField(blank=False, max_length=100, null=False)
    fkresolution = models.ForeignKey(Resolution)
    ci = models.IntegerField(blank=False, null=False, unique=True)
    email = models.EmailField(max_length=140, blank=False, null=False, unique=True)
    curriculum = models.FileField(blank=True, upload_to='curriculums/%Y_%m_%d/')
    typesevaluators = models.ManyToManyField(TypeEvaluator, through='TypesEvaluator')
    fkstatus = models.ForeignKey(Status)
    fknationality = models.ForeignKey(Nationality)

    def __str__(self):
        return "%s %s" %(self.firstname, self.lastname)

    class Meta:
        verbose_name = 'Evaluator'
        verbose_name_plural = 'Evaluators'
        ordering = ('id', )

class TypesEvaluator(models.Model):
    fkevaluator = models.ForeignKey(Evaluator)
    fktypeevaluator = models.ForeignKey(TypeEvaluator)
    fknamecareer = models.ForeignKey(NameCareer)

    def __str__(self):
        return "%s %s" %(self.fkevaluator, self.fktypeevaluator)

    class Meta:
        verbose_name = 'Type Evaluator'
        verbose_name_plural = 'Types Evaluators'
        ordering = ('id',)