# Generated by Django 4.0.5 on 2022-06-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StartUp', '0003_rename_appointments_appointment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_detail',
            name='quaterly_plan',
            field=models.TextField(verbose_name='Quaterly Plans'),
        ),
    ]
