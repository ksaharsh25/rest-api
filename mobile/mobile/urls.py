"""mobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from spam.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spamlist',Spamlist.as_view(),name='Spamlist'),
    path('spamlist/<str:pk>',SpamDetails.as_view(),name='SpamDetails'),
    path('mobilelist',mobilelist.as_view(),name='mobilelist'),
    path('mobilelist/<str:pk>',mobiledetails.as_view(),name='mobiledetails'),
    path('numberexist/<str:number>',numberexist,name="spam"),
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('mark_as_spam/<str:mobspam>',mark_as_spam,name="mark_as_spam")
    
]
