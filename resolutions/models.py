from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Resolution(models.Model):
    number = models.IntegerField(blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    document = models.FileField(upload_to='resolutions/%Y_%m_%d/')

    def __str__(self):
        return '(%d)-%s' %(self.number, self.start_date)

    class Meta:
        verbose_name = 'Resolution'
        verbose_name_plural = 'Resolutions'
        ordering = ('id',)

    def _get_term(self):
        return "%s / %s" %(self.start_date, self.end_date)

    def _get_date(self):
        return "%s" %(self.start_date)

    def _format_date(self):
        format = ('%Y')
        return self.start_date.strftime(format)
    
    years = property(_format_date)
    term = property(_get_term)