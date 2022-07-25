from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import *
from .models import *
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class AdminInquiryApiView(ListCreateAPIView):
    serializer_class=AdminInquirySerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return AdminInquiry.objects.all()


class AdminDashboardApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=AdminDashboardSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)
    lookup_field=('username')
    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return AdminDashboard.objects.all()


class AdminProfileApiView(ListCreateAPIView):
    serializer_class=AdminProfileSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return AdminProfile.objects.filter(username=self.request.user)

class AdminAppointmentApiView(ListCreateAPIView):
    serializer_class=AdminAppointmentSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')
    def perform_create(self, serializer):
      
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return AdminAppointment.objects.filter(username=uid)

class EventApiView(ListCreateAPIView):
    serializer_class=EventSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Event.objects.filter(created_by=self.request.user)

#
# Fetch 1 Update and delete
#

class AdminProfileDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=AdminProfileSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)
    lookup_field=('username')

    def get_queryset(self):
        return AdminProfile.objects.filter(username=self.request.user)

class AdminAppointmentDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=AdminAppointmentSerializer
    permission_classes=(IsAuthenticated,)
    lookup_field=('username')

    def get_queryset(self):
        uid = self.kwargs.get(self.lookup_field)
        return AdminAppointment.objects.filter(username=uid).all()

class EventDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=EventSerializer
    permission_classes=(IsAuthenticated,IsAdminUser)
    lookup_field=('username')

    def get_queryset(self):
        return Event.objects.filter(created_by=self.request.user)


class AllEventDetailApiView(viewsets.ModelViewSet):
   queryset = Event.objects.all()
   serializer_class = EventSerializer

