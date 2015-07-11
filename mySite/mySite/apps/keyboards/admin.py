from django.contrib import admin

# Register your models here.

from django.contrib import admin
from mySite.apps.keyboards.models import Keyboard

admin.site.register(Keyboard)
