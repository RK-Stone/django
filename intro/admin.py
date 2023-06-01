from django.contrib import admin
# Register your models here.
from . import models
# python manage.py makemigrations
admin.site.register(models.Intro)
admin.site.register(models.Category)
admin.site.register(models.Tag)
