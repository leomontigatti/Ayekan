# Residency urls.

# Django.
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Views.
from . import views


urlpatterns = [
    
    # Resident paths.
    path('resident/list/', views.ResidentListView.as_view(), name = 'resident_list'),
    path('resident/search/', views.resident_search, name = 'resident_search'),
    path('resident/create/', views.ResidentCreateView.as_view(), name = 'resident_create'),
    path('resident/<int:pk>/update/', views.ResidentUpdateView.as_view(), name = 'resident_update'),
    path('resident/<int:pk>/detail/', views.ResidentDetailView.as_view(), name = 'resident_detail'),
    
    # Medication paths.
    path('medication/search/', views.medication_search, name = 'medication_search'),
    path('medication/list/', views.MedicationListView.as_view(), name = 'medication_list'),
    path('medication/create/', views.MedicationCreateView.as_view(), name = 'medication_create'),
    path('medication/<int:pk>/update/', views.MedicationUpdateView.as_view(), name = 'medication_update'),
    
    # Prescription paths.
    path('prescription/search/', views.prescription_search, name = 'prescription_search'),
    path('prescription/list/', views.PrescriptionListView.as_view(), name = 'prescription_list'),
    path('prescription/create/', views.PrescriptionCreateView.as_view(), name = 'prescription_create'),
    path('prescription/<int:pk>/update/', views.PrescriptionUpdateView.as_view(), name = 'prescription_update'),
    path('prescription/<int:pk>/detail/', views.PrescriptionDetailView.as_view(), name = 'prescription_detail'),
    path('prescription/<int:pk>/list/', views.ResidentPrescriptionListView.as_view(), name = 'resident_prescription_list'),
    
    # Stock paths.
    path('stock/create/', views.StockCreateView.as_view(), name = 'stock_create'),
    path('stock/<int:pk>/detail/', views.StockDetailView.as_view(), name = 'stock_detail'),
    
    # Tutor paths.
    path('tutor/create/', views.TutorCreateView.as_view(), name = 'tutor_create'),
    path('tutor/<int:pk>/update/', views.TutorUpdateView.as_view(), name = 'tutor_update'),
    
]