from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index,name="home"),
    path('', views.profile,name="home"),
    path('malisafi/<slug:user_name>/', views.connections,name="connections"),
    path("sign",views.signup,name="signup"),
  ]


