from django.shortcuts import render,redirect,get_object_or_404
from .forms import leave_applications
from .models import Employee
from accounts.models import CreateUser
from datetime import date
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test,permission_required


# Create your views here.

@permission_required('employee.add_leave_application','employee.view_leave_application')
def create_leave(request):
    days_left=check_daysleft(request.user.id)
    users=get_object_or_404(CreateUser,email=request.user.email)
    # user=get_object_or_404(Employee, id=request.user.id)
    form=leave_applications(instance=users)
    
    if request.method=='POST':
        form=leave_applications(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user=get_object_or_404(Employee,user_id=request.user.id)
            d1 = data.start_date
            d2 = data.end_date
            day = (d2 - d1).days
            data.total_days=days
            data.approved=False
            # chnge=get_object_or_404(Employee,user_id=request.user.id)
            # chnge.num_available_leave=chnge.num_available_leave- int(day)
            # chnge.save()
            data.applied_on=timezone.now()
            data.save()
            return redirect('/') #redirect('home')
    context={'form':form,'days_left':days_left}
    return render(request,'leave.html',context)

    
def check_daysleft(ids):
    
    try:
        emp=Employee.objects.get(user_id=ids)
        days_left=emp.num_available_leave
        print(emp.num_available_leave)
        return int(days_left)

    except Exception as e:
        print(e)