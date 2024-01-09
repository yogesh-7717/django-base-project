from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userprofile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    phone_number = models.CharField(max_length= 12)
    address = models.TextField(max_length= 100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    