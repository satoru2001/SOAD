from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from donate.models import don_sub
import stripe
from datetime import datetime
stripe.api_key = "sk_test_51HlzX4Fk05w5rdX8Exiqg8oEBD8RJ9CHgs4PSXr3G9vQHsXaJo0i5FUOcjh9dLc8VnbhiKQDZwUpq22TQ2RzoIZg00BKQkJLTA"
# Create your views here.
def index(request):
    return render(request,'donate/index11.html')

def charge(request): 
    if request.method == 'POST':
       amount = int(request.POST['amount'])
       sub = request.POST['sub']
       if sub=='subscription':
           if not request.user.is_authenticated:
               return HttpResponseRedirect(reverse('Register:user_login'))
               
       customer = stripe.Customer.create(
           email = '111@11.11',
           source=request.POST['stripeToken']
        #    username = request.user.username 
       )

       charge = stripe.Charge.create(
           customer = customer,
           amount = amount*100,
           currency='inr',
           description=sub
       )

    if sub=='subscription':
        pay = don_sub(
            user = request.user,
            amount = amount,
            transaction_id = charge['id'],
            type = sub,
            date = datetime.now()
        )
        pay.save()
    
    else:
        pay = don_sub(
            user = None,
            amount = amount,
            transaction_id = charge['id'],
            type = sub,
            date = datetime.now()
        )
        pay.save()

    if sub=='subscription':
        return render(request,'donate/paymentsuccess.html',context={'amount':amount})
    return redirect(reverse('donate:success', args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, 'donate/success.html', {'amount':amount})