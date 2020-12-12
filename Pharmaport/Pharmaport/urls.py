"""Pharmaport URL Configuration

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
from django.conf.urls import include
from Pharmaport import views


urlpatterns = [
    path('',views.index,name='home'),
    path('admin/', admin.site.urls),
    path('users_page/',include('users_page.urls',namespace="users_page")),
    path('doctors/',include('Doctors.urls',namespace="doctors")),
    path('register/',include('Register.urls')),
    path('feedback/',include('contactApp.urls',namespace='feedback')),
    path('payment/',include('donate.urls', namespace='donate')),
    path('api/',include('Pharmaport.api.urls',namespace="api")),
    path('mock/',include('mockapps.urls',namespace="mock_app")),
]
