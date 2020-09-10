from django.shortcuts import render,reverse
from employee.models import leave_application,Employee
# Create your views here.
from employee.models import leave_application,Employee
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponseRedirect

class approve_list(LoginRequiredMixin,ListView):
     model = leave_application
     template_name='approve_list.html'

     # def test_func(self):
     #      return self.request.user.roles == "manager"


class ApplicationDetail(DetailView):
    model = leave_application
    template_name = 'detailapplication.html'



def approve_leave(request,id):
     leve=leave_application.objects.get(id=id)
     usr=Employee.objects.get(user=leve.user)
     usr.num_available_leave=usr.num_available_leave-leve.total_days
     usr.save()
     leve.approved=True
     leve.save()
     return HttpResponseRedirect(reverse('application_detail', args=[id]))