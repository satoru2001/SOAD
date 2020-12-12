from django.urls import path
from django.conf.urls import include
from .views import index,data_view
app_name = 'mock_app'
urlpatterns = [
    path("",index,name="home"),
    path("data/",data_view,name="data"),
]

