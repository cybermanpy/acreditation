from __future__ import unicode_literals

from django.db import models
from resolutions.models import Resolution
from evaltypes.models import EvalType
from namecareers.models import NameCareer

# Create your models here.

class Evaluator(models.Model):
    firstname = models.CharField(blank=False, max_length=100, null=False)
    lastname = models.CharField(blank=False, max_length=100, null=False)
    fkresolution = models.ForeignKey(Resolution)
    curriculum = models.FileField(blank=True, upload_to='curriculum/%Y_%m_%d/')
    evaltypes = models.ManyToManyField(EvalType, through='TypeEvaluator')

    def __str__(self):
        return "%s %s" %(self.firstname, self.lastname)

    class Meta:
        verbose_name = 'Evaluator'
        verbose_name_plural = 'Evaluators'


class TypeEvaluator(models.Model):
    fkevaluator = models.ForeignKey(Evaluator)
    fkevaltype = models.ForeignKey(EvalType)
    fknamecareer = models.ForeignKey(NameCareer)

    def __str__(self):
        return "%s %s" %(self.fkevaluator, self.fkevaltype)

    class Meta:
        verbose_name = 'TypeEvaluator'
        verbose_name_plural = 'TypeEvaluators'
        ordering = ('id',)