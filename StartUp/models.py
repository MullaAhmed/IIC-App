from django.db import models


# Create your models here.

class StartUp_Profile(models.Model):
    startup_name=models.CharField("Start Up Name",max_length=200)
    ipr_details=models.CharField("IPR Details",max_length=200)
    awards_and_recognition=models.CharField("Awards & Recognition",max_length=200)
    employees=models.IntegerField("Total Emplyees")
    finances=models.CharField("Financial Support",max_length=2000)
    # mentor=
    mentor_feedback=models.TextField("Mentor Feedback")

    def __str__(self):
        return '%s' % (self.startup_name)

service_stages = (
        ('Filled', 'Filled'),
        ('Being Processed', 'Being Processed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
service_names = (
        ('Accommodation', 'Accommodation'),
        ('Reimbursement', 'Reimbursement'),
        ('IPR', 'IPR'),
        ('Procurement', 'Procurement'),
        ('Lab', 'Lab'),
        ('Exit & Graduation', 'Exit & Graduation'),
    )

class Service(models.Model):
    startup_name = models.ForeignKey("StartUp_Profile", on_delete=models.CASCADE)
    service_name= models.CharField ("Service Name",max_length=20,choices=service_names,default="None")
    current_stage=models.CharField ("Current Stage",max_length=20,choices=service_stages)
    note=models.CharField("Note",max_length=200)

    def __str__(self):
        return '%s' % (self.startup_name)

class Appointment(models.Model):
    startup_name = models.ForeignKey("StartUp_Profile", on_delete=models.CASCADE)
    appointment_date=models.DateTimeField ("Date",max_length=200)
    appointment_with=models.CharField("Person",max_length=200)

    def __str__(self):
        return '%s' % (self.startup_name)

class Project_Detail(models.Model):
    startup_name = models.ForeignKey("StartUp_Profile", on_delete=models.CASCADE)
    project_stage=models.CharField("Project Stage",max_length=200)
    project_summary=models.CharField("Project Summary",max_length=200)
    prototype_details=models.CharField("Prototype Details",max_length=200)
    quaterly_plan=models.TextField("Quaterly Plans")
    
    def __str__(self):
        return '%s' % (self.startup_name)

class Team(models.Model):
    startup_name = models.ForeignKey("StartUp_Profile", on_delete=models.CASCADE)
    member_1=models.CharField("Member 1",max_length=200)
    member_2=models.CharField("Member 2",max_length=200,blank=True)
    member_3=models.CharField("Member 3",max_length=200,blank=True)
    member_4=models.CharField("Member 4",max_length=200,blank=True)
    member_5=models.CharField("Member 5",max_length=200,blank=True)
    
    def __str__(self):
        return '%s' % (self.startup_name)
