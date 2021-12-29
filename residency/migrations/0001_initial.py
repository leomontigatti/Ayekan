# Generated by Django 3.2.8 on 2021-11-09 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=100)),
                ('commercial_name', models.CharField(max_length=200)),
                ('pharmaceutical_form', models.CharField(choices=[('Cápsulas', 'Cápsulas'), ('Crema', 'Crema'), ('Dosis', 'Dosis'), ('Gel', 'Gel'), ('Gotas', 'Gotas'), ('Inyectable', 'Inyectable'), ('Jarabe', 'Jarabe'), ('Loción', 'Loción'), ('Paff', 'Paff'), ('Parche', 'Parche'), ('Polvo', 'Polvo'), ('Pomada', 'Pomada'), ('Suplemento', 'Suplemento'), ('Otro', 'Otro')], default='Otro', max_length=50)),
                ('amount', models.FloatField()),
                ('measurement_unit', models.CharField(choices=[('Unidad', 'Unidad'), ('mg', 'mg'), ('g', 'g'), ('kg', 'kg'), ('ml', 'ml')], default='Unidad', max_length=10)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='residency/pictures/medication')),
            ],
            options={
                'ordering': ['commercial_name', 'amount'],
            },
        ),
        migrations.CreateModel(
            name='Prepaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.FloatField(default=0)),
                ('before_lunch', models.FloatField(default=0)),
                ('lunch', models.FloatField(default=0)),
                ('tea', models.FloatField(default=0)),
                ('before_dinner', models.FloatField(default=0)),
                ('dinner', models.FloatField(default=0)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('medication_status', models.CharField(choices=[('Activo', 'Activo'), ('Suspendido', 'Suspendido'), ('SOS', 'SOS')], default='Activo', max_length=50)),
                ('prescription_date', models.DateField(help_text='Formato AAAA-mm-dd')),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('in_pillbox', models.BooleanField(default=False)),
                ('floor', models.CharField(choices=[('Planta baja', 'Planta baja'), ('Planta alta', 'Planta alta')], default='Planta baja', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Otro', 'Otro'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Otro', max_length=50)),
                ('citizenship', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(choices=[('Casado/a', 'Casado/a'), ('Divorciado/a', 'Divorciado/a'), ('Viudo/a', 'Viudo/a'), ('Soltero/a', 'Soltero/a')], default='Casado/a', max_length=50)),
                ('id_type', models.CharField(choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE'), ('Pasaporte', 'Pasaporte')], default='DNI', max_length=50)),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('phone_number', models.CharField(help_text='Código de area sin 0 y número sin 15', max_length=200)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_info', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliable', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='residency.medication')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='residency.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Activo', 'Activo'), ('Baja', 'Baja')], default='Activo', max_length=50)),
                ('admission_date', models.DateField(auto_now_add=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('Otro', 'Otro'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default='Otro', max_length=50)),
                ('citizenship', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(choices=[('Casado/a', 'Casado/a'), ('Divorciado/a', 'Divorciado/a'), ('Viudo/a', 'Viudo/a'), ('Soltero/a', 'Soltero/a')], default='Casado/a', max_length=50)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('id_type', models.CharField(choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE'), ('Pasaporte', 'Pasaporte')], default='DNI', max_length=50)),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='resident/photos')),
                ('room_type', models.CharField(choices=[('Doble', 'Doble'), ('Simple', 'Simple'), ('Triple', 'Triple'), ('Simple B/Privado', 'Simple B/Privado')], default='Simple', max_length=50)),
                ('floor', models.CharField(choices=[('Planta baja', 'Planta baja'), ('Planta alta', 'Planta alta')], default='Planta baja', max_length=50)),
                ('bed', models.CharField(blank=True, max_length=50, null=True)),
                ('room_number', models.CharField(blank=True, max_length=50, null=True)),
                ('drop_date', models.DateField(blank=True, null=True)),
                ('re_enter_date', models.DateField(blank=True, null=True)),
                ('decease_date', models.DateField(blank=True, null=True)),
                ('affiliation_number', models.CharField(max_length=100)),
                ('vaccines', models.TextField(blank=True, max_length=500, null=True)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('weight', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('bmi', models.CharField(blank=True, max_length=50, null=True)),
                ('survival_certificate', models.BooleanField(default=False)),
                ('prepaid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='residency.prepaid')),
                ('tutor', models.ManyToManyField(to='residency.Tutor')),
            ],
            options={
                'ordering': ['nickname'],
            },
        ),
        migrations.AddField(
            model_name='prescription',
            name='authorized_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prescriptions', to='residency.staff'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prescriptions', to='residency.medication'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='resident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='residency.resident'),
        ),
    ]
