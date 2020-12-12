from django.shortcuts import render
from Register.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import requests,json,urllib
from django.contrib.auth.models import User
from django.http import JsonResponse
from Register.models import UserProfileInfo
from django.core.mail import EmailMessage,send_mail
from django.conf import settings


# from django.views import View
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from Register.utils import token_generator
from django.template.loader import render_to_string
import random
import os
import qrcode

otp=0

def index(request):
    return render(request,'Register/index.html')
    

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    registered = False
    initial_data={
        'doctor_id':'0',
    }
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            url = 'https://www.google.com/recaptcha/api/siteverify'
            clientkey = request.POST.get('g-recaptcha-response')
            secretkey='6LdkdgMaAAAAAF8KWEg4CC2eqCFTs2cRR3l1EKZ2'
            values={
			'secret' : secretkey,

			'response' : clientkey,
			}
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url,data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']: 
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered = True
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': token_generator.make_token(user),
                    })
                to_list=[user.email]
                from_email=settings.EMAIL_ADDRESS
                send_mail(mail_subject, message, from_email,to_list,fail_silently=False)
                return HttpResponse('Please confirm your email address to complete the registration')
            else:
                return HttpResponse('Invalid recaptcha')    

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm(initial=initial_data)
    return render(request,'Register/register1.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                rn=random.randint(100000,999999)
                global otp
                otp=rn
                image=qrcode.make("OTP:"+str(rn))
                print(otp)
                image.save("Static/images/shashank.png")
                request.session['username']=username
                request.session['password']=password
                return render(request,'Register/qrcode.html',{})
                
                # return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Register/login3.html', {})

# def verificationview(self,request,uidb64,token):
#     if request.method=='GET':
#         return HttpResponseRedirect('Register/login3.html')
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def check_otp(request):
    user_otp=request.POST.get("otp")
    if user_otp==str(otp):
        username=request.session['username']
        password=request.session['password']
        user = authenticate(username=username, password=password)
        login(request,user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('invalid otp')    
