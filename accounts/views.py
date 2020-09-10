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
        group, created = Group.objects.get_or_create(name=form.instance.roles) 
        user.groups.add(group)
        if form.instance.roles=='employee':
            Employee.objects.create(
             user=user)
        return super().form_valid(form)

