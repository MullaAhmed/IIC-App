from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Mentor-Profiles', AllMentorProfileApiView)

urlpatterns = [
    path("Mentor-Profile/",MentorProfileApiView.as_view(),name="Profile"),
    
    path('', include(router.urls)),
 
    path("Mentor-Profile/<slug:username>/",MentorProfileDetailApiView.as_view(),name="Profile"),

   
    ]