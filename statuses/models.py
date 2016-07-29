from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Status(models.Model):
    description = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        ordering = ('id',)