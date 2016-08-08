from __future__ import unicode_literals

from django.db import models
from universities.models import University
from campuses.models import Campus
# Create your models here.

class Faculty(models.Model):
    name = models.CharField(blank=False, max_length=100)
    fkuniversity = models.ForeignKey(University)
    fkcampus = models.ForeignKey(Campus)

    # def __str__(self):
    #     return '%s' %(self.name)

    def __str__(self):
        return '%s - %s' %(self.name, self.fkuniversity)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ('id',)