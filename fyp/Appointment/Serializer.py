
from http import client
from rest_framework import serializers
from Appointment.models import Appointment, Rating
from datetime import datetime

from api.models import User


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('__all__')


class AppointmentSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Appointment

        fields = ('__all__')
        
    
    # def __init__(self, *args, **kwargs):
    #     super(AppointmentSerializer, self).__init__(*args, **kwargs)
    #     request=self.context.get('request')
    #     if request and request.method =='POST':
    #         self.Meta.depth = 0
    #     else:
    #         self.Meta.depth = 1

       

        


        
class AppointmentSerializerTwo(serializers.ModelSerializer):
       
    class Meta:
        model = Appointment

        fields = ('__all__')
        depth=1
    