from django.shortcuts import render , redirect, get_object_or_404
from .models import Doctor, Patient
from .models import DoctorFrom, PatientFrom
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView

class IndexView(ListView):
    template_name = "board/index.html"
    context_object_name = "patient_list"

    def get_queryset(self):
        return Patient.objects.filter(waiting_status=True)


class PatientCreateView(CreateView):
    model = Patient
    fields = ["doctor", "patient_name"]
    success_url = reverse_lazy("board:index")


class PatientDetailView(DeleteView):
    template_name = "board/patient_detail.html"
    model = Patient



class PatientUpdataView(UpdateView):
    model = Patient
    fields = ["patient_name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("board:index")


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy("board:index")



class DoctorDetialView(DetailView):
    template_name = "board/doctor_detial.html"
    model = Doctor






