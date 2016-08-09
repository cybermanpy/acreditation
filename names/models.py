from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Name(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
        ordering = ('id',)