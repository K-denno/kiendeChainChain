from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index,name="home"),
    path('', views.profile,name="home"),
    path("sign",views.signup,name="signup")
  ]


