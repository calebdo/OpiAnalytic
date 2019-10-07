from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog import models as cmod

# Create your models here.
class User(AbstractUser):
    email = models.TextField()
    
        
        