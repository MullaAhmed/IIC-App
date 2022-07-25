from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Events', AllEventDetailApiView)


urlpatterns = [
    path("Admin-Dashboard/<slug:username>/",AdminDashboardApiView.as_view(),name="Dashboard"),
    path("Admin-Inquiry/",AdminInquiryApiView.as_view(),name="Inquiry"),

    path("Admin-Profile/",AdminProfileApiView.as_view(),name="Profile"),
    path("Admin-Events/",EventApiView.as_view(),name="Event"),
    path("AdminAppointments/<slug:username>/",AdminAppointmentApiView.as_view(),name="AdminAppointment"),
 
    path("Admin-Profile/<slug:username>/",AdminProfileDetailApiView.as_view(),name="Profile"),
    path("Admin-Events/<slug:username>/",EventDetailApiView.as_view(),name="Event"),
    path('', include(router.urls)),
    path("AdminAppointment/<slug:username>/",AdminAppointmentDetailApiView.as_view(),name="AdminAppointment"),
   
    ]