from django.contrib import admin
from student.models import student


# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
	list_display=['id','rollno'  ,  'name'  , 
	 'lastname'  ,  'fathername'  ,  'fatherlastname'  ,  'email'  , 
	  'password'  ,  'mobileno'  ,  'gender'  ,  'dob'  ,  'doa'  ,  
	  'address'  ,  'image']