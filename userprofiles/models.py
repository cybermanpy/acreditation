from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    level = models.CharField(max_length=140, blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)
    profiles = models.ManyToManyField(User, through='UserProfile', related_name='user_profile')

    def __str__(self):
        return "%s" %(self.level)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ('id', )

class UserProfile(models.Model):
    fkuser = models.ForeignKey(User, on_delete=models.CASCADE)
    fkprofile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__ (self):
        return "%s" %(self.fkuser)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'
        ordering = ('id', )