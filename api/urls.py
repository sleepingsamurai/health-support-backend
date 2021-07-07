from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name="api-overview"),
    path('user-list/', views.userList,name="user-list"),
    path('user-register/', views.userRegister,name="user-register"),
    path('hospital-list/', views.hospitalList,name="hospital-list"),
    path('vaccine-slot-list/', views.vaccineSlotList,name="vaccine-slot-list"),
    path('bed-list/', views.bedsList,name="bed-list"),
    path('oxygen-cylinder-list/', views.oxygenCylinderList,name="oxygen-cylinder-list"),
    path('booking-list/', views.bookingsList,name="booking-list"),
    path('item-list/', views.itemList,name="item-list"),

]