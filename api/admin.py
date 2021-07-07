from django.contrib import admin
from .models import Hospitals, Items, VaccineSlots, Beds, OxygenCylinder, Bookings

# Register your models here.
admin.site.register(Hospitals)
admin.site.register(Items)
admin.site.register(VaccineSlots)
admin.site.register(Beds)
admin.site.register(OxygenCylinder)
admin.site.register(Bookings)

