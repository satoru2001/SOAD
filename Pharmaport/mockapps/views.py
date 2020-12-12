from django.shortcuts import render
from .forms import dataset,doc,data
import requests
# Create your views here.
def index(request):
    form1 = doc
    a = ''
    t = ''
    if request.method=='POST':
        form1 = doc(request.POST)
        if form1.is_valid():
            print("hello")
            doc_id = form1.cleaned_data['doc_id']
            hospital = form1.cleaned_data['hospital']
            url = "http://127.0.0.1:8000/api/doctor/"
            if(doc_id):
                url = url+str(doc_id)
            elif(hospital):
                url=url+str(hospital)
                t = 'aaa'
            url+="?format=json"
            print(url)
            r = requests.get(url)
            a = r.json()
    context = {'form1':form1,'a':a,'t':t}
    return render(request,'mockapps/index.html',context=context)

def data_view(request):
    form = data
    b = ''
    if request.method=='POST':
        form = data(request.POST)
        if form.is_valid():
            conn_id = form.cleaned_data['conn_id']
            count = form.cleaned_data['count']
            url = "http://127.0.0.1:8000/api/data/"
            if(conn_id):
                url = url+str(conn_id)
            if(count):
                url=url+"/"+str(count)
            url+="?format=json"
            print(url)
            r = requests.get(url)
            b = r.json()
            print(len(b))
            return render(request,'mockapps/data.html',context={"b":b})
    context = {'form':form,'b':b}
    return render(request,'mockapps/data.html',context=context)