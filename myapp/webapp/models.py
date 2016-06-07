from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserCategory(models.Model):
    name = models.CharField(primary_key=True, max_length=128, unique=True)
    description = models.CharField(max_length=1024)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    category = models.ForeignKey(UserCategory)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.fname + self.lname
    
class VisitorLog(models.Model):
    LogId = models.AutoField(primary_key=True)
    UserToVisit = models.ForeignKey(User)
    category = models.ForeignKey(UserCategory)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    
    