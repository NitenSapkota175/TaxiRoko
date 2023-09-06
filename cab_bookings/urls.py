from django.urls import path,include
from . import views
urlpatterns = [
    path('' , views.Home , name='Home'),
    path('about_us/',views.About_Us,name='About_Us'),
  
]
