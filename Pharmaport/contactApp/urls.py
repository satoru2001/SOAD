from django.contrib import admin
from django.urls import path,include
from contactApp import views
app_name = 'feedback'
urlpatterns = [
    path('',views.feedback,name ="home"),
]
