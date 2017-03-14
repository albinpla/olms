from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User)
    dept=( 
        ('cs','Computer Science'),
        ('EC','Electronics and Communication'),
        ('EEE','Electrical and Electronic'),
        ('Mech','Mechanical'),
        ('BE','Biomedial'),
        ('AS','Applied Science'),
        ('NT','Non-Teching')
        )
    department = models.CharField(max_length=4,choices=dept,default='NT')
    Tflag = models.BooleanField(default=False)

    def _str_(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username   

class department(models.Model):
    depart=models.CharField(max_length=4,primary_key=True)
    hod = models.OneToOneField(User)

    def _str_(self):
        return self.department

    def __unicode__(self):
        return self.department

class leave_history(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    startdate = models.DateField(auto_now_add = False,auto_now=True)
    enddate = models.DateField(auto_now_add = False,auto_now=True)
    choices=(
        ('cl','casual leave'),
        ('hp','half paid')
        )
    leavetype = models.CharField(max_length=20,choices=choices)
    status = models.BooleanField(default=False)
    des = models.CharField(max_length=300)
    half_day = models.IntegerField()

    def _str_(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username       

class leave_statistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    casual = models.IntegerField()
    vacation = models.IntegerField()
    conpens = models.IntegerField()
    earned = models.IntegerField()
    half_paid = models.IntegerField()

    def _str_(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username   
