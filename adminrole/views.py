from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from adminrole.models import adminrole
from student.models import student
from faculty.models import faculty
from student.models import studentresult
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

	

def adminenroll(req):
	adm=adminrole()
	encryptedpassword=make_password(req.POST['password'])
	adm.name=req.POST.get("name")
	adm.email=req.POST.get("emailid")
	adm.password=encryptedpassword
	adm.mobileno=req.POST.get("mobileno")
	adm.save()
	messages.success(req,'Admin Added Successfully')
	return render(req,'admmessage.html')

def deleteadm(req):
    email=req.GET.get("email")
    deladm=adminrole.objects.get(email=email)
    deladm.delete()
    messages.success(req,'Admin Deleted Successfully')
    #return redirect('http://127.0.0.1:8000/checkrole')
    return render(req,'admmessage.html')

def admpass(req):
	if req.method=="GET":
		email=req.GET.get("email")
		cpass=adminrole.objects.get(email=email)
		cpass=adminrole.objects.filter(email=email)
		return render(req,'admpass.html',{'cpass':cpass})
	else:
		email=req.GET.get("email")
		encryptedpassword=make_password(req.POST['password'])
		cpass=adminrole.objects.get(email=email)
		cpass.password=encryptedpassword
		cpass.save()
		return redirect('/checkrole')

def modadm(req):
	if req.method=="GET":
		email=req.GET.get("email")
		modadm=adminrole.objects.get(email=email)
		modadm=adminrole.objects.filter(email=email)
		return render(req,'modadmin.html',{'modadm':modadm})
	else:
		encryptedpassword=make_password(req.POST['password'])
		email=req.GET.get("email")
		modadm2=adminrole.objects.get(email=email)
		modadm2.name=req.POST.get("name")
		modadm2.mobileno=req.POST.get("mobileno")
		modadm2.password=encryptedpassword
		modadm2.save()
		"""modfac2.faculty.object.all()"""
		return render(req,'admmessage.html')


def uploadadmimg(req):
	if req.method=="GET":
		email=req.GET.get("email")
		img=adminrole.objects.get(email=email)
		img=adminrole.objects.filter(email=email)
		return render(req,'admimage.html',{'img':img})
	else:
		email=req.GET.get("email")
		img2=adminrole.objects.get(email=email)
		img2.image=req.FILES['image']
		img2.save()
		return render(req,'admmessage.html')
