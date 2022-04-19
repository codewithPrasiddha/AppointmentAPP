from django.db import models
from datetime import datetime
# Create your models here.
from api.models import User

class Rating(models.Model):
    rating = models.IntegerField()
    doctor= models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    
class Appointment(models.Model):
    client_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='appointment_client_id')

    doctor_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='appointment_doctor_id')
    date = models.DateField(null=False)
    time = models.TimeField(null=False)

    status = models.BooleanField(default=False)
