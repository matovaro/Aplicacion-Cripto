from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('aes', views.aes, name='aes'),
    path('eoa', views.eoa, name='eoa'),
    path('firma', views.firma, name='firma'),
    path('validar', views.validar, name='validar'),
    path('ver', views.verification, name='ver'),
    path('<int:save_id>/', views.detail, name='detail')

]