from django.core import validators
from djanho import forms
from student models import student
class studentEnroll(forms.ModelForm):
	class Meta:
		model=student
		fields=['name' ,  'lastname' ,  'fathername' ,  'fatherlastname' ,  'email' ,  'password' ,  'mobileno' ,  'gender' ,  'dob',  'address']
