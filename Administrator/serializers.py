from rest_framework import serializers,fields
from .models import *

class AdminInquirySerializer(serializers.ModelSerializer):

    class Meta:
        model=AdminInquiry
        fields=(
                'id','username',
                'service_name',
    
                )

class AdminDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminDashboard
        fields=(
                'id',
                'username',
                'total_applications',
                'newly_incubated_startups',
                'active_startups',
                'startups_till_date',
                'accumulated_startup_sales',
                'total_startup_awards',
                'total_employment_generated',
                'iic_awards',
                'iic_events',
        )

class AdminProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=AdminProfile
        fields=(
                'id',
                'username',
                'image',
                'position',
                'expertise', 
                'other_information',)

class AdminAppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=AdminAppointment
        fields=(
                'id','username',
                'admin_appointment_date',
                'admin_appointment_with',
                )

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model=Event
        fields=(
                'id','created_by',
                'event_name',
                'event_date',
                'event_brief',)