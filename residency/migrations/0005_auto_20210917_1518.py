# Generated by Django 3.2.7 on 2021-09-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residency', '0004_alter_resident_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='gender',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resident',
            name='id_type',
            field=models.IntegerField(),
        ),
    ]
