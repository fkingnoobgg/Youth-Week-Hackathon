from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']

    @admin.register(HTUser)
    class HTUserAdmin(admin.ModelAdmin):
        list_display = ['user','activation_key']

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['user','name','description','votes_up','votes_down','longitude','latitude','time_created','time_modified']
    list_filter = ['time_created','time_modified']
