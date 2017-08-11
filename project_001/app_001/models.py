# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from django.db import models

# Create your models here.

class User(models.Model): 
    name = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    mobile = models.CharField(max_length=11, blank=True)
    #amount = models.IntField(default=1, required=True) models.BigIntegerField()
    comments = models.CharField(max_length=30, blank=True)

    def __str__(self): 
        return "%s" % self.name
