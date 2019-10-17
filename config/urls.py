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
router.register('caracteristiqueapi', CaracteristiqueViewSet, base_name='caracteristiqueapi')
router.register('socialLinkapi', SocialLinkViewSet, base_name='socialLinkapi')
router.register('headerslideapi', HeaderSlideViewSet, base_name='headerslideapi')
router.register('otherpageapi', OtherPageViewSet, base_name='otherpageapi')
router.register('pageap', PageViewSet, base_name='pageap')
router.register('plainteapi', PlainteViewSet, base_name='plainteapi')
router.register('consultantapi', ConsultantViewSet, base_name='consultantapi')
router.register('identiteapi', IdentiteViewSet, base_name='identiteapi')
router.register('bureauapi', BureauViewSet, base_name='bureauapi')

urlpatterns = [
]

urlpatterns += router.urls