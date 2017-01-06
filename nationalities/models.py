from __future__ import unicode_literals

from django.db import models

class Nationality(models.Model):
    origin = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return "%s" %(self.origin)

    class Meta:
        verbose_name = 'Nationality'
        verbose_name_plural = 'Nationalities'
        ordering = ('id', )