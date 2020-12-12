from django.contrib import admin
from django.urls import path
from  Register import views

app_name='Register'

urlpatterns = [
    path('',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='logout'),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('check_otp',views.check_otp,name='check_otp'),
]
