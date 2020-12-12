from django.contrib import admin
from django.urls import path
from users_page import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "users_page"

urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.fileslist,name="fileslist"),
    path('list/upload',views.uploadfile,name="uploadfile"),
    path('list/<int:pk>/', views.delete_file, name='delete_file'),
    path('/otp',views.otp_generate,name="otp"),
    path('/rate',views.Rate,name='Rate'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)