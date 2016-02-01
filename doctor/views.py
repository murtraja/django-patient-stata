from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from forms import DoctorRegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Patient
from datetime import datetime as dt

# Create your views here.
@login_required
def index(request):
    return render(request, 'doctor/index.html')

@csrf_exempt
def login_view(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        print "username:",username,"password",password
        return login_user(request, username, password)
    # so this is a get request, check if the user is already logged in
    if request.user.is_authenticated():
        return HttpResponseRedirect("/doctor/")
    else:
        return render(request, 'doctor/login.html')

def login_user(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/doctor/")
        else:
            return HttpResponse("Your account is disabled!")
    else:
        return HttpResponse('invalid login!')

@csrf_exempt
def register_view(request):
    if request.method=="POST":
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            username = request.POST.get('username')
            password = request.POST.get('password')
            print "username:",username,"password",password
            return login_user(request, username, password)
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor/register.html', {'form':form})


def logout_view(request):
    if request.user.is_authenticated(): #check if user is authenticated here
        logout(request)
        #return HttpResponse("You were logged out!")
    return HttpResponseRedirect('/doctor/login')


@csrf_exempt
def postTemp_view(request):
    if request.method=="POST":
        pname = request.POST.get('name')
        value = request.POST.get('data')
        print "name:",pname,", value:",value
        new_value=  Patient(patient_name=pname, temp_value  = float(value), time_recorded = dt.now())
        new_value.save()
        return HttpResponse("OK")
    else:
        return render(request, 'doctor/postTest.html')

@login_required
@csrf_exempt
def new_patient_view(request):
    if request.method == "POST":
        # save patient to database
        pname = request.POST.get('patient_name')
        new_patient = Patient(patient_name = pname, temp_value = 0, time_recorded = dt.now())
        return HttpResponseRedirect('/doctor/')
    else:
        return render(request, 'doctor/workstation_entry.html')

def analysis_view(request):
    return render(request, 'doctor/workstation_main.html')

def get_data_view(request):
    values = Patient.objects.all()
    print values
    size = len(values)
    recent = values[size-5:]
    mydict = {'data':[]}
    for rec in recent:
        print rec.temp_value
        mydict['data'].append(rec.temp_value)
    return JsonResponse(mydict)