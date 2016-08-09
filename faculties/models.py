from __future__ import unicode_literals

from django.db import models
from universities.models import University
from campuses.models import Campus
from names.models import Name
# Create your models here.

class Faculty(models.Model):
    fkname = models.ForeignKey(Name)
    fkuniversity = models.ForeignKey(University)
    fkcampus = models.ForeignKey(Campus)

    # def __str__(self):
    #     return '%s' %(self.name)

    def __str__(self):
        return '%s-%s-%s' %(self.fkname, self.fkuniversity, self.fkcampus)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ('id',)