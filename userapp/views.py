from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date
from . import models,forms


# Create your views here. # These are the menu links available 
#in the navigation bar, for every link, we create urls seperately
def home_page_view(request):
    return render(request, 'index.html')
def otp(request):
    return render(request, 'otp.html')
def recipes_page_view(request):
    return render(request, 'recipes.html')
def veg_recipes_page_view(request):
    return render(request, 'veg.html')
def nonveg_recipes_page_view(request):
    return render(request, 'nonveg.html')
def samosa(request):
    return render(request, 'samosa.html')
def chillipaneer(request):
    return render(request, 'chillipaneer.html')
def dabeli(request):
    return render(request, 'dabeli.html')
def vegfriedrice(request):
    return render(request, 'vegfriedrice.html')
def phulka(request):
    return render(request, 'phulka.html')
def vegbiryani(request):
    return render(request, 'vegbiryani.html')
def gulabjamun(request):
    return render(request, 'gulabjamun.html')
def kheer(request):
    return render(request, 'kheer.html')
def jalebi(request):
    return render(request, 'jalebi.html')
def chickenspringrolls(request):
    return render(request, 'chickenspringrolls.html')
def muttonkeemasamosa(request):
    return render(request, 'muttonkheemasamosa.html')
def chilliprawns(request):
    return render(request, 'chilliprawns.html')
def butterchicken(request):
    return render(request, 'butterchicken.html')
def chickenbiryani(request):
    return render(request, 'chickenbiryani.html')
def muttonbiryani(request):
    return render(request, 'muttonbiryani.html')
def login_page_view(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('otp')
        else:
            return HttpResponse("not saved")
    else:
        return render(request, 'login.html', {'form' : form})