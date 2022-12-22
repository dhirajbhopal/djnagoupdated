from django.urls import path, include
from . import views


urlpatterns = [
    path('facultyprofile', views.facultyprofile),
    path('facenroll', views.facenroll),
    path('deletefac', views.deletefac),
    path('modfac', views.modfac),
    path('facpass', views.facpass),
    path('uploadfacimg', views.uploadfacimg),

] 
