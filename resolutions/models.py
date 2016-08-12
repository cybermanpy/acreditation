from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Resolution(models.Model):
    number = models.IntegerField(blank=False);
    start_date = models.DateField()
    end_date = models.DateField()
    document = models.FileField(upload_to='resolutions/%Y_%m_%d/')

    def __str__(self):
        return '(%d)-%s' %(self.number, self.start_date)

    class Meta:
        verbose_name = 'Resolution'
        verbose_name_plural = 'Resolutions'
        ordering = ('id',)