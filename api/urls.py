from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name="api-overview"),
    path('user-list/', views.userList,name="user-list"),
    path('user-register/', views.userRegister,name="user-register"),
]