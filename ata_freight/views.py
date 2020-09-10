from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import CreateUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required()
def index(request):
    user=CreateUser.objects.get(email=request.user.email)
    context={'data':user}
    return render(request,'home.html',context)

def logouts(request):
    logout(request)
    return redirect('index')#redirect(request.META.get('HTTP_REFERER','/'))