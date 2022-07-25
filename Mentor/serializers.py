from rest_framework import serializers,fields
from .models import *
from StartUp.models import *

class MentorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=MentorProfile
        fields=(
                'id',
                'username',
                'image',
                'position',
                'experties', 
                'mail',
                'number',
                'other_information',)

class MentorAppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=MentorAppointment
        fields=(
                'id','username',
                'appointment_date',
                'appointment_with',
                )


class MentorStartUpProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=StartUpProfile
        fields=(
                'id','username',
                'image',
                'ipr_details',
                'awards_and_recognition', 
                'employees',
                'finances',
                'mentor_feedback',
                'mentor_minutes',)