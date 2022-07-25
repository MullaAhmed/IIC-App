from django.urls import path
from .views import *

urlpatterns = [
    path("StartUp-Profile/",StartUpProfileApiView.as_view()),
    path("Services/",ServiceApiView.as_view(),name="Service"),
    path("StartUpAppointment/",StartUpAppointmentApiView.as_view(),name="StartUpAppointment"),
    path("Project-Details/",ProjectDetailApiView.as_view(),name="Project"),
    path("Team/",TeamApiView.as_view(),name="Team"),


    path("StartUp-Profile/<slug:username>/",StartUpProfileDetailApiView.as_view()),
    path("Services/<slug:username>/",ServiceDetailApiView.as_view(),name="Service"),
    path("StartUpAppointment/<slug:username>/",StartUpAppointmentDetailApiView.as_view(),name="StartUpAppointment"),
    path("Project-Details/<slug:username>/",ProjectDetailDetailApiView.as_view(),name="Project"),
    path("Team/<slug:username>/",TeamDetailApiView.as_view(),name="Team"),


    path("Mess-And-Accommodation/",MessAndAccommodationApiView.as_view()),
    path("Financial-Services/",FinancialServicesApiView.as_view()),
    path("Exit-And-Graduation/",ExitAndGraduationApiView.as_view()),
    path("Lab-Services/",LabServicesApiView.as_view()),
    path("Procurement-Service/",ProcurementServiceApiView.as_view()),
    path("IPR-Services/",IPR_ServicesApiView.as_view()),

    path("Mess-And-Accommodation/<slug:username>/",MessAndAccommodationDetailApiView.as_view()),
    path("Financial-Services/<slug:username>/",FinancialServicesDetailApiView.as_view()),
    path("Exit-And-Graduation/<slug:username>/",ExitAndGraduationDetailApiView.as_view()),
    path("Lab-Services/<slug:username>/",LabServicesDetailApiView.as_view()),
    path("Procurement-Service/<slug:username>/",ProcurementServiceDetailApiView.as_view()),
    path("IPR-Services/<slug:username>/",IPR_ServicesDetailApiView.as_view()),

    ]