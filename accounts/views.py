from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import PublicUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import Group, Permission
# Create your views here.
from employee.models import Employee

class SignUpView(generic.CreateView):
    form_class = PublicUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        '''adding roles while signup'''
        user = form.save()
        
        rol=form.instance.roles
        group, created = Group.objects.get_or_create(name=rol) 
        if rol=='manager':
            p1=Permission.objects.get(name='Can view employee')
            p2=Permission.objects.get(name='Can change employee')
            group.permissions.add(p1,p2)
        elif rol=='employee':
            p1=Permission.objects.get(name='Can view employee')
            p2=Permission.objects.get(name='Can change employee')
            p3=Permission.objects.get(name='Can add employee')
            group.permissions.add(p1,p2,p3)
        elif rol=='admin':
             p=Permission.objects.get(name='Can view employee')
             p1=Permission.objects.get(name='Can view permission')
             p2=Permission.objects.get(name='Can view group')
             p3=Permission.objects.get(name='Can view leave_application')
             p4=Permission.objects.get(name='Can view user')
             p5=Permission.objects.get(name='Can change leave_application')
             group.permissions.add(p1,p2,p3,p,p5,p4)
             user.is_staff=True
             user.save() 
        user.groups.add(group)
        if form.instance.roles=='employee':
            Employee.objects.create(
             user=user)
        return super().form_valid(form)

