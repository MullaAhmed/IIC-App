from cgitb import lookup
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#
# Create and Fetch All
#

class StartUpProfileApiView(ListCreateAPIView):
    serializer_class=StartUpProfileSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return StartUpProfile.objects.all()


class ServiceApiView(ListCreateAPIView):
    serializer_class=ServiceSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return Service.objects.filter(username=self.request.user)


class StartUpAppointmentApiView(ListCreateAPIView):
    serializer_class=StartUpAppointmentSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return StartUpAppointment.objects.filter(username=self.request.user)

class ProjectDetailApiView(ListCreateAPIView):
    serializer_class=ProjectDetailSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return ProjectDetail.objects.filter(username=self.request.user)

class TeamApiView(ListCreateAPIView):
    serializer_class=TeamSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return Team.objects.filter(username=self.request.user)


#
# Fetch 1 Update and delete
#

class StartUpProfileDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=StartUpProfileSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return StartUpProfile.objects.filter(username=uid)


class ServiceDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=ServiceSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def get_queryset(self):
        return Service.objects.filter(username=self.request.user)

class StartUpAppointmentDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=StartUpAppointmentSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def get_queryset(self):
        return StartUpAppointment.objects.filter(username=self.request.user)

class ProjectDetailDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=ProjectDetailSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def get_queryset(self):
        return ProjectDetail.objects.filter(username=self.request.user)

class TeamDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=TeamSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def get_queryset(self):
        return Team.objects.filter(username=self.request.user)


############
# Services #
############

class MessAndAccommodationApiView(ListCreateAPIView):
    serializer_class=MessAndAccommodationSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return MessAndAccommodation.objects.filter(username=self.request.user)


class FinancialServicesApiView(ListCreateAPIView):
    serializer_class=FinancialServicesSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return FinancialServices.objects.filter(username=self.request.user)


class ExitAndGraduationApiView(ListCreateAPIView):
    serializer_class=ExitAndGraduationSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return ExitAndGraduation.objects.filter(username=self.request.user)

class LabServicesApiView(ListCreateAPIView):
    serializer_class=LabServicesSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return LabServices.objects.filter(username=self.request.user)


class ProcurementServiceApiView(ListCreateAPIView):
    serializer_class=ProcurementServiceSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return ProcurementService.objects.filter(username=self.request.user)


class IPR_ServicesApiView(ListCreateAPIView):
    serializer_class=IPR_ServicesSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return IPR_Services.objects.filter(username=self.request.user)

#
# Fetch 1 Update and delete
#


class MessAndAccommodationDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=MessAndAccommodationSerializer
    permission_classes=(IsAuthenticated,)

    lookup_field=('username')
    def get_queryset(self):
        return MessAndAccommodation.objects.filter(username=self.request.user)


class FinancialServicesDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=FinancialServicesSerializer
    permission_classes=(IsAuthenticated,)

    lookup_field=('username')
    def get_queryset(self):
        return FinancialServices.objects.filter(username=self.request.user)


class ExitAndGraduationDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=ExitAndGraduationSerializer
    permission_classes=(IsAuthenticated,)

    lookup_field=('username')
    def get_queryset(self):
        return ExitAndGraduation.objects.filter(username=self.request.user)

class LabServicesDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=LabServicesSerializer
    permission_classes=(IsAuthenticated,)

    lookup_field=('username')
    def get_queryset(self):
        return LabServices.objects.filter(username=self.request.user)


class ProcurementServiceDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=ProcurementServiceSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def get_queryset(self):
        return ProcurementService.objects.filter(username=self.request.user)


class IPR_ServicesDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=IPR_ServicesSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def get_queryset(self):
        return IPR_Services.objects.filter(username=self.request.user)

