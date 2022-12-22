# Generated by Django 4.1 on 2022-11-13 09:49

import adminrole.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminrole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, null=True, upload_to=adminrole.models.filepathadmin)),
            ],
        ),
    ]