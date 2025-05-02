from django.db import models
from django.utils import timezone

# Create your models here.

class WeatherSearch(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    pressure = models.IntegerField()
    search_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.city} - {self.search_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-search_date']
