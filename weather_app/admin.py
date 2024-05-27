
from django.contrib import admin
from .models import  WeatherForecasting_Data

# Register your models here.
class WeatherForecasting_DataAdmin(admin.ModelAdmin):
    list_display=('Username','city','timezone','temperature','status')

admin.site.register(WeatherForecasting_Data,WeatherForecasting_DataAdmin)






