from django.contrib import admin

# Register your models here.
from .models import Pupil

admin.site.register(Pupil) # registers the model of pupil to the admin site

