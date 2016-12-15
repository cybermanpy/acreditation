from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Deparments'
        ordering = ('id',)