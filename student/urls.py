from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboard),
    path('signuptask', views.signuptask),
    path('entermarks', views.entermarks),
    path('deletestu', views.deletestu),
    path('stupass', views.stupass),
    path('modstu', views.modstu),
    path('modresult', views.modresult),
    path('cheksignup', views.cheksignup),
    path('sendotp', views.sendotp),
    path('imgupdate', views.imgupdate),
    path('updaetstu', views.updaetstu),
    path('deletemark',views.deletemark),
    path('resetstupass',views.resetstupass),
] 


