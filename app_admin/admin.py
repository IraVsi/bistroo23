from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)  # Admin page show category model
admin.site.register(MenuHeadlines)  # Admin page show Menüü pealkirjad  modelist
# admin.site.register(ToiduNimed)  # Admin page show Menüü pealkirjad modelist
admin.site.register(FoodMenu)
admin.site.register(FoodItem)