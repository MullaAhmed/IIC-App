from django.db import models
from Authentication.models import User

# Create your models here.

class StartUpProfile(models.Model):
    username=models.CharField("Name",max_length=500,unique=True) 
    
    image=models.CharField("Profile Image",max_length=10000) 
    ipr_details=models.JSONField("IPR Details",max_length=200)
    awards_and_recognition=models.JSONField("Awards & Recognition",max_length=200)
    employees=models.IntegerField("Total Emplyees")
    finances=models.JSONField("Financial Support",max_length=2000)
    # mentor
    mentor_feedback=models.TextField("Mentor Feedback")
    mentor_minutes=models.TextField("Minutes of the Meeting")

    def __str__(self):
       
        return (self.username)

class Service(models.Model):
    username=models.CharField("Name",max_length=500) 
    
    service_name= models.CharField ("Service Name",max_length=50,default="None")
    current_stage=models.CharField ("Current Stage",max_length=50)
    note=models.CharField("Note",max_length=200)

    def __str__(self):
        return (self.username)


class StartUpAppointment(models.Model):
    username=models.CharField("Name",max_length=500) 
    
    start_up_appointment_date=models.DateTimeField ("Date",max_length=200)
    start_up_appointment_with=models.CharField("Person",max_length=200)

    def __str__(self):
        return (self.username)

class ProjectDetail(models.Model):
    username=models.CharField("Name",max_length=500) 
    
    project_stage=models.CharField("Project Stage",max_length=200)
    project_summary=models.CharField("Project Summary",max_length=200)
    prototype_details=models.CharField("Prototype Details",max_length=200)
    quaterly_plan=models.TextField("Quaterly Plans")
    
    def __str__(self):
        return (self.username)

class Team(models.Model):
    username=models.CharField("Name",max_length=500) 
    
    member_1=models.JSONField("Member 1",max_length=2000)
    member_2=models.JSONField("Member 2",max_length=2000,blank=True)
    member_3=models.JSONField("Member 3",max_length=2000,blank=True)
    member_4=models.JSONField("Member 4",max_length=2000,blank=True)
    member_5=models.JSONField("Member 5",max_length=2000,blank=True)
    
    def __str__(self):
        return (self.username)


############
# Services #
############

class MessAndAccommodation(models.Model):
    username=models.CharField("Name",max_length=500) 
    
    email=models.EmailField("Email")
    
    expected_duration_accommodation=models.IntegerField("Expected Duration of Accommodation (In Months)")
    number_of_people_accommodation=models.IntegerField("Number of people")
    names_of_people_accommodation=models.CharField("Names Of People",max_length=2000)
    other_remarks_accommodation=models.TextField("Remarks")

    expected_duration_mess=models.IntegerField("Expected Duration of Accommodation (In Months)")
    number_of_people_mess=models.IntegerField("Number of people")
    names_of_people_mess=models.CharField("Names Of People",max_length=2000)
    other_remarks_mess=models.TextField("Remarks")    

    def __str__(self):
        return (self.username)


class FinancialServices(models.Model):
    username=models.CharField("Name",max_length=500) 
    
    email=models.EmailField("Email")
    item_name=models.CharField("Item Name",max_length=200)
    item_value=models.FloatField("Item Value")
    quantity=models.IntegerField("Quantity")
    total_Value=models.FloatField("Total Value")
    bill_attachment=models.FileField("Bill Attachment",upload_to="Bill Attachment",blank=True)
    approval_attachment=models.FileField("Approval Attachment",upload_to="Approval Attachment",blank=True)
    other_remarks=models.TextField("Remarks")


    def __str__(self):
        return (self.username)
    

class ExitAndGraduation(models.Model):
    username=models.CharField("Name",max_length=500)
    email=models.EmailField("Email")
    extension_time=models.CharField("Extension Time",max_length=200)
    reason_for_extension=models.TextField("Reason For Extension")
    progress_update=models.CharField("Progress Update",max_length=200)
    other_remarks=models.TextField("Remarks")

    def __str__(self):
        return (self.username)


class LabServices(models.Model):
    username=models.CharField("Name",max_length=500)
    email=models.EmailField("Email")
    name_of_laboratory=models.CharField("Name Of Laboratory",max_length=200)
    equipment_required=models.CharField("Equipment Required",max_length=200)
    raw_material_required=models.CharField("Raw Material Required",max_length=200)
    test=models.CharField("Test",max_length=200)
    duration=models.CharField("Duration",max_length=200)
    number_of_people=models.IntegerField("Number of people")
    names_of_people=models.CharField("Names Of People",max_length=2000)
    other_remarks=models.TextField("Remarks")   

    def __str__(self):
        return (self.username)
  
class ProcurementService(models.Model):
    username=models.CharField("Name",max_length=500)
    email=models.EmailField("Email")   
    item_name=models.CharField("Item Name",max_length=200)
    detailed_specification=models.TextField("Detailed Specification")
    expected_unit_price=models.FloatField("Expected Unit Price")
    required_quantity=models.IntegerField("Required Quantity")
    supplier_1=models.CharField("Supplier 1",max_length=2000)
    supplier_2=models.CharField("Supplier 2",max_length=2000,blank=True)
    supplier_3=models.CharField("Supplier 3",max_length=2000,blank=True)
    supplier_4=models.CharField("Supplier 4",max_length=2000,blank=True)
    supplier_5=models.CharField("Supplier 5",max_length=2000,blank=True)
    other_remarks=models.TextField("Remarks")   

    def __str__(self):
        return (self.username)


class IPR_Services(models.Model):
    username=models.CharField("Name",max_length=500)
    email=models.EmailField("Email")
    type_of_IPR=models.CharField("Type of IPR",max_length=200)
    proposed_title=models.CharField("Proposed Title",max_length=200)
    IPR_document=models.FileField("IPR Document",upload_to="IPR Document",blank=True)
    other_remarks=models.TextField("Remarks")   

    def __str__(self):
        return (self.username)
