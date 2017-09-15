# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models

class User(models.Model): 
    name = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    mobile = models.CharField(max_length=11, blank=True)
    #amount = models.IntField(default=1, required=True) models.BigIntegerField()
    comments = models.CharField(max_length=30, blank=True)

    def __str__(self): 
        return "%s: %s --> %s" % (self.name, self.amount, self.amount * 0.025)

class UserProfile(models.Model):  
#class Total(models.Model):  
  
    user = models.OneToOneField(User)  
    name = models.CharField(max_length=32)  
  
    def __unicode__(self):  
        return self.name  
