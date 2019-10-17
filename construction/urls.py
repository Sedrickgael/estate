"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import *
from .  import views


router = DefaultRouter()
router.register('typedemaisonapi', TypeDeMaisonViewSet, base_name='typeapi')
router.register('maisonapi', HouseViewSet, base_name='maisonapi')
router.register('localisationapi', LocalisationViewSet, base_name='localisationapi')

urlpatterns = [
    path('', views.index, name='index'),
    path('nos_maisons/', views.house, name='house'),
    path('details_maison/<slug>', views.housedetails, name='house_details'),
]

urlpatterns += router.urls