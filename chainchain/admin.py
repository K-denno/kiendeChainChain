from django.contrib import admin
from .models import Profile,Level,Notifications
# Register your models here.

admin.site.register(Profile)
admin.site.register(Notifications)
admin.site.register(Level)