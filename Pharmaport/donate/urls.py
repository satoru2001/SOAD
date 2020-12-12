from django.urls import path
from donate import views
app_name = 'donate'
urlpatterns = [
    path('',views.index,name='index'),
    path('charge/',views.charge,name='charge'),
    path('success/<str:args>/',views.successMsg,name='success'),
]
