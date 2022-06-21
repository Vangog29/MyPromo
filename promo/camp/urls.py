"""promo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from camp import views



urlpatterns = [

    path('camps', views.camps, name='camps'),
    path('createcamp', views.createcamp, name='createcamp'),
    path('mycamp', views.mycamp, name ='mycamp'),
    path('camps/<int:id_campaign>', views.showcamp, name='showcamp'),
    path('campsedit/<int:id_campaign>', views.editcamp, name='editcamp'),
    path('homeedit/<int:id_campaign>', views.homeedit, name='homeedit'),
    path('polledit/<int:id_campaign>', views.polledit, name='polledit'),
    path('formpoll/<int:id_campaign>', views.formpoll, name='formpoll'),

]
