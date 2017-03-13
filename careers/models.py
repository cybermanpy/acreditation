from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from faculties.models import Faculty
from statuses.models import Status
from resolutions.models import Resolution
from namecareers.models import NameCareer

# Create your models here.

class Career(models.Model):
    fknamecareer = models.ForeignKey(NameCareer)
    fkstatus = models.ForeignKey(Status)
    fkresolution = models.OneToOneField(Resolution)
    fkfaculty = models.ForeignKey(Faculty)
    fkuser = models.ForeignKey(User)
    national = models.IntegerField(blank=True, null=True)
    arcusur = models.BooleanField(blank=False, default=False)
    posgrado = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.fknamecareer.description

    class Meta:
        verbose_name = 'Carrer'
        verbose_name_plural = 'Careers'
        ordering = ('id',)