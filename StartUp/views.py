from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def startup_profile(response,name):
    try:
        output=StartUp_Profile.objects.filter(startup_name=name).all().values()
    except:
        output={ }
    return(HttpResponse(output))
    

def service(response,name):
    try:
        id=StartUp_Profile.objects.filter(startup_name=name).all().values()[0]['id']    
        output=Service.objects.filter(startup_name_id=id).all().values()
    except:
        output={ }
    return(HttpResponse(output))

def appointment(response,name):
    try:
        id=StartUp_Profile.objects.filter(startup_name=name).all().values()[0]['id']    
        output=Appointment.objects.filter(startup_name_id=id).all().values()
    except:
        output={ }
    return(HttpResponse(output))

def project_detail(response,name):
    try:
        id=StartUp_Profile.objects.filter(startup_name=name).all().values()[0]['id']    
        output=Project_Detail.objects.filter(startup_name_id=id).all().values()
    except:
        output={ }
    return(HttpResponse(output))
 
def team(response,name):
    try:
        id=StartUp_Profile.objects.filter(startup_name=name).all().values()[0]['id']    
        output=Team.objects.filter(startup_name_id=id).all().values()
    except:
        output={ }
    return(HttpResponse(output))

 
 