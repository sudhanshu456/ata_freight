
from django.urls import path,include

from . import views
urlpatterns = [
    path('approve_list/',views.approve_list.as_view(),name='approve_list'),
    path('application_detail/<int:pk>/',views.ApplicationDetail.as_view(),name='application_detail'),
    path('approve/<int:id>/',views.approve_leave,name='approve_leave')
]
