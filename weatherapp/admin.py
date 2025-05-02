from django.contrib import admin
from .models import WeatherSearch

@admin.register(WeatherSearch)
class WeatherSearchAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'description', 'search_date')
    list_filter = ('city', 'search_date')
    search_fields = ('city', 'description')
    ordering = ('-search_date',)
