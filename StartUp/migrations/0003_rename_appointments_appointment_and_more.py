# Generated by Django 4.0.5 on 2022-06-04 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StartUp', '0002_rename_appointment_appointments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointments',
            new_name='Appointment',
        ),
        migrations.RenameModel(
            old_name='Project_Details',
            new_name='Project_Detail',
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
