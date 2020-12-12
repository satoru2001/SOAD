from .views import get_docFeedback_docid,get_docFeedback_hosp,get_files,method_identify,establish_connection,patient_files 
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UploadViewSet
app_name = 'api'

router = routers.DefaultRouter()
router.register('', UploadViewSet, basename="upload")

urlpatterns = [
    path('doctor/<int:doc_id>/',get_docFeedback_docid,name='post-doc'),
    path('doctor/<str:hospital>/',get_docFeedback_hosp,name='post-hosp'),
    path('dataset/<str:name>/',get_files,name="get-files"),
    path('prescription/<str:comp_laint>', method_identify,name="comp_data"),
    path('connect/',establish_connection,name="conn"),
    path('data/<str:con_id>/<int:count>',patient_files,name="get data"),
    path('data/<str:con_id>',patient_files,name="get data default"),
    path("upload/", include(router.urls)),
]