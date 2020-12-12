from django.shortcuts import render
from .forms import pres_form,apoi_form,get_pres,UploadDocumentForm,io,io_1
import datetime,time
from django.contrib.auth.decorators import login_required
from .models import prescription,apointment_1,Profile
from users_page.models import connections_existed,otp,files
from django.contrib.auth.models import User
from users_page.forms import filesForm
from django.utils import timezone
now_aware = timezone.now()


@login_required(login_url="Register:user_login")
def index_view(request):
    if not request.user.userprofileinfo.is_doctor:
        context={"errors":"You are not a doctor/signed in with user account"}
    else:
        data=prescription.objects.all()
        next_apoi=datetime.date.today()+datetime.timedelta(1)
        dates = apointment_1.objects.filter(date_filed=next_apoi)
        view_pres = None
        cname = None
        te = ""
        cal_info = ""
        form = pres_form
        form_1= apoi_form
        form_2 = get_pres
        form_3 = UploadDocumentForm
        files_form = filesForm
        test = io
        test_1 = io_1
        a={}
        context = {}
        a['qw']=''
        if request.method == 'POST':
            form = pres_form(request.POST)
            form_1 = apoi_form(request.POST)
            form_2= get_pres(request.POST)
            form_3= UploadDocumentForm(request.POST, request.FILES)
            files_form = filesForm(request.POST, request.FILES)
            test = io(request.POST)
            test_1 = io_1(request.POST)

            # Connection establishing
            if test.is_valid():
                id_1 = test.cleaned_data['id_temp']
                otp_entered = test.cleaned_data['otp']
                user = User.objects.get(username=id_1)
                user_otp = otp.objects.filter(user=user).order_by('-date')[0]
                if(user_otp.passcode == int(otp_entered)):
                    connect = connections_existed(doctor_id = request.user.userprofileinfo.doctor_id,user=user,date=datetime.datetime.now())
                    connect.save()
            
            if test_1.is_valid():
                delta = datetime.timedelta(200)
                cname = test_1.cleaned_data['cars']
                id_2 = test_1.cleaned_data['id_temp_1']
                try:
                    user_con = User.objects.get(username=id_2)
                    doc_con = request.user.userprofileinfo.doctor_id
                    time = connections_existed.objects.filter(doctor_id = doc_con,user=user_con).order_by('-date')[0]
                    dif = datetime.datetime.now() - time.date.replace(tzinfo=None)
                except:
                    dif = datetime.timedelta(2)
                    te= "The data wont be saved as either the patient doesnt exist in records or you havent connected "
                finally:
                    if(delta > dif):
                        a['qw'] = id_2
                        context['ty'] = a
                    else:
                        te= "The data wont be saved as either the patient doesnt exist in records or you havent connected "

            
            elif form.is_valid():
                form.pa_id = form.cleaned_data['pa_id']
                form.age_1 = form.cleaned_data['age_1']
                form.comp = form.cleaned_data['comp']
                form.doc_name = form.cleaned_data['doc_name']
                form.medicine = form.cleaned_data['medicine']
                form.med_co = form.cleaned_data['med_co']
                form.medicine_1 = form.cleaned_data['medicine_1']
                form.medicine_2 = form.cleaned_data['medicine_2']
                form.medicine_3 = form.cleaned_data['medicine_3']
                form.medicine_4 = form.cleaned_data['medicine_4']
                form.save()
                form = pres_form


            elif form_1.is_valid():
                apoi_user = form_1.cleaned_data['pat_id_1']
                try:
                    apoi_user_1 = User.objects.get(username=apoi_user)
                    bol = 1
                except:
                    bol = 0
                
                print(bol)
                if(bol == 1):
                    form_1.pat_id_1 = form_1.cleaned_data['pat_id_1']
                else:
                    form_1.pat_id_1 = "hello"
                form_1.date_filed = form_1.cleaned_data['date_filed']
                form_1.time_filed=form_1.cleaned_data['time_filed']
                form_1.save()

            elif form_3.is_valid():
                form_3.save()
            
            elif files_form.is_valid():
                print(files_form)
                print('hello')
                print(files_form.cleaned_data['pa_id'])
                obj = files_form.save(commit=False)
                obj.user=context['ty'].qw
                obj.save()


        count_tot = len(data)
        context = {  'pat' : data ,'form_1':form_1 ,'form_3':form_3 ,'test' :test,'test_1' :test_1, 'tot_con':count_tot , 'next':dates , 'ty':a ,'te':te , 'info':cal_info ,'user':a['qw']}

        if(cname=='b'):
            context['form'] = form
            context['type'] = 'b'
        elif(cname=='a'):
            view_pres=prescription.objects.filter(pa_id=a['qw'])
            context['view_pres'] = view_pres
            context['type'] = 'a'
        elif(cname=='c'):
            context['reports_data'] = get_files(a['qw'])
            context['type1'] = 'a'
            context['type'] = 'c'
        elif(cname=='d'):
            context['report'] = files_form
            context['type1'] = 'b'
            context['type'] = 'c'
        else:
            context['type'] ='c'
            context['type1'] = 'c'


        #elif request.method == 'GET':
        #   form_3 = dform(request.GET)
        #  if form_3.is_valid():
        #     temp = request.GET['dete_filed']
            #    form_3.date_filed = temp
            #   form_3.save()
                
    # if request.method == 'GET':
        #    form_1 = apoi_form(request.GET)
        #   form_1.pat_id_1 = form.cleaned_data['pat_id_1']
        #  form_1.save()
        # form_1 = apoi_form 
        #count_tot = len(data)
        #context = { 'form':form , 'pat' : data ,'form_1':form_1,'form_2':form_2 ,'form_3':form_3 , 'view_pres' : view_pres, 'tot_con':count_tot , 'next':dates}
    return render(request,'doctor/base.html',context=context)


def get_files(user,count=10):
    file_url = []
    user = User.objects.get(username=user)
    files_obj = files.objects.filter(user=user).order_by('-date')
    r = count
    if (len(files_obj)<r):
        r = len(files_obj)
    for k in range(r):
        i = files_obj[k]
        file_url.append(i)
    return file_url