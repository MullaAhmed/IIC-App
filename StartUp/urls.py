from django.urls import path
from .views import *

urlpatterns = [
    path("<slug:name>/StartUp-Profile",startup_profile,name="Profile"),
    path("<slug:name>/Service",service,name="Services"),
    path("<slug:name>/Appointment",appointment,name="Appointments"),
    path("<slug:name>/Project-Details",project_detail,name="Project Details"),
    path("<slug:name>/Team",team,name="Team"),
]
