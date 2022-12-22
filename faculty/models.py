from django.db import models
import os
import datetime

# Create your models here.
def filepathfac(req,filename):
   old_filename = filename
   timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
   filename= "%s%s" % (timeNow,old_filename)
   return os.path.join('uploads/',filename)
   
class faculty(models.Model):
	
	name=models.CharField(max_length=15,null=False)
	email=models.CharField(max_length=40,null=False)
	password=models.CharField(max_length=100,null=False)
	mobileno=models.CharField(max_length=15,null=False)
	subject=models.CharField(max_length=15,null=False)
	image=models.ImageField(upload_to=filepathfac,null=True,blank=True)


def __str__(self):
	f=self.name+self.email+str(self.password)+str(self.mobileno)+self.subject
	return f