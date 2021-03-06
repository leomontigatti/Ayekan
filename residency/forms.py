# Residency forms.

# Django.
from django.forms import ModelForm, Textarea
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
            'birth_date': 'Fecha de nacimiento', 'gender': 'G??nero', 
            'citizenship': 'Nacionalidad', 'marital_status': 'Estado civil',
            'address': 'Domicilio', 'city': 'Ciudad',
            'id_type': 'Tipo de documento', 'id_number': 'N??mero de documento',
            'tutor': 'Tutor'
        }


class HealthInfoCreateForm(ModelForm):
    # Creates a form to add a resident's health information.
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-HealthInfoForm'
        self.helper.form_class = 'row-g3 needs-validation'
        self.helper.form_method = 'post'
        self.helper.attrs = {'novalidate' : ''}
        self.helper.layout = Layout(
            Row(
                Column('prepaid', css_class = 'form-group col'),
                Column('affiliation_number', css_class = 'form-group col'),
                css_class = 'form-row'
            ),
            Row(
                Column('vaccines', css_class = 'form-group col-md'),
                Column('notes', css_class = 'form-group col-md'),
                css_class = 'form-row'
            ),
            Row(
                Column('weight', css_class = 'form-group col-md'),
                Column('height', css_class = 'form-group col-md'),
                Column('bmi', css_class = 'form-group col-md'),
                Column('survival_certificate', css_class = 'form-group col-md'),
                css_class = 'form-row'
            ),
        )
    
    
    class Meta:
        model = Resident
        fields = (
            'prepaid', 'affiliation_number', 'vaccines', 'notes', 'weight', 'height',
            'bmi', 'survival_certificate',
        )
        labels = {
            'prepaid': 'Obra social', 'affiliation_number': 'N??mero de afiliado',
            'vaccines': 'Vacunas', 'notes': 'Notas', 'weight': 'Peso', 'height': 
            'Altura', 'bmi': 'IMC', 'survival_certificate': 'Certificado de supervivencia'
        }
        widgets = {
            'vaccines': Textarea(attrs={'rows': 4, 'placeholder': 'Fecha y detalle'}),
            'notes': Textarea(attrs={'rows': 4})
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
            'pharmaceutical_form': 'Presentaci??n', 'measurement_unit': 'Unidad de medida', 
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
            'resident': 'Residente', 'floor': 'Piso', 'prescription_date': 'Fecha de prescripci??n',
            'medication': 'Nombre y dosis de la medicaci??n', 'medication_status': 'Estado',
            'in_pillbox': 'En pastillero', 'breakfast': 'Desayuno', 'lunch': 'Almuerzo', 
            'tea': 'Merienda', 'dinner': 'Cena', 'notes': 'Notas'
        }
        widgets = {
            # 'total_per_day': NumberInput(attrs = {'readonly': True})
            'notes': Textarea(attrs={'rows': 4})
        }


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
            'prescription': 'Prescripci??n del residente', 
            'medication': 'Medicaci??n', 'avaliable': 'Disponible'
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
                Column('first_name', css_class = 'form-group col-md'),
                Column('last_name', css_class = 'form-group col-md'),
                css_class = 'form-row'
            ),
            Row(
                Column('id_type', css_class = 'form-group col-md-2'),
                Column('id_number', css_class = 'form-group col-md'),
                Column('age', css_class = 'form-group col-md'),
                Column('gender', css_class = 'form-group col-md'),
                Column('marital_status', css_class = 'form-group col-md'),
                css_class = 'form-row',
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
            Row(
                Column('citizenship', css_class = 'form-group col-md-6'),
                Column('profession', css_class = 'form-group col-md-6'),
                css_class = 'form-row'
            ),
        )
    
    
    class Meta:
        model = Tutor
        fields = (
            'first_name', 'last_name', 'phone_number', 'email', 'billing_info', 'id_type',
            'address', 'city', 'age', 'gender', 'citizenship', 'marital_status', 'id_number',
            'profession'
        )
        labels = {
            'first_name': 'Nombre', 'last_name': 'Apellido', 'phone_number': 'N??mero de tel??fono',
            'email': 'Email', 'billing_info': 'CUIT facturaci??n', 'id_type': 'Tipo de documento',
            'address': 'Domicilio', 'city': 'Ciudad', 'age': 'Edad', 'gender': 'G??nero',
            'citizenship': 'Nacionalidad', 'marital_status': 'Estado civil', 'id_number':
            'N??mero de documento', 'profession': 'Profesi??n'
        }
