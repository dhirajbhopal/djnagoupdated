# Generated by Django 4.1 on 2022-11-12 16:26

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=15, null=True, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('fathername', models.CharField(max_length=15)),
                ('fatherlastname', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=15, unique=True)),
                ('gender', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('doa', models.DateField(null=True)),
                ('address', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=student.models.filepath)),
            ],
        ),
        migrations.CreateModel(
            name='studentresult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=15, null=True, unique=True)),
                ('rollno', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=15)),
                ('semester', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=15)),
                ('subjectcode', models.CharField(max_length=15)),
                ('fullmark', models.IntegerField()),
                ('obtainmark', models.IntegerField()),
                ('pracfullmark', models.IntegerField()),
                ('pracobtmark', models.IntegerField()),
                ('totalmark', models.IntegerField()),
                ('result', models.CharField(max_length=15)),
                ('CGPA', models.CharField(max_length=5)),
                ('resultdate', models.DateField()),
            ],
        ),
    ]
