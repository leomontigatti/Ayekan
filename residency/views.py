# Residency views.

# Django.
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
# from django.core.serializers.json import DjangoJSONEncoder
import json

# Models.
from residency.models import *

# Forms.
from residency.forms import *


# ------------------------------------------ Resident stuff ------------------------------------------


def resident_search(request):
    # Looks up for a resident with given data.
    
    if request.method == 'POST':
        imput_field = request.POST['imput_field']
        resident_list = Resident.objects.filter(Q(nickname__icontains = imput_field) |
            Q(first_name__icontains = imput_field) |
            Q(last_name__icontains = imput_field))
        context = {
            'resident_list': resident_list,
            'active_page': 'resident',
        }
        return render(request, 'resident/search.html', context)
    else:
        return render(request, 'resident/list.html', {'active_page': 'resident'})


class ResidentListView(ListView):
    # Shows a list of resident objects.
    
    model = Resident
    context_object_name = 'resident_list'
    template_name = 'resident/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'resident'
        # context['qs_json'] = json.dumps(list(Resident.objects.values()),indent=4, sort_keys=True, cls=DjangoJSONEncoder)
        return context


class ResidentCreateView(SuccessMessageMixin, CreateView):
    # Creates a new resident.
    
    form_class = ResidentCreateForm
    template_name = 'resident/create.html'
    success_message = 'Residente creado con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'resident'
        return context


class ResidentUpdateView(SuccessMessageMixin, UpdateView):
    # Updates an existing resident.
    
    model = Resident
    form_class = ResidentCreateForm
    template_name = 'resident/update.html'
    success_message = 'Residente editado con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'resident'
        return context


class ResidentDetailView(DetailView):
    # Shows a resident detail for printing.
    
    model = Resident
    template_name = 'resident/detail.html'
    context_object_name = 'resident'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'resident'
        return context


# ------------------------------------------ Medication stuff ------------------------------------------


def medication_search(request):
    # Looks up for a medication with given data.
    
    if request.method == 'POST':
        imput_field = request.POST['imput_field']
        medication_list = Medication.objects.filter(Q(drug_name__icontains = imput_field) |
            Q(commercial_name__icontains = imput_field))
        context = {
            'medication_list': medication_list,
            'active_page': 'medication',
        }
        return render(request, 'medication/list.html', context)
    else:
        return render(request, 'medication/search.html', {'active_page': 'medication'})


class MedicationListView(ListView):
    # Shows a list of medication objects.
    
    model = Medication
    context_object_name = 'medication_list'
    template_name = 'medication/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'medication'
        return context


class MedicationCreateView(SuccessMessageMixin, CreateView):
    # Creates a new medication.
    
    form_class = MedicationCreateForm
    template_name = 'medication/create.html'
    success_message = 'Medicación creada con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'medication'
        return context


class MedicationUpdateView(SuccessMessageMixin, UpdateView):
    # Updates an existing medication.
    
    model = Medication
    form_class = MedicationCreateForm
    template_name = 'medication/update.html'
    success_message = 'Medicación editada con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'medication'
        return context


# ------------------------------------------ Prescription stuff ------------------------------------------


def prescription_search(request):
    # Looks up for a prescription with given data.
    
    if request.method == 'POST':
        imput_field = request.POST['imput_field']
        prescription_list = Prescription.objects.filter(Q(medication__commercial_name__icontains = imput_field) |
            Q(medication__drug_name__icontains = imput_field) | Q(resident__first_name__icontains = imput_field) | 
            Q(resident__last_name__icontains = imput_field) | Q(resident__nickname__icontains = imput_field) | 
            Q(prescription_date__icontains = imput_field))
        context = {
            'prescription_list': prescription_list,
            'active_page': 'prescription',
        }
        return render(request, 'prescription/list.html', context)
    else:
        return render(request, 'prescription/search.html', {'active_page': 'prescription'})


class PrescriptionListView(ListView):
    # Shows a list of all prescription objects.
    
    model = Prescription
    context_object_name = 'prescription_list'
    template_name = 'prescription/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'prescription'
        return context
    

class ResidentPrescriptionListView(ListView):
    # Shows a list of prescription objects related to a resident.
    
    template_name = 'prescription/list.html'
    
    def get_queryset(self):
        prescription_list = Prescription.objects.filter(resident_id = self.kwargs['pk'])
        return prescription_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'prescription'
        return context


class PrescriptionCreateView(SuccessMessageMixin, CreateView):
    # Creates a new prescription.
    
    form_class = PrescriptionCreateForm
    template_name = 'prescription/create.html'
    success_message = 'Prescripción creada con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'prescription'
        return context


class PrescriptionUpdateView(SuccessMessageMixin, UpdateView):
    # Updates an existing prescription.
    
    model = Prescription
    form_class = PrescriptionCreateForm
    template_name = 'prescription/update.html'
    success_message = 'Prescripción editada con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'prescription'
        return context
    

class PrescriptionDetailView(DetailView):
    # Shows a prescription detail for printing.
    
    model = Prescription
    template_name = 'prescription/detail.html'
    context_object_name = 'prescription'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'prescription'
        return context


# ------------------------------------------ Stock stuff ------------------------------------------


class StockCreateView(SuccessMessageMixin, CreateView):
    # Creates a new stock.
    
    form_class = StockCreateForm
    template_name = 'stock/create.html'
    success_message = 'Stock creado con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'stock'
        return context


class StockListView(ListView):
    # Shows a list of stock objects related to a prescription.
    
    model = Stock
    context_object_name = 'stock_list'
    template_name = 'stock/list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'stock'
        return context


class StockDetailView(DetailView):
    # Shows a prescription detail for printing.
    
    model = Prescription
    template_name = 'stock/detail.html'
    context_object_name = 'prescription'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'stock'
        return context


# ------------------------------------------ Tutor stuff ------------------------------------------


class TutorCreateView(SuccessMessageMixin, CreateView):
    # Creates a new tutor.
    
    form_class = TutorCreateForm
    template_name = 'tutor/create.html'
    
    def get_success_url(self):
        return reverse('resident_create')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'resident'
        return context


class TutorUpdateView(SuccessMessageMixin, UpdateView):
    # Updates an existing tutor.
    
    model = Tutor
    form_class = TutorCreateForm
    template_name = 'tutor/update.html'
    success_message = 'Tutor editado con éxito!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'resident'
        return context
