from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = ['username','email', 'password']

class HospitalSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Hospitals
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Items
        fields = '__all__'

class VaccineSerializer(serializers.ModelSerializer) :
    class Meta:
        model = VaccineSlots
        fields = '__all__'

class BedSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Beds
        fields = '__all__'

class OxygenSerializer(serializers.ModelSerializer) :
    class Meta:
        model = OxygenCylinder
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Bookings
        fields = '__all__'


