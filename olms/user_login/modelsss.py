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