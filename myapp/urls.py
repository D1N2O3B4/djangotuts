from django.urls import path
from . import views

urlpatterns = [path('',views.index,name='home'),
               path('counter',views.count,name='counter')]
