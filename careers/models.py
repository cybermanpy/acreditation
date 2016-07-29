from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from faculties.models import Faculty
from statuses.models import Status
from resolutions.models import Resolution

# Create your models here.

class Career(models.Model):
    name = models.CharField(blank=False, max_length=100)
    fkstatus = models.ForeignKey(Status)
    fkresolution = models.OneToOneField(Resolution)
    fkfaculty = models.ForeignKey(Faculty)
    fkuser = models.ForeignKey(User)
    national = models.IntegerField(blank=False)
    career = models.IntegerField(blank=False)
    university = models.IntegerField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Carrer'
        verbose_name_plural = 'Careers'
        ordering = ('id',)