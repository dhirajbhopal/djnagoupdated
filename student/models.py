from django.db import models
import os
import datetime
# Create your models here.

def filepath(req,filename):
   old_filename = filename
   timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
   filename= "%s%s" % (timeNow,old_filename)
   return os.path.join('uploads/',filename)

   
class student(models.Model):
	rollno=models.CharField(max_length=15,null=True,unique=True)
	name=models.CharField(max_length=15,null=False)
	lastname=models.CharField(max_length=15,null=False)
	fathername=models.CharField(max_length=15,null=False)
	fatherlastname=models.CharField(max_length=15,null=False)
	email=models.CharField(max_length=40,null=False,unique=True)
	password=models.CharField(max_length=100,null=False)
	mobileno=models.CharField(max_length=15,null=False,unique=True)
	gender=models.CharField(max_length=15,null=False)
	dob=models.DateField()
	doa=models.DateField(null=True)
	address=models.CharField(max_length=100,null=False)
	image=models.ImageField(upload_to=filepath,null=True,blank=True)

def __str__(self):
	return self.name



class studentresult(models.Model):
	email=models.CharField(max_length=15,null=True,unique=True)
	rollno=models.CharField(max_length=15,null=False)
	branch=models.CharField(max_length=15,null=False)
	semester=models.CharField(max_length=15,null=False)
	subject=models.CharField(max_length=15,null=False)
	subjectcode=models.CharField(max_length=15,null=False)
	fullmark=models.IntegerField(null=False)
	obtainmark=models.IntegerField(null=False)
	pracfullmark=models.IntegerField(null=False)
	pracobtmark=models.IntegerField(null=False)
	totalmark=models.IntegerField(null=False)
	result=models.CharField(max_length=15,null=False)
	CGPA=models.CharField(max_length=5,null=False)
	resultdate=models.DateField()


def __str__(self):
	return self.rollno







