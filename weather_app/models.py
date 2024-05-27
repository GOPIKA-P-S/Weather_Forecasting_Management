
from django.db import models
# Create your models here.

class WeatherForecasting_Data(models.Model):
    Username=models.CharField(max_length=200)
    Email_id=models.EmailField(unique=True)
    Password=models.CharField(max_length=100)
    is_staff=models.BooleanField(default=True)
    city=models.CharField(max_length=300,verbose_name="City")
    timezone=models.DateTimeField(auto_now_add=True)
    #temperature=models.FloatField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status=models.CharField(max_length=40)
    
    def __str__(self):
        return self.Username

    




