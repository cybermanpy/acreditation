from __future__ import unicode_literals

from django.db import models
from departments.models import Department

# Create your models here.

class Campus(models.Model):
    name = models.CharField(blank=False, max_length=100)
    description = models.CharField(blank=False, max_length=100)
    fkdepartment = models.ForeignKey(Department)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = "Campuses"
        ordering = ('id',)