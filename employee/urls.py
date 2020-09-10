
from django.urls import path,include

from . import views
urlpatterns = [
    path('leave/',views.create_leave,name='leave'),
]
