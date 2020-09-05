from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _

class CreateUser(AbstractUser):
    ROLES = (

        ('manager', 'Manager'),
        ('employee', 'Employee'),
        ('admin', 'Administrator'),

    )

    username= None
    email = models.EmailField(unique=True)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    roles = models.CharField(max_length=50, choices = ROLES)
    date_joined = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
   
    def __str__(self):
        return self.email
