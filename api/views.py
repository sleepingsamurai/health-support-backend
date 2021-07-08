import re
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
        'VaccineTypeList' : '/vaccine-type-list/',
        'VaccineSlotList' : '/vaccine-slot-list/',
        'BedList' : '/bed-list/',
        'OxygenCylinderList' : '/oxygen-cylinder-list/',
        'BookingList' : '/booking-list/',
        'ItemList' : '/item-list/',
        'VaccineTypeSlot' : '/vaccine-slot/<str:vactid>/',
        'HospitalVaccineSlot' : '/hospital-vaccine-slot/<str:hospid>',
    }
    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hospitalList(request):
    if request.method == 'GET':
        hospitals = Hospitals.objects.all()
        serializer = HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def itemList(request):
    if request.method == 'GET':
        items = Items.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vaccineTypeList(request):
    if request.method == 'GET':
        vaccinetype = VaccineType.objects.all()
        serializer = VaccineTypeSerializer(vaccinetype, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VaccineTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def vaccineSlotList(request):
    if request.method == 'GET':
        vaccineslots = VaccineSlots.objects.all()
        serializer = VaccineSerializer(vaccineslots, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VaccineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bedsList(request):
    if request.method == 'GET':
        beds = Beds.objects.all()
        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def oxygenCylinderList(request):
    if request.method == 'GET':
        oxygencylinders = OxygenCylinder.objects.all()
        serializer = OxygenSerializer(oxygencylinders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OxygenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bookingsList(request):
    if request.methd == 'GET':
        bookings = request.user.bookings_set.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def userRegister(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getVaccineTypeSlots(request, vactid) :
    vaccinetype = VaccineType.objects.get(id=vactid)
    slots = vaccinetype.vaccineslots_set.all()
    serializer = VaccineSerializer(slots, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getHospitalVaccineSlots(request, hospid) :
    hospital = Hospitals.objects.get(id=hospid)
    slots = hospital.vaccineslots_set.all()
    serializer = VaccineSerializer(slots, many=True)
    return Response(serializer.data)



