import uuid
from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import CreateUser
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse


class Employee(models.Model):
    user=models.OneToOneField(CreateUser, on_delete=models.CASCADE,primary_key=True)
    num_available_leave=models.IntegerField(default=30,null=True,blank=True)

    def __str__(self):
        return self.user.email or ' '


class leave_application(models.Model):

    user=models.ForeignKey(Employee,on_delete=models.CASCADE)
    subject=models.TextField()
    application=RichTextField()
    start_date=models.DateField()
    end_date=models.DateField()
    applied_on=models.DateTimeField()
    approved=models.BooleanField()
    total_days=models.IntegerField()
    def __str__(self):
        return self.subject or ' '
    
    def get_absolute_url(self):
        return reverse("application_detail", kwargs={"pk": self.pk})
    

    