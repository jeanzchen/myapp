from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class UserCategory(models.Model):
    name = models.CharField(primary_key=True, max_length=128, unique=True)
    description = models.CharField(max_length=1024)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class SiteUser(models.Model):
    UserId = models.AutoField(primary_key=True)
    category = models.ForeignKey(UserCategory)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    empid = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    dept = models.CharField(max_length=128)
    comment = models.CharField(max_length=128)
    nowtime = models.DateTimeField(default=datetime.now())

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.fname + self.lname + self.empid + self.phone + self.email + self.dept + self.comment 
    
class Activity(models.Model):
    UserId = models.AutoField(primary_key=True)
    category = models.ForeignKey(UserCategory)
    try:
        fname = models.CharField(max_length=128)
        lname = models.CharField(max_length=128)
              
        ACTIVITY_CHOICES =(
            ('1', 'Gym Usage'), 
            ('2', 'Weight Reduce'), 
            ('3', 'Yoga'),                 
        )
    
        acttype = models.CharField(max_length=1, choices = ACTIVITY_CHOICES) 
    except ValueError as v:
        pass
           
class VisitorLog(models.Model):
    LogId = models.AutoField(primary_key=True)
    UserToVisit = models.ForeignKey(SiteUser)
    category = models.ForeignKey(UserCategory)
    fname = models.CharField(max_length=128, null=True)
    lname = models.CharField(max_length=128, null=True) 
    phone = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)
    dept = models.CharField(max_length=128, null=True)
    comment = models.CharField(max_length=128, null=True)
    nowtime = models.DateTimeField(default=datetime.now())#define field waktu/time
      
    try:
        #choice
        ACTIVITY_CHOICES =(
            ('1', 'Gym Usage'), 
            ('2', 'Weight Reduce'), 
            ('3', 'Yoga'),                 
        )
    
        acttype = models.CharField(max_length=1, choices = ACTIVITY_CHOICES, default="1") 
    except ValueError as v:
        pass
    