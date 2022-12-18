from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Items)
class AdminRoom(admin.ModelAdmin):
    list_display = ('name', 'user','created_at')