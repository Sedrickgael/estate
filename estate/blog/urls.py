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
router.register('commentaireapi', CommentaireViewSet, base_name='commentaireapi')
router.register('videoapi', NewVideoViewSet, base_name='videoapi')
router.register('imageapi', NewImageViewSet, base_name='imageapi')
router.register('newapi', NewViewSet, base_name='newapi')
router.register('auteurapi', AuteurViewSet, base_name='auteurapi')
router.register('categorieapi', CategorieViewSet, base_name='categorieapi')

urlpatterns = [
    path('blogliste/', views.blog, name='blog'),
    path('comment/<id>', views.comment, name='comment'),
    path('blogdetails/<slug>', views.blogdetails,name='blogdetails'),
]


urlpatterns += router.urls