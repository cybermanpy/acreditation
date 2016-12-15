from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EvalType(models.Model):
    description = models.CharField(blank=False, max_length=100, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'EvalType'
        verbose_name_plural = 'EvalTypes'
        ordering = ('id',)