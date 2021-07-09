from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework.authtoken.views import Token

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = ['id','username','email', 'password']

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True,
        } }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class HospitalSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Hospitals
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Items
        fields = '__all__'

class VaccineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineType
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



