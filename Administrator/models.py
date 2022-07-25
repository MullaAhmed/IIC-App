from django.db import models
from Authentication.models import UserManager

# Create your models here.
class AdminInquiry(models.Model):
    username=models.CharField("Name",max_length=500) 
    service_name= models.CharField ("Service Name",max_length=50,default="None")

    def __str__(self):
        return '%s' % (self.username)


class AdminDashboard(models.Model):
    username=models.CharField("Name",default="IIC",max_length=500) 
    total_applications=models.IntegerField("Applications")
    newly_incubated_startups=models.IntegerField("Newly incubated")
    active_startups=models.JSONField("Active Startups")

    startups_till_date=models.JSONField("Startups Till Date")

    accumulated_startup_sales=models.IntegerField("Sales")
    total_startup_awards=models.IntegerField("Awards")
    total_employment_generated=models.JSONField("Total Employs")

    iic_awards=models.JSONField("IIC Awards")
    iic_events=models.JSONField("IIC Events")

    def __str__(self):
        return '%s' % (self.username)

class AdminProfile(models.Model):
    username=models.CharField("Name",max_length=500) 
    
    image=models.CharField("Profile Image",max_length=10000) 
    position=models.CharField("Position & Company",max_length=200)
    expertise=models.CharField("Expertise",max_length=1000)
    other_information=models.CharField("Other Information",max_length=200) 

    def __str__(self):
        return '%s' % (self.username)

class AdminAppointment(models.Model):
    username=models.CharField("Name",max_length=500) 
    admin_appointment_date=models.DateTimeField ("Date",max_length=200)
    admin_appointment_with=models.CharField("Person",max_length=200)

    def __str__(self):
        return '%s' % (self.username)

class Event(models.Model):
    created_by=models.CharField("Creators Name",max_length=200)
    event_name=models.CharField("Event Name",max_length=200)
    event_date=models.DateTimeField ("Date",max_length=200)
    event_brief=models.CharField("Description",max_length=2000)

    def __str__(self):
        return '%s' % (self.event_name)