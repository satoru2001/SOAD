from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users_page.models import otp,doc,connections_existed,files
import random,datetime
from users_page.forms import filesForm,feedbackForm
from Doctors.models import prescription
# Create your views here.

@login_required(login_url="Register:user_login")
def fileslist(request):
    f = files.objects.all()
    p = prescription.objects.all().filter(pa_id=request.user.username).order_by('date')
    cdict = {'files':f,'prescription':p}
    return render(request,'patients/fileslist.html',context=cdict)

def uploadfile(request):
    if request.method == 'POST':
        form = filesForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            return redirect('/users_page/list')
    else:
        form = filesForm()
        
    cdict = {'form':form}

    return render(request,'patients/uploadfile.html',context=cdict)

def delete_file(request, pk):
    if request.method == 'POST':
        f = files.objects.get(pk=pk)
        f.delete()
    return redirect('/users_page/list')

def otp_generate(request):
    number = random.randint(100000,999999)
    otp_obj = otp(passcode = number,user=request.user,date=datetime.datetime.now())
    otp_obj.save()
    return render(request,'patients/fileslist.html',context={'passcode':number})

def Rate(request):
	user = request.user

	if request.method == 'POST':
		form = feedbackForm(request.POST)
		if form.is_valid():
			rate = form.save(commit=False)
			rate.user = user
			rate.save()
			return redirect('/users_page/list')
	else:
		form = feedbackForm()

	context = {
		'form': form, 
	}

	return render(request,'patients/rate.html',context=context)