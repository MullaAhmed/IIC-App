from django.db import models

# Create your models here.
class MentorProfile(models.Model):
    username=models.CharField("Mentor Name",max_length=200)
    image=models.CharField("Profile Image",max_length=10000) 
    position=models.CharField("Position & Company",max_length=200)
    experties=models.CharField("Expertise",max_length=1000)
    mail=models.EmailField("Mail",default="temp@gmail.com")
    number = models.IntegerField("Number",blank=False,default=000)
    other_information=models.CharField("Other Information",max_length=200) 

    def __str__(self):
        return '%s' % (self.username)

class MentorAppointment(models.Model):
    username = models.CharField("Mentor_Profile", max_length=500)
    appointment_date=models.DateTimeField ("Date",max_length=200)
    appointment_with=models.CharField("Person",max_length=200)

    def __str__(self):
        return '%s' % (self.username)