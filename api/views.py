from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.models import User
from .models import *

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'UserList' : '/user-list/',
        'Register' : '/user-register/',
        'HospitalList' : '/hospital-list/',
        'VaccineSlotList' : '/vaccine-slot-list/',
        'BedList' : '/bed-list/',
        'OxygenCylinderList' : '/oxygen-cylinder-list/',
        'BookingList' : '/booking-list/',
        'ItemList' : '/item-list/',
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def hospitalList(request):
    hospitals = Hospitals.objects.all()
    serializer = HospitalSerializer(hospitals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def itemList(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def vaccineSlotList(request):
    vaccineslots = VaccineSlots.objects.all()
    serializer = VaccineSerializer(vaccineslots, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bedsList(request):
    beds = Beds.objects.all()
    serializer = BedSerializer(beds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def oxygenCylinderList(request):
    oxygencylinders = OxygenCylinder.objects.all()
    serializer = OxygenSerializer(oxygencylinders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookingsList(request):
    bookings = Bookings.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def userRegister(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)