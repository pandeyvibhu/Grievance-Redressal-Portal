
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import Grievance, Category
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from final import classify

# Create your views here.
@login_required
def home(request, tab_id):
	if request.user.username == "admin" :
		all_grievances = Grievance.objects.all().order_by('-date')[:10]
		return render(request, "main/admin.html", {		
		'list_of_grievances': all_grievances,
		'N' : 'N', 'R' : 'R', 'C' : 'C', 
		})
	else :
		grievances= Grievance.objects.get_grievances_for_user(request.user)
		return render(request, "main/home.html", {
		'tab_id': tab_id,
		'list_of_grievances': grievances,
		'N' : 'N', 'R' : 'R', 'C' : 'C',
		})


def index(request) :
	return home(request, '1')

def resolve(request, grievance_id):
	grievance= get_object_or_404(Grievance, pk=grievance_id)
	grievance.status='C'
	grievance.save()
	return HttpResponseRedirect(reverse('home', args=(2,)))

@require_POST
def read(request, grievance_id):
	grievance= get_object_or_404(Grievance, pk=grievance_id)
	grievance.status='R'
	grievance.save()
	return HttpResponseRedirect(reverse('home', args=(2,)))

@require_POST
def update(request, grievance_id):
	# print("Updatinf the categories ..")
	grievance= get_object_or_404(Grievance, pk=grievance_id)
	cgs= request.POST['categories']
	# print(cgs)
	cgs= cgs.split()
	for current in grievance.categories.all() :
		grievance.categories.remove(current)
		grievance.actions.remove(current.action)
		print("removing ",current.action)
	for new in cgs :
		category= Category.objects.get_category_for(new)
		grievance.categories.add(category.first())
		grievance.actions.add(category.first().action)
	grievance.save()
	return HttpResponseRedirect(reverse('home', args=(2,)))

@require_POST
def add_grievance(request):
	st= request.user.student
	desc= request.POST['description']
	# cgs= request.POST['categories']
	cgs= classify(desc).split(' ')
	print("The categories are: ", cgs)

	grievance= Grievance.objects.create(student= st, description= desc)
	# [TODO] categories to be detected using nlp
	for categ in cgs :
		print(categ)
		category= Category.objects.get_category_for(categ)
		print(category.first())	
		grievance.categories.add(category.first())
	# [TODO] categories have been guessed. Add actions based on the guessed categories to the grievance
	for categ in grievance.categories.all() :
		grievance.actions.add(categ.action)
	grievance.save()
	print(grievance, " : ", grievance.description, " of category ", grievance.categories.all())
	return HttpResponseRedirect(reverse('home', args=(2,)))

