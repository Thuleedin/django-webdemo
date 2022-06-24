from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_gen.forms import SubscriptionModelForm
from .models import Subscription

# Create your views here.
def home(request):
    return render (request,'app_gen/home.html')

def about(request):
    return render (request,'app_gen/about.html')

def subscription(request):
    if request.method == 'POST':
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subscription_thankyou'))
    else:
        form = SubscriptionModelForm()
    context = {'form': form}
    return render(request, 'app_gen/subscription_form.html', context)

def subscription_thankyou(request):
    return render(request,'app_gen/subscription_thankyou.html')