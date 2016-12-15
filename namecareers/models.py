from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NameCareer(models.Model):
    description = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Name Career'
        verbose_name_plural = 'Name Careers'
        ordering = ('id',)