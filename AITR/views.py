from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.shortcuts import redirect
from student.models import student
from student.models import studentresult
from faculty.models import faculty
from adminrole.models import adminrole
from faculty.models import faculty
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import logout

def home(request):
	return render(request,'default.html')


def signup(request):
	return render(request,'usersignup.html')


def info(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contactus.html')

def study(request):
	return render(request,'courses.html')

def resetpasstemp(req):
	return render(req,'resetpasstemp.html')
	


def checkrole(req):
	email = req.COOKIES.get('emailid')
	role = req.COOKIES.get('role')
	password = req.COOKIES.get('password')
	role=req.POST.get("role")
	email=req.POST.get("emailid")
	password=req.POST.get("password")
	if (role=="student"):
		rec=student()
		rec2=student.objects.filter(email=email)
		showres=studentresult.objects.filter(email=email)
		for i in rec2:
			check=check_password(password, i.password)
			if (i.email==email and check==True):
				recipient_list = i.email
				#send_mail(' Student Login Successfull ','You Have logged in Successfully','dhiraj.cybrom@gmail.com',[recipient_list])
				return render(req,'stuprofile.html',{'rec2':rec2 ,'showres':showres})
			else:
				messages.success(req,'Wrong user name or password!!!')
				return redirect('/')
		messages.success(req,'Student Does not Exist')
		return redirect('/')

	elif (role=="faculty"):
		fac=faculty()
		fac2=faculty.objects.filter(email=email)
		for i in fac2:
			  check=check_password(password, i.password)
			  if (i.email==email and check==True):
			  	recipient_list = i.email
			  	#send_mail('Faculty Login Successfull ','You Have logged in Successfully','dhiraj.cybrom@gmail.com',[recipient_list])			  	
			  	return render(req,'facprofile.html',{'fac2':fac2})
			  else:
			  	messages.success(req,'Wrong user name or password!!!')
			  	return redirect('/')
		messages.success(req,'Faculty Does not Exist')
		return redirect('/')
		

	elif (role=="admin"):
		amd2=adminrole()
		stud=student()
		stu=studentresult()
		fac=faculty()
		sturec=studentresult.objects.all()
		studrec=student.objects.all()
		fac2=faculty.objects.all()
		adm3=adminrole.objects.all()
		adm2=adminrole.objects.filter(email=email)
		for i in adm2:
			check=check_password(password, i.password)
			if (i.email==email and check==True):
				recipient_list = i.email
				#send_mail('Admin Login Successfull ','You Have logged in Successfully','dhiraj.cybrom@gmail.com',[recipient_list])
				return render(req,'admprofile.html',{'adm3':adm3, 'adm2':adm2,'sturec':sturec,'studrec':studrec,'fac2':fac2})
			else:
				messages.success(req,'Wrong user name or password!!!')
				return redirect('/')
	messages.success(req,'Admin Does not Exist')
	return redirect('/')

	

def logout_view(req):
	req.session['data']=""
	return redirect('/?next=/logout_view')








