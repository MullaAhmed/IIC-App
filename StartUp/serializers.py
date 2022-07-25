from rest_framework import serializers,fields
from .models import *

class StartUpProfileSerializer(serializers.ModelSerializer):

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

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Service
        fields=(
                'id','username',
                'service_name',
                'current_stage',
                'note',)

class StartUpAppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=StartUpAppointment
        fields=(
                'id','username',
                'start_up_appointment_date',
                'start_up_appointment_with',
                )

class ProjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProjectDetail
        fields=(
                'id','username',
                'project_stage',
                'project_summary',
                'prototype_details',
                'quaterly_plan')

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model=Team
        fields=(
                'id','username',
                'member_1',
                'member_2',
                'member_3',
                'member_4',
                'member_5',)


############
# Services #
############



class MessAndAccommodationSerializer(serializers.ModelSerializer):
    
        class Meta:
            model=MessAndAccommodation
            fields=(
                    'id','username',
                    'email',
                     'expected_duration_accommodation',
                     'number_of_people_accommodation',
                     'names_of_people_accommodation',
                     'other_remarks_accommodation',
                     'expected_duration_mess',
                     'number_of_people_mess',
                     'names_of_people_mess',
                     'other_remarks_mess',
                    )

class FinancialServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model=FinancialServices
        fields=(
                'id','username',
                'email',
                'item_name',
                'item_value',
                'quantity',
                'total_Value',
                'bill_attachment',
                'approval_attachment',
                'other_remarks',)

class ExitAndGraduationSerializer(serializers.ModelSerializer):

    class Meta:
        model=ExitAndGraduation
        fields=(
                'id','username',
                'email',
                'extension_time',
                'reason_for_extension',
                'progress_update',
                'other_remarks',)

class LabServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model=LabServices
        fields=(
                'id','username',
                'email',
                'equipment_required',
                'raw_material_required',
                'test',
                'duration',
                'number_of_people',
                'names_of_people',
                'other_remarks',)

class ProcurementServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProcurementService
        fields=(
                'id','username',
                'email',
                'item_name',
                'detailed_specification',
                'expected_unit_price',
                'required_quantity',
                'supplier_1',
                'supplier_2',
                'supplier_3',
                'supplier_4',
                'supplier_5',
                'other_remarks',)

class IPR_ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model=IPR_Services
        fields=(
                'id','username',
                'email',
                'type_of_IPR',
                'proposed_title',
                'IPR_document',
                'other_remarks',)