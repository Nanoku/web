"""CRT6_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import (handler400, handler403, handler404, handler500)
from mainapp.views import *
#from django.http import *
#from django.contrib import admin

#handler404 = handler404

urlpatterns = [
    path('', test, name='home'), #r'^$'
    path('login/', test, name='home'),
    path('signup/', test, name='home'),
    path('question/<int:q_id>/',  test, name='home'),
    path('ask/', test, name='home'),
    path('popular/', test, name='home'),
    path('new/', test, name='home'),
    path('new/', test, name='home'),
]