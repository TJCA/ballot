from django.contrib import admin

from .models import Athlete


class AthleteAdmin(admin.ModelAdmin):
    list_display = ['number', 'name']

admin.site.register(Athlete, AthleteAdmin)
