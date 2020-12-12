from rest_framework import status
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes, renderer_classes, authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from users_page.models import doc,files
from django.core.exceptions import ObjectDoesNotExist
from .serializers import docGetSerializer,filesGetSerializer,pres_data_serializers,UploadSerializer, connection, keyforconnection
from Doctors.models import prescription
from rest_framework.viewsets import ViewSet
from users_page.models import connection_api,otp,files
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.renderers import HTMLFormRenderer,TemplateHTMLRenderer, BrowsableAPIRenderer
import datetime

class feedback(object):
    def __init__(self , rating,doc_name,hospital_name,feedback):
        self.rating = rating
        self.name = doc_name
        self.hospital_name = hospital_name
        self.recent_feedback = feedback

class file_retrive(object):
    def __init__(self,name,metadata,url,date):
        self.name = name
        self.metadata = metadata
        self.file_url = url
        self.date_created = str(date)[:10]+" "+str(date)[11:19]


def return_dict(obj_list):
    rating = 0
    for obj in obj_list:
        rating+=obj.rating
    rating = rating/len(obj_list)
    rec_feed=''
    for i in range(10 if len(obj_list)>=10 else len(obj_list)):
        rec_feed+=str(i+1)+": "+obj_list[i].feedback+" "
    data = feedback(rating,obj_list[0].docname,obj_list[0].hospital,rec_feed)
    return data

@api_view(http_method_names=['GET'])
@authentication_classes([])
@permission_classes([])
def get_docFeedback_docid(request,doc_id):# retrive ojects
    obj_list = doc.objects.filter(doctor_id=doc_id)
    if(len(obj_list)>0):
        data = return_dict(obj_list)
        serializer = docGetSerializer(data)
        return Response(data=serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=['GET'])
@authentication_classes([])
@permission_classes([])
def get_docFeedback_hosp(request,hospital):# retrive ojects
    obj_list = doc.objects.filter(hospital=hospital)
    if(len(obj_list)>0):
        docs = set()
        data = list()
        for obj in obj_list:
            docs.add(obj.doctor_id)
        for doc_id in docs:
            data.append(return_dict(doc.objects.filter(doctor_id=doc_id)))
        serializer = docGetSerializer(data,many=True)
        return Response(data=serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=['GET'])
@authentication_classes([])
@permission_classes([])
def get_files(request,name):
    obj_list = files.objects.filter(name=name)
    if(len(obj_list)>0):
        data = []
        for i in obj_list:
            data.append(file_retrive(i.name,i.metadata,i.uploadedfiles.url,i.date))
        serializer = filesGetSerializer(data,many=True)
        return Response(data=serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(http_method_names=['GET'])
@authentication_classes([])
@permission_classes([])
def patient_files(request,con_id,count=10):
    obj = connection_api.objects.get(connection_id=con_id)
    if obj:
        obj_list = files.objects.filter(user=obj.user).order_by("-date")
        if(len(obj_list)>0):
            data = []
            r = count
            if(len(obj_list)<count):
                r = len(obj_list)
            for k in range(r):
                i = obj_list[k]
                data.append(file_retrive(i.name,i.metadata,i.uploadedfiles.url,i.date))
            serializer = filesGetSerializer(data,many=True)
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response("Entered Connection Key is Wrong",status=status.HTTP_401_UNAUTHORIZED)

@api_view(http_method_names=['GET','POST',])
@authentication_classes([])
@permission_classes([])
def method_identify(request,comp_laint):
    if request.method == 'GET':
        return complaint_data_get(request,comp_laint)
    elif request.method == 'POST':
        return complaint_data_post(request)

def complaint_data_get(request,comp_laint):
    data = prescription.Objects.filter(comp=comp_laint)
    serializer = pres_data_serializers(data,many=True)
    return Response(data=serializer.data)

def complaint_data_post(request):
    serializer = pres_data_serializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['POST'])
@authentication_classes([])
@permission_classes([])
def establish_connection(request):
    serializer = connection(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(username=serializer.data["username"])
        user_otp = otp.objects.filter(user=user).order_by('-date')[0]
        if(user_otp.passcode == serializer.data["passcode"]):
            connect = connection_api(doctor_id = serializer.data["docid"],user=user,date=datetime.datetime.now())
            connect.save()
            ser = keyforconnection({"secret_key":str(connect)})
            return Response(data=ser.data,status=status.HTTP_200_OK)
        else:
            return Response("passcode donot match",status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            con_id = serializer.data["connection_id"]
            try:
                obj = connection_api.objects.get(connection_id=con_id)
            except ObjectDoesNotExist:
                print("yes its true")
                return Response("invalid key",status=status.HTTP_404_NOT_FOUND)
            file_uploaded = request.FILES.get('file_uploaded')
            user_file = files(name=serializer.data["name"],metadata=serializer.data["metadata"],
                        via_api=True,connection=obj,user=obj.user,uploadedfiles=file_uploaded)
            user_file.save()

            return Response("Success",status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
