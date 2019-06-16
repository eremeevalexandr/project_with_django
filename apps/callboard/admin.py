from django.contrib import admin
from .models import Category, Adverts
from django_mptt_admin.admin import DjangoMpttAdmin

# Register your models here.

admin.site.register(Category, DjangoMpttAdmin)
admin.site.register(Adverts)