from django.db import models
from authentication.models import User
from helpers.models import TrackingModel

class Task(TrackingModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=None)
    complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title + ' - ' + self.description 
