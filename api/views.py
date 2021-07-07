from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.models import User
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hospitalList(request):
    hospitals = Hospitals.objects.all()
    serializer = HospitalSerializer(hospitals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def itemList(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vaccineSlotList(request):
    vaccineslots = VaccineSlots.objects.all()
    serializer = VaccineSerializer(vaccineslots, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bedsList(request):
    beds = Beds.objects.all()
    serializer = BedSerializer(beds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def oxygenCylinderList(request):
    oxygencylinders = OxygenCylinder.objects.all()
    serializer = OxygenSerializer(oxygencylinders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bookingsList(request):
    bookings = request.user.bookings_set.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def userRegister(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)