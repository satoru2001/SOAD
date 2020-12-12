from rest_framework import serializers
from users_page.models import doc,files
from Doctors.models import prescription
from rest_framework.serializers import Serializer, FileField



class UploadSerializer(serializers.Serializer):
    connection_id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    metadata = serializers.CharField(required=False)
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded','connection_id','name','metadata']


class docGetSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    hospital_name = serializers.CharField(max_length=100)
    recent_feedback = serializers.CharField()


class filesGetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    metadata = serializers.CharField()
    date_created = serializers.DateTimeField()
    file_url = serializers.URLField()

class pres_data_serializers(serializers.Serializer):
    comp=serializers.CharField()
    medicine=serializers.CharField()
    medicine_1=serializers.CharField()
    medicine_2=serializers.CharField()
    medicine_3=serializers.CharField()
    medicine_4=serializers.CharField()

    def create(self,validated_date):
        return prescription(**validated_date)



class connection(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100)
    docid = serializers.IntegerField(required=True)
    passcode = serializers.IntegerField(required=True)

class keyforconnection(serializers.Serializer):
    secret_key = serializers.CharField(max_length=100)