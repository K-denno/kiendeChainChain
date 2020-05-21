from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=20,default="beginner")

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    dp = models.ImageField(upload_to="profile_pictures",blank=True)
    bio = models.CharField(max_length=500)
    level = models.OneToOneField(Level,on_delete=models.CASCADE,related_name="profiles",null=True)
    phone_number = models.BigIntegerField(null=True)
    location = models.CharField(max_length=20)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.user.username

class Notifications(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications')
    message = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message