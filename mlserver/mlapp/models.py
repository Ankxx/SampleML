from django.db import models
# Create your models here.

from django.utils import timezone


class Predict(models.Model):
    originLocation = models.CharField(max_length=200)
    destinationLocation = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.save()

    def __str__(self):
        return "Predictions for route {} to {}".format(self.originLocation, self.destinationLocation)