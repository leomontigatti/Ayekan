# Generated by Django 3.2.7 on 2021-09-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residency', '0003_auto_20210917_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='status',
            field=models.IntegerField(),
        ),
    ]
