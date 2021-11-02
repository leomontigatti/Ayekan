# Residency forms.

# Django.
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

# Models.
from residency.models import *


class ResidentCreateForm(ModelForm):
    # Creates a form to add a new resident.
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ResidentForm'
        self.helper.form_class = 'row-g3 needs-validation'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate' : ''}
        self.helper.layout = Layout(
            Row(Column('tutor', css_class = 'form-group col-md-6'),
                css_class = 'form-row'
            ),
            Row(
                Column('status', css_class = 'form-group col-md-2'),
                Column('picture', css_class = 'form-group col-md-10'),
                css_class = 'form-row'
            ),
            Row(
                Column('nickname', css_class = 'form-group col-md-2'),
                Column('first_name', css_class = 'form-group col-md-5'),
                Column('last_name', css_class = 'form-group col-md-5'),
                css_class = 'form-row'
            ),
            Row(
                Column('birth_date', css_class = 'form-group col-md-3'),
                Column('gender', css_class = 'form-group col-md-3'),
                Column('citizenship', css_class = 'form-group col-md-3'),
                Column('marital_status', css_class = 'form-group col-md-3'),
                css_class = 'form-row'
            ),
            Row(
                Column('address', css_class = 'form-group col-md-6'),
                Column('city', css_class = 'form-group col-md-6'),
                css_class = 'form-row'
            ),
            Row(
                Column('id_type', css_class = 'form-group col-md-2'),
                Column('id_number', css_class = 'form-group col-md-4'),
                css_class = 'form-row'
            ),
        )
    
    
    class Meta:
        model = Resident
        fields = (
            'status', 'picture', 'nickname', 'first_name', 'last_name', 'birth_date', 'gender',
            'citizenship', 'marital_status', 'address', 'city', 'id_type', 'id_number',
            'tutor'
        )
        labels = {
            'status': 'Estado', 'picture': 'Foto',
            'nickname': 'Apodo', 'first_name': 'Nombre', 'last_name': 'Apellido',
            'birth_date': 'Fecha de nacimiento', 'gender': 'Género', 
            'citizenship': 'Ciudadanía', 'marital_status': 'Estado civil',
            'address': 'Domicilio', 'city': 'Ciudad',
            'id_type': 'Tipo de documento', 'id_number': 'Número de documento',
            'tutor': 'Tutor'
        }


class MedicationCreateForm(ModelForm):
    # Creates a form to add a new medication.
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-MedicationForm'
        self.helper.form_class = 'row-g3 needs-validation'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate' : ''}
        self.helper.layout = Layout(
            Row(
                Column('drug_name', css_class = 'form-group col-md-6'),
                Column('commercial_name', css_class = 'form-group col-md-6'),
                css_class = 'form-row'
            ),
            Row(
                Column('pharmaceutical_form', css_class = 'form-group col-md-3'),
                Column('amount', css_class = 'form-group col-md-2'),
                Column('measurement_unit', css_class = 'form-group col-md-2'),
                Column('picture', css_class = 'form-group col-md-5'),
                css_class = 'form-row'
            ),
        )
    
    
    class Meta:
        model = Medication
        fields = (
            'drug_name', 'commercial_name', 'pharmaceutical_form', 'measurement_unit', 
            'picture', 'amount'
        )
        labels = {
            'drug_name': 'Nombre de la droga', 'commercial_name': 'Nombre comercial',
            'pharmaceutical_form': 'Presentación', 'measurement_unit': 'Unidad de medida', 
            'picture': 'Foto', 'amount': 'Cantidad'
        }


class PrescriptionCreateForm(ModelForm):
    # Creates a form to add a new prescription.
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-PrescriptionForm'
        self.helper.form_class = 'row-g3 needs-validation'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate' : ''}
        self.helper.layout = Layout(
            Row(
                Column('resident', css_class = 'form-group col-md-5'),
                Column('floor', css_class = 'form-group col-md-2'),
                css_class = 'form-row'
            ),
            Row(
                Column('prescription_date', css_class = 'form-group col-md-3'),
                Column('medication', css_class = 'form-group col-md-5'),
                Column('medication_status', css_class = 'form-group col-md-2'),
                css_class = 'form-row'
            ),
            Row(
                Column('breakfast', css_class = 'form-group col-md-2'),
                Column('lunch', css_class = 'form-group col-md-2'),
                Column('tea', css_class = 'form-group col-md-2'),
                Column('dinner', css_class = 'form-group col-md-2'),
                Column('in_pillbox', css_class = 'form-group col-md-2 ml-5'),
                css_class = 'form-row'
            ),
            Row(
                Column('notes', css_class = 'form-group'),
                css_class = 'form-row'
            )
        )
    
    
    class Meta:
        model = Prescription
        fields = (
            'resident', 'floor', 'prescription_date', 'medication', 'medication_status',
            'in_pillbox', 'breakfast', 'lunch', 'tea', 'dinner', 'notes'
        )
        labels = {
            'resident': 'Residente', 'floor': 'Piso', 'prescription_date': 'Fecha de prescripción',
            'medication': 'Nombre y dosis de la medicación', 'medication_status': 'Estado',
            'in_pillbox': 'En pastillero', 'breakfast': 'Desayuno', 'lunch': 'Almuerzo', 
            'tea': 'Merienda', 'dinner': 'Cena', 'notes': 'Notas'
        }
        # widgets = {
        #     'total_per_day': forms.NumberInput(attrs = {'readonly': True})
        # }


class StockCreateForm(ModelForm):
    # Creates a form to add a new stock.
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-StockForm'
        self.helper.form_class = 'row-g3 needs-validation'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate' : ''}
        self.helper.layout = Layout(
            Row(
                Column('prescription', css_class = 'form-group col-md-6'),
                Column('medication', css_class = 'form-group col-md-6'),
                css_class = 'form-row'
            ),
            Row(
                Column('avaliable', css_class = 'form-group col-md-6')
            )
        )
    
    
    class Meta:
        model = Stock
        fields = (
            'prescription', 'medication', 'avaliable'
        )
        labels = {
            'prescription': 'Prescripción del residente', 
            'medication': 'Medicación', 'avaliable': 'Disponible'
        }


class TutorCreateForm(ModelForm):
    # Creates a form to add a new tutor.
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-TutorForm'
        self.helper.form_class = 'row-g3 needs-validation'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate' : ''}
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class = 'form-group col-md-5'),
                Column('last_name', css_class = 'form-group col-md-5'),
                css_class = 'form-row'
            ),
            Row(
                Column('phone_number', css_class = 'form-group col-md-4'),
                Column('email', css_class = 'form-group col-md-4'),
                Column('billing_info', css_class = 'form-group col-md-4'),
                css_class = 'form-row'
            ),
            Row(
                Column('address', css_class = 'form-group col-md-6'),
                Column('city', css_class = 'form-group col-md-6'),
                css_class = 'form-row'
            ),
        )
    
    
    class Meta:
        model = Tutor
        fields = (
            'first_name', 'last_name', 'phone_number', 'email', 'billing_info',
            'address', 'city'
        )
        labels = {
            'first_name': 'Nombre', 'last_name': 'Apellido', 'phone_number': 'Número de teléfono',
            'email': 'Email', 'billing_info': 'DNI / CUIT', 'address': 'Domicilio', 'city': 'Ciudad'
        }
