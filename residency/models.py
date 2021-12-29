# Residency models.

# Django.
from django.db import models
from django.urls import reverse
from datetime import date


class Prepaid(models.Model):
    # Prepaid model.
    
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200, blank = True)
    phone_number = models.CharField(max_length = 50, blank = True)
    
    def __str__(self) -> str:
        return self.name


class Resident(models.Model):
    # Resident model.
    
    status = models.CharField(max_length = 50, choices = [
        ('Activo', 'Activo'), ('Baja', 'Baja')], default = 'Activo')
    admission_date = models.DateField(auto_now_add = True)
    nickname = models.CharField(max_length = 50, blank = True, null = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    birth_date = models.DateField()
    gender = models.CharField(max_length = 50, choices = [
        ('Otro', 'Otro'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default = 'Otro')
    citizenship = models.CharField(max_length = 50, blank = True, null = True)
    marital_status = models.CharField(max_length = 50, choices = [
        ('Casado/a', 'Casado/a'), ('Divorciado/a', 'Divorciado/a'), ('Viudo/a', 'Viudo/a'), 
        ('Soltero/a', 'Soltero/a')], default = 'Casado/a')
    address = models.CharField(max_length = 100, blank = True, null = True)
    city = models.CharField(max_length = 100, blank = True, null = True)
    id_type = models.CharField(max_length = 50, choices = [
        ('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE'), ('Pasaporte', 'Pasaporte')], default = 'DNI')
    id_number = models.CharField(max_length = 20, unique = True)
    last_modified = models.DateTimeField(auto_now = True)
    picture = models.ImageField(upload_to = 'resident/photos', blank = True, null = True)
    tutor = models.ManyToManyField('Tutor')
    room_type = models.CharField(max_length = 50, choices = [
        ('Doble', 'Doble'), ('Simple', 'Simple'), ('Triple', 'Triple'), 
        ('Simple B/Privado', 'Simple B/Privado')], default = 'Simple')
    floor = models.CharField(max_length = 50, choices = [
        ('Planta baja', 'Planta baja'), ('Planta alta', 'Planta alta')], default = 'Planta baja')
    bed = models.CharField(max_length = 50, blank = True, null = True)
    room_number = models.CharField(max_length = 50, blank = True, null = True)
    drop_date = models.DateField(blank = True, null = True)
    re_enter_date = models.DateField(blank = True, null = True)
    decease_date = models.DateField(blank = True, null = True)
    
    # Health related information.
    
    prepaid = models.ForeignKey(Prepaid, on_delete = models.PROTECT, default = 1)
    affiliation_number = models.CharField(max_length = 100)
    vaccines = models.TextField(max_length = 500, blank = True, null = True)
    notes = models.TextField(max_length = 500, blank = True, null = True)
    weight = models.CharField(max_length = 50, blank = True, null = True)
    height = models.CharField(max_length = 50, blank = True, null = True)
    bmi = models.CharField(max_length = 50, blank = True, null = True)
    survival_certificate = models.BooleanField(default = False)
    
    def calculate_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    
    def tutor_list(self):
        return self.tutor.all()
    
    def __str__(self):
        if self.nickname:
            return f'{self.last_name}, {self.first_name} / {self.nickname}'
        else:
            return f'{self.last_name}, {self.first_name}'
    
    class Meta:
        ordering = ['nickname']
        
    # def get_absolute_url(self):
    #     resident = self.objects.latest('last_modified')
    #     return reverse('resident_detail', kwargs = {'int': resident.pk})


class Medication(models.Model):
    # Medication model.
    
    drug_name = models.CharField(max_length = 100)
    commercial_name = models.CharField(max_length = 200)
    pharmaceutical_form = models.CharField(max_length = 50, choices = [
        ('Cápsulas', 'Cápsulas'), ('Crema', 'Crema'), ('Dosis', 'Dosis'), ('Gel', 'Gel'), ('Gotas', 'Gotas'), 
        ('Inyectable', 'Inyectable'), ('Jarabe', 'Jarabe'), ('Loción', 'Loción'), ('Paff', 'Paff'), 
        ('Parche', 'Parche'), ('Polvo', 'Polvo'), ('Pomada', 'Pomada'), ('Suplemento', 'Suplemento'), 
        ('Otro', 'Otro')], default = 'Otro')
    amount = models.FloatField()
    measurement_unit = models.CharField(max_length = 10, choices = [
        ('Unidad', 'Unidad'), ('mg', 'mg'), ('g', 'g'), ('kg', 'kg'), ('ml', 'ml')], default = 'Unidad')
    picture = models.ImageField(upload_to = 'residency/pictures/medication', blank = True, null = True)
    
    def __str__(self):
        return f'{self.commercial_name} {self.amount} {self.measurement_unit}'
    
    class Meta:
        ordering = ['commercial_name', 'amount']
    
    def get_absolute_url(self):
        return reverse('medication_search')


class Prescription(models.Model):
    # Prescription model.
    
    resident = models.ForeignKey(Resident, on_delete = models.CASCADE, related_name = 'prescriptions')
    medication = models.ForeignKey(Medication, on_delete = models.PROTECT, related_name = 'prescriptions')
    breakfast = models.FloatField(default = 0)
    before_lunch = models.FloatField(default = 0)
    lunch = models.FloatField(default = 0)
    tea = models.FloatField(default = 0)
    before_dinner = models.FloatField(default = 0)
    dinner = models.FloatField(default = 0)
    notes = models.TextField(max_length = 500, blank = True, null = True)
    medication_status = models.CharField(max_length = 50, choices = [
        ('Activo', 'Activo'), ('Suspendido', 'Suspendido'), ('SOS', 'SOS')], default = 'Activo')
    prescription_date = models.DateField(help_text = 'Formato AAAA-mm-dd')
    last_modified = models.DateTimeField(auto_now_add = True)
    in_pillbox = models.BooleanField(default = False)
    floor = models.CharField(max_length = 50, choices = [
        ('Planta baja', 'Planta baja'), ('Planta alta', 'Planta alta')], default = 'Planta baja')
    authorized_by = models.ForeignKey('Staff', on_delete = models.PROTECT, related_name = 'prescriptions')
    
    def total_per_day(self):
        total = self.breakfast + self.lunch + self.tea + self.dinner
        return total
    
    def avaliable_stock(self):
        stock_list = Stock.objects.filter(prescription_id = self.pk)
        for stock in stock_list:
            if stock.avaliable > 0:
                return stock
            
    def stock_list(self):
        return  Stock.objects.filter(prescription_id = self.pk)
    
    def __str__(self):
        return f'{self.resident} - {self.medication}'    
    
    def get_absolute_url(self):
        return reverse('prescription_search')


class Stock(models.Model):
    # Stock model.
    
    prescription = models.ForeignKey(Prescription, on_delete = models.CASCADE, related_name = 'stock')
    medication = models.ForeignKey(Medication, on_delete = models.PROTECT, related_name = 'stock')
    avaliable = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
        
    def unit_converter(self):
        # Converts stock measurement unit to fit prescription's one.
        
        if self.prescription.medication.measurement_unit == 'mg':
            if self.medication.measurement_unit == 'g':
                return self.medication.amount * 1000
            elif self.medication.measurement_unit == 'kg':
                return self.medication.amount * 1000000
            else:
                return self.medication.amount
        elif self.prescription.medication.measurement_unit == 'g':
            if self.medication.measurement_unit == 'mg':
                return self.medication.amount / 1000
            elif self.medication.measurement_unit == 'kg':
                return self.medication.amount * 1000
            else:
                return self.medication.amount
        elif self.prescription.medication.measurement_unit == 'kg':
            if self.medication.measurement_unit == 'mg':
                return self.medication.amount / 1000000
            elif self.medication.measurement_unit == 'g':
                return self.medication.amount / 1000
            else:
                return self.medication.amount
        else:
            return self.medication.amount
            
    def meal_calculator(self):
        # Calculates the different meal dosis according to prescription's.
        
        meal_list = []
        for meal in [self.prescription.breakfast, self.prescription.lunch,
                     self.prescription.tea, self.prescription.dinner]:
            meal_list.append(meal / self.unit_converter())
        return meal_list
    
    def get_absolute_url(self):
        return reverse('prescription_search')


class Tutor(models.Model):
    # Tutor model.

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.CharField(max_length = 10, blank = True, null = True)
    gender = models.CharField(max_length = 50, choices = [
        ('Otro', 'Otro'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default = 'Otro')
    citizenship = models.CharField(max_length = 50, blank = True, null = True)
    marital_status = models.CharField(max_length = 50, choices = [
        ('Casado/a', 'Casado/a'), ('Divorciado/a', 'Divorciado/a'), ('Viudo/a', 'Viudo/a'), 
        ('Soltero/a', 'Soltero/a')], default = 'Casado/a')
    id_type = models.CharField(max_length = 50, choices = [
        ('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE'), ('Pasaporte', 'Pasaporte')], default = 'DNI')
    id_number = models.CharField(max_length = 20, unique = True)
    phone_number = models.CharField(max_length = 200, help_text = 'Código de area sin 0 y número sin 15')
    email = models.EmailField(max_length = 100, blank = True, null = True)
    profession = models.CharField(max_length = 100, blank = True, null = True)
    address = models.CharField(max_length = 100, blank = True, null = True)
    city = models.CharField(max_length = 100, blank = True, null = True)
    billing_info = models.CharField(max_length = 100, blank = True, null = True)
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse('resident_list')


class Staff(models.Model):
    # Staff model.
    
    name = models.CharField(max_length = 50)
