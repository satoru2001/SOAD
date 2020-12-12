from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from contactApp.forms import FeedbackForm
# Create your views here.
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=True)
            save_it.save()
            subject = 'Regarding feedback submitted'
            message = 'Hello! {} ,\nYour feedback is in progress!\nThank you for providing your valuable feedback.\nIt matters a lot for us.\n\nThanks\nSatya Lokathantra team.'.format(save_it.user_name)
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.user_mail]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            return render(request,'feedback/thanks.html')
    else:
        form = FeedbackForm()
    return render(request,'feedback/form.html',{'form': form})