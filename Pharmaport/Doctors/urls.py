from django.contrib import admin
from django.urls import path
from Doctors import views

app_name = "doctors"

urlpatterns = [
    path('',views.index_view,name="index_view"),
    # path('api/<str:comp_laint>', include('website.api.urls'))
   # path('<str:cname>/',views.index_view,name="index_view"),
]
