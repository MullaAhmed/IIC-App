# Generated by Django 4.0.5 on 2022-06-04 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartUp_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=200, verbose_name='Start Up Name')),
                ('ipr_details', models.CharField(max_length=200, verbose_name='IPR Details')),
                ('awards_and_recognition', models.CharField(max_length=200, verbose_name='Awards & Recognition')),
                ('employees', models.IntegerField(verbose_name='Total Emplyees')),
                ('finances', models.CharField(max_length=2000, verbose_name='Financial Support')),
                ('mentor_feedback', models.TextField(verbose_name='Mentor Feedback')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_1', models.CharField(max_length=200, verbose_name='Member 1')),
                ('member_2', models.CharField(max_length=200, verbose_name='Member 2')),
                ('member_3', models.CharField(max_length=200, verbose_name='Member 3')),
                ('member_4', models.CharField(max_length=200, verbose_name='Member 4')),
                ('member_5', models.CharField(max_length=200, verbose_name='Member 5')),
                ('startup_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StartUp.startup_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_stage', models.DateTimeField(choices=[('Filed', 'Filed'), ('Being Processed', 'Being Processed'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=20, verbose_name='Current Stage')),
                ('note', models.CharField(max_length=200, verbose_name='Note')),
                ('startup_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StartUp.startup_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_stage', models.CharField(max_length=200, verbose_name='Project Stage')),
                ('project_summary', models.CharField(max_length=200, verbose_name='Project Summary')),
                ('prototype_details', models.CharField(max_length=200, verbose_name='Prototype Details')),
                ('quaterly_plan', models.TextField(verbose_name='Financial Support')),
                ('startup_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StartUp.startup_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField(max_length=200, verbose_name='Date')),
                ('appointment_with', models.CharField(max_length=200, verbose_name='Per son')),
                ('startup_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StartUp.startup_profile')),
            ],
        ),
    ]
