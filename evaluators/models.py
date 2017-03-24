from __future__ import unicode_literals

from django.db import models
from resolutions.models import Resolution
from typeevaluators.models import TypeEvaluator
from namecareers.models import NameCareer
from statuses.models import Status
from nationalities.models import Nationality
from universities.models import University

# Create your models here.

class Evaluator(models.Model):
    firstname = models.CharField(blank=False, max_length=100, null=False)
    lastname = models.CharField(blank=False, max_length=100, null=False)
    ci = models.IntegerField(blank=False, null=False, unique=True)
    email = models.EmailField(max_length=140, blank=False, null=False, unique=True)
    curriculum = models.FileField(blank=True, upload_to='curriculums/%Y_%m_%d/')
    typesevaluators = models.ManyToManyField(TypeEvaluator, through='TypesEvaluator')
    fkstatus = models.ForeignKey(Status)
    fknationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    conflict = models.ManyToManyField(University, through='EvaluatorUniversity')

    def __str__(self):
        return "%s %s" %(self.firstname, self.lastname)

    class Meta:
        verbose_name = 'Evaluator'
        verbose_name_plural = 'Evaluators'
        ordering = ('ci', )

    def _get_full_name(self):
        return "%s %s" %(self.firstname, self.lastname)
    fullname = property(_get_full_name)

class TypesEvaluator(models.Model):
    fkevaluator = models.ForeignKey(Evaluator, on_delete=models.CASCADE)
    fktypeevaluator = models.ForeignKey(TypeEvaluator, on_delete=models.CASCADE)
    fknamecareer = models.ForeignKey(NameCareer, on_delete=models.CASCADE)
    fkresolution = models.ForeignKey(Resolution, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" %(self.fkevaluator, self.fktypeevaluator)

    class Meta:
        unique_together = ('fkevaluator', 'fktypeevaluator', 'fknamecareer')
        verbose_name = 'Type Evaluator'
        verbose_name_plural = 'Types Evaluators'
        ordering = ('fknamecareer__description',)

class EvaluatorUniversity(models.Model):
    fkevaluator = models.ForeignKey(Evaluator, on_delete=models.CASCADE)
    fkuniversity = models.ForeignKey(University, on_delete=models.CASCADE)
    start_job = models.DateField(blank=False, null=False)
    end_job = models.DateField(blank=False, null=False)
    reason = models.TextField(blank=False, null=False)
    doc = models.FileField(blank=True, upload_to='declarations/%Y_%m_%d/')

    def __str__(self):
        return "%s %s" %(self.fkevaluator, self.fkuniversity)

    class Meta:
        unique_together = ('fkevaluator', 'fkuniversity', 'start_job')
        verbose_name = 'Evaluator / University'
        verbose_name_plural = 'Evaluators / Universities'
        ordering = ('fkuniversity__name', )