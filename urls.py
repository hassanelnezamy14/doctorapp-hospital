from django.urls import path
from . import views
app_name = "board"
urlpatterns = [
    path("", views.IndexView.as_view , name="index"),
    path("doctor/<int:pk>/", views.DoctorDetailView.as_view , name="doctor_detail"),
    path("patient/<int:pk>/", views.DoctorDetailView.as_view , name="patient_detail"),
    path(
        "patient/<int:pk>/edit",
        views.PatientUpdateView.as_view , 
        name="patient_update",
    ),
     path("patient/create", views.PatientCreateView.as_view , name="patient_create"),
     path("patient/<int:pk>/delete", views.PatientDeleteView.as_view , name="patient_delete"),

]