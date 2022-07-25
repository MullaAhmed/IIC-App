from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,BasePermission
# Create your views here.
from django.shortcuts import render,HttpResponse
class IsMentorUser(BasePermission):

    def has_permission(self, request, view):
        request.user and request.user.is_mentor
        return bool(request.user and request.user.is_mentor)



class MentorProfileApiView(ListCreateAPIView):
    serializer_class=MentorProfileSerializer
    permission_classes=(IsAuthenticated,IsMentorUser)

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return MentorProfile.objects.filter(username=self.request.user)

#
# Fetch 1 Update and delete
#

class MentorProfileDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=MentorProfileSerializer
    permission_classes=(IsAuthenticated,IsMentorUser)
    lookup_field=('username')

    def get_queryset(self):
        return MentorProfile.objects.filter(username=self.request.user)



class AllMentorProfileApiView(viewsets.ModelViewSet):
   queryset = MentorProfile.objects.all()
   serializer_class = MentorProfileSerializer

