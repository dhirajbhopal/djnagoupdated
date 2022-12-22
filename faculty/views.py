from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from faculty.models import faculty
from student.models import student
from student.models import studentresult
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def facultyprofile(req):
	return render(req,'facprofile.html')

def facenroll(req):
	encryptedpassword=make_password(req.POST['password'])
	ob=faculty()
	ob.name=req.POST.get("name")
	ob.email=req.POST.get("emailid")
	ob.password=encryptedpassword
	ob.mobileno=req.POST.get("mobileno")
	ob.subject=req.POST.get("subject")
	ob.save()
	return render(req,'admmessage.html')

def deletefac(req):
    email=req.GET.get("email")
    delfac=faculty.objects.get(email=email)
    delfac.delete()
    return render(req,'admmessage.html')

def modfac(req):
	if req.method=="GET":
		email=req.GET.get("email")
		modfac=faculty.objects.get(email=email)
		modfac=faculty.objects.filter(email=email)
		return render(req,'modifyfac.html',{'modfac':modfac})
	else:
		email=req.GET.get("email")
		encryptedpassword=make_password(req.POST['password'])
		modfac2=faculty.objects.get(email=email)
		modfac2.name=req.POST.get("name")
		modfac2.mobileno=req.POST.get("mobileno")
		modfac2.subject=req.POST.get("subject")
		modfac2.password=encryptedpassword
		modfac2.save()
		#modfac2.faculty.object.all()
		return render(req,'admmessage.html')
		
def facpass(req):
    if req.method=="GET":
        email=req.GET.get("email")
        cpass=faculty.objects.get(email=email)
        cpass=faculty.objects.filter(email=email)
        return render(req,'facpas.html',{'cpass':cpass})
    else:
        email=req.GET.get("email")
        encryptedpassword=make_password(req.POST['password'])
        cpass=faculty.objects.get(email=email)
        cpass.password=encryptedpassword
        cpass.save()
        messages.success(req,'Facaulty Password Changed Successfully')
        return redirect('/checkrole')



def uploadfacimg(req):
	if req.method=="GET":
		email=req.GET.get("email")
		img=faculty.objects.get(email=email)
		img=faculty.objects.filter(email=email)
		return render(req,'facimage.html',{'img':img})
	else:
		email=req.GET.get("email")
		img2=faculty.objects.get(email=email)
		img2.image=req.FILES['image']
		img2.save()
		return render(req,'admmessage.html')

