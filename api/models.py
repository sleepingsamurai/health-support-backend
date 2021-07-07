from django.contrib.auth.backends import UserModel
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.

class Hospitals(models.Model) :
    name = models.TextField()

    def __str__(self):
        return self.name

class Items(models.Model) :
    name = models.TextField()

    def __str__(self):
        return self.name

class VaccineSlots(models.Model) :
    vaccine_slot_code = models.CharField(max_length = 20)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return self.vaccine_slot_code

class Beds(models.Model) :
    bed_code = models.CharField(max_length = 20)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return self.bed_code

class OxygenCylinder(models.Model) :
    oxygen_cylinder_code = models.CharField(max_length = 20)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)

    def __str__(self):
        return self.oxygen_cylinder_code

class Bookings(models.Model) :
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    item = models.ForeignKey(Items,  on_delete=models.CASCADE)

    def __str__(self):
        return self.user