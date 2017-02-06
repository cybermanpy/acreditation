from __future__ import unicode_literals

from django.db import models
from evaluators.models import TypesEvaluator
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

class Audit(models.Model):
    action = models.CharField(max_length=1)
    username = models.CharField(max_length=140)
    logs = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s" %(self.action)

    class Meta:
        verbose_name = 'Audit'
        verbose_name_plural = 'Audits'
        ordering = ('action',)

@receiver(user_logged_in)
def getUser(sender, user, request, **kwargs):
    logger = logging.getLogger(__name__)
    uname = logger.info('%s') %(user)
    # def getUser1():
    #     u = uname
    #     return u

@receiver(post_save, sender=TypesEvaluator)
def writeAuditTypesEvaluator(sender, **kwargs):
    if kwargs.get('created', False):
        action = 'c'
        up = kwargs.get('instance')
        username = 'admin'
        logs = up
        a = Audit(action=action, username=username, logs=logs)
        a.save()