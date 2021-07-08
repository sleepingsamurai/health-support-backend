from api.views import vaccineTypeList
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Hospitals)
admin.site.register(Items)
admin.site.register(VaccineSlots)
admin.site.register(Beds)
admin.site.register(OxygenCylinder)
admin.site.register(Bookings)
admin.site.register(VaccineType)

