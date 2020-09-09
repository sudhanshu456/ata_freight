import uuid
from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import CreateUser
# Create your models here.

class Employee(models.Model):
    user=models.OneToOneField(CreateUser, on_delete=models.CASCADE)
    num_available_leave=models.IntegerField(default=30,null=True,blank=True)

    def __str__(self):
        return self.user.email or ' '
    

class leave_application(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    user=models.ForeignKey(Employee,on_delete=models.CASCADE)
    subject=models.TextField()
    application=RichTextField()


    def __str__(self):
        return self.subject or ' '
    

    