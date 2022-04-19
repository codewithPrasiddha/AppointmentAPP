from re import U
from .models import Appointment,Rating
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializer import AppointmentSerializer,RatingSerializer,AppointmentSerializerTwo
from api.models import User


@api_view(['GET'])
def All(request):

    a = Appointment.objects.all()

    s = AppointmentSerializerTwo(a, many=True)

    return Response(s.data)


@api_view(['GET'])
def Single(request, pk):

    a = Appointment.objects.filter(id=pk)
    s = AppointmentSerializer(a, many=True)
    return Response(s.data)


@api_view(['POST'])
def Add(request):

    s = AppointmentSerializer(data=request.data)
    if s.is_valid():
        
        s.save()
        return Response(s.data)


@api_view(['PUT'])
def Edit(request, pk):
    u = Appointment.objects.get(id=pk)
    s = AppointmentSerializer(
        instance=u, data=request.data)
    if s.is_valid():

        s.save()
    return Response(s.data)


@api_view(['DELETE'])
def Remove(request, pk):
    d = Appointment.objects.get(id=pk)
    d.delete()
    return Response("Appointment Deleted")



@api_view(['GET'])
def AllRating(request):

    a = Rating.objects.all()

    s = RatingSerializer(a, many=True)

    return Response(s.data)


@api_view(['GET'])
def SingleRating(request, pk):

    a = Rating.objects.filter(id=pk)
    s = RatingSerializer(a, many=True)
    return Response(s.data)


@api_view(['POST'])
def AddRating(request):

    s = RatingSerializer(data=request.data)
    if s.is_valid():
            
        s.save()
    return Response(s.data)





