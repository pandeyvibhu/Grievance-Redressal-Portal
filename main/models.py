
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
STATUS_CHOICES= (
	('N','Not read'),
	('R', 'Read'),
	('C', 'Complete'))

HOSTEL_CHOICES= (
	('C.V. Raman', 'C.V. Raman'),
	)

class Action(models.Model):
	description= models.CharField(max_length=500)
	def __str__(self):
		return self.description

class CategoryManager(models.Manager):
	def get_category_for(self, category_name):
		return super(CategoryManager, self).get_queryset().filter(name=category_name)

class Category(models.Model):
	name= models.CharField(max_length=100)
	hostel= models.CharField(max_length=100,choices=HOSTEL_CHOICES)
	action= models.OneToOneField(Action, null=True)
	objects= CategoryManager()
	def __str__(self):
		return "category : %s" % self.name

class Student(models.Model):
	name= models.CharField(max_length=100)
	department= models.CharField(max_length=100)
	hostel= models.CharField(max_length=100, choices=HOSTEL_CHOICES)
	user= models.OneToOneField(User, null=True)

	def __str__(self):
		return "name : %s" % self.name

class GrievanceManager(models.Manager):
	def get_grievances_for_user(self, user):
		return super(GrievanceManager, self).get_queryset().filter(student=user.student).order_by('-date')	

class Grievance(models.Model):
	student= models.ForeignKey(Student, on_delete= models.CASCADE)
	date= models.DateTimeField(auto_now_add=True)
	description= models.CharField(max_length=1000)
	status= models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
	categories= models.ManyToManyField(Category)	
	actions= models.ManyToManyField(Action)
	objects= GrievanceManager()

	def get_date(self):
		return self.date.strftime('%d %b, %Y') 

	def __str__(self):
		return "Grievance by %s on %s " % (self.student.name, self.date.strftime('%d %b, %Y'))
