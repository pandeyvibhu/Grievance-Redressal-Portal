
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from main.models import Student, Grievance, Category, Action

# Register your models here.
admin.site.register(Student)
admin.site.register(Grievance)
admin.site.register(Category)
admin.site.register(Action)
