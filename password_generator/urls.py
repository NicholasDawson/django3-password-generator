"""password_generator URL Configuration

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
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('password/', views.password, name='password'),
    # `/` is included so that people can type in example.com/password/ or example.com/password just a quality of life improvement
    # name field is what name you can reference using {% url 'name' %}
]
