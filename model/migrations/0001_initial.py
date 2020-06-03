# Generated by Django 3.0.6 on 2020-06-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientNumber', models.CharField(max_length=256)),
                ('StatePatientNumber', models.CharField(max_length=256)),
                ('DateAnnounced', models.CharField(max_length=256)),
                ('EstimatedOnsetDate', models.CharField(max_length=256)),
                ('AgeBracket', models.CharField(max_length=256)),
                ('Gender', models.CharField(max_length=2)),
                ('DetectedCity', models.CharField(max_length=50)),
                ('DetectedDistrict', models.CharField(max_length=50)),
                ('DetectedState', models.CharField(max_length=50)),
                ('Statecode', models.CharField(max_length=50)),
                ('CurrentStatus', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('ContractedfromwhichPatient', models.CharField(max_length=50)),
                ('Nationality', models.CharField(max_length=50)),
                ('Typeoftransmission', models.CharField(max_length=50)),
                ('StatusChangeDate', models.CharField(max_length=256)),
                ('Source_1', models.TextField()),
                ('Source_2', models.TextField()),
                ('Source_3', models.TextField()),
                ('BackupNotes', models.TextField()),
                ('Numcases', models.CharField(max_length=256)),
            ],
        ),
    ]