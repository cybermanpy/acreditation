from __future__ import unicode_literals

from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
    	return self.name

    class Meta:
    	verbose_name = 'University'
    	verbose_name_plural = 'Universities'
    	ordering = ('id',)