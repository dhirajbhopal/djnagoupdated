from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import student
from student.models import studentresult
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.db.utils import IntegrityError
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

def dashboard(request):
	return render(request,'userdashboard.html')

def studentrofile(request):
    return render(request,'stuprofile.html')

def generateOTP(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def signuptask(request):
    code = 0
    try:
        encryptedpassword=make_password(request.POST['password'])
        ob=student() 
        ob.mobileno=request.POST.get("mobileno")
        ob.email=request.POST.get("emailid")
        ob.rollno=request.POST.get("rollno")
        ob.name=request.POST.get("name")
        ob.lastname=request.POST.get("name1")
        ob.fathername=request.POST.get("father")
        ob.fatherlastname=request.POST.get("father1")
        ob.email=request.POST.get("emailid")
        ob.password=encryptedpassword
        ob.gender=request.POST.get("gender")
        ob.dob=request.POST.get("dob")
        ob.dob=request.POST.get("dob")
        ob.address=request.POST.get("add")
        #if len(request.FILES)!=0:
        ob.save()
    except IntegrityError as ex:          
        code = 1
    except Exception as ex:       
        code = 2
    return redirect("/cheksignup?err="+str(code))  

def cheksignup(req):
    code = req.GET.get("err")
    msg = ""
    if code=="0":
        msg="Registeration Done Successfully"
        return render(req,"default.html",{"msg":msg})
    if code=="1":
        msg="Phone or Email is Already Registered !"        
    if code=="2":
        msg="Registeration Failed !"        
    return render(req,"usersignup.html",{"msg":msg})  

            
def entermarks(req):
    result=studentresult()    
    result.rollno=req.POST.get("rollno")
    result.branch=req.POST.get("branch1")
    result.semester=req.POST.get("semester")
    result.subject=req.POST.get("subject")
    result.subjectcode=req.POST.get("subjectcode")
    result.fullmark=(req.POST.get("fullmark"))
    result.obtainmark=(req.POST.get("obtainmark"))
    result.pracfullmark=(req.POST.get("pracfullmark"))
    result.pracobtmark=(req.POST.get("pracobtmark"))
    result.totalmark=(req.POST.get("totalmark"))
    result.result=req.POST.get("result")
    result.CGPA=(req.POST.get("CGPA"))
    result.resultdate=req.POST.get("resultdate")
    result.save()       
    return render(req,'admmessage.html')

def deletestu(req):
    email=req.GET.get("email")
    delstu=student.objects.get(email=email)
    delstu.delete()
    return render(req,'admmessage.html')

def stupass(req):
    if req.method=="GET":
        email=req.GET.get("email")
        cpass=student.objects.get(email=email)
        cpass=student.objects.filter(email=email)
        return render(req,'stupas.html',{'cpass':cpass})
    else:
        email=req.GET.get("email")
        encryptedpassword=make_password(req.POST['password'])
        cpass=student.objects.get(email=email)
        cpass.password=encryptedpassword
        cpass.save()
        messages.success(req,'Changed Successfully')
        return redirect('/checkrole')

def modstu(req):
    if req.method=="GET":
        email=req.GET.get("email")
        modstu=student.objects.get(email=email)
        modstu=student.objects.filter(email=email)
        return render(req,'modstudent.html',{'modstu':modstu})
    else:
        email=req.GET.get("email")
        encryptedpassword=make_password(req.POST['password'])
        modstu2=student.objects.get(email=email)
        modstu2.mobileno=req.POST.get("mobileno")
        modstu2.password=encryptedpassword
        modstu2.save()
        """modfac2.faculty.object.all()"""
        return render(req,'admmessage.html')

def modresult(req):
    if req.method=="GET":
        ids=req.GET.get("ids")
        modres=studentresult.objects.get(id=ids)
        modres=studentresult.objects.filter(id=ids)
        return render(req,'modifyresult.html',{'modres':modres})
    else:
        ids=req.GET.get("ids")
        result1=studentresult.objects.get(id=ids)
        result1.rollno=req.POST.get("rollno")
        result1.branch=req.POST.get("branch1")
        result1.semester=req.POST.get("semester")
        result1.subject=req.POST.get("subject")
        result1.subjectcode=req.POST.get("subjectcode")
        result1.fullmark=(req.POST.get("fullmark"))
        result1.obtainmark=(req.POST.get("obtainmark"))
        result1.pracfullmark=(req.POST.get("pracfullmark"))
        result1.pracobtmark=(req.POST.get("pracobtmark"))
        result1.totalmark=(req.POST.get("totalmark"))
        result1.result=req.POST.get("result")
        result1.CGPA=(req.POST.get("CGPA"))
        result1.resultdate=req.POST.get("resultdate")
        result1.email=req.POST.get("emailid")
        result1.save()
        return render(req,'admmessage.html')


def sendmail(email,otp):
    try:
        print("mail iniitializing")
        message ="""<html><body><h1 style='color:red'>Welcome to Cybrom</h1> <hr>Hello Mr. {0},<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Please enter otp to complete your registraion <b><br><br>
        Your OTP is :- <span style='color:red'>  {1} </spna> </b> please don't share to anyone.<br>
        <br><b> Thanks<br><br> Team Cybrom<br>    Bhopal Branch </b></body></html>""".format(email,otp)
        smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
        print("mail part11111++++") 
        smtp.starttls()
        smtp.login("dhiraj.cybrom@gmail.com","tgoxlldbjymrxmev")
        print("mail part2222++++") 
        msg = MIMEMultipart() 
        msg['From'] ="Dhiraj Patel"
        print("mail part3333++++")
        msg['To'] = email
        print("mail part44 email")
        msg['Subject'] = "Registraion OTP"
        print("mail part55555 Subject++++")
        msg.attach(MIMEText(message, 'html'))
        print("mail part55 Message++++")
        smtp.send_message(msg)
        print("mail part777++++")
        smtp.quit()
        print("mail done+++++")      
        return True
    except Exception as ex:       
        return False


def sendotp(request):
    email = request.GET.get("email")
    print("your mail is+++++ ",email)
    if len(email)>0:
        email = email
        otp = generateOTP(6)
        print("your OTP is+++++ ",otp)
        check = sendmail(email,otp)
        print("sending mail+++++ ")
        request.session['loginotp'] = otp
        return HttpResponse("OTP Send Successfully! "+str(otp)+" ")
    else:
        return HttpResponse("OTP Send Failed, Please Try Again  !")           
                
    return HttpResponse("Email Id Not Exist !")

def imgupdate(req):
    if req.method=="GET":
        email=req.GET.get("email")
        img=student.objects.get(email=email)
        img=student.objects.filter(email=email)
        return render(req,'stuimage.html',{'img':img})
    else:
        email=req.GET.get("email")
        img2=student.objects.get(email=email)
        img2.image=req.FILES['image']
        img2.save()
        return render(req,'admmessage.html')

def updaetstu(req):
    if req.method=="GET":
        email=req.GET.get("email")
        modstu=student.objects.get(email=email)
        modstu=student.objects.filter(email=email)
        return render(req,'updatestudent.html',{'modstu':modstu})
    else:
        email=req.GET.get("email")
        modstu3=student.objects.get(email=email)
        modstu3.email=req.POST.get("emailid")
        modstu3.mobileno=req.POST.get("mobileno")
        modstu3.rollno=req.POST.get("rollno")
        modstu3.name=req.POST.get("name")
        modstu3.lastname=req.POST.get("name1")
        modstu3.fathername=req.POST.get("father")
        modstu3.fatherlastname=req.POST.get("father1")
        modstu3.dob=req.POST.get("dob")
        modstu3.doa=req.POST.get("doa")
        modstu3.address=req.POST.get("address")
        modstu3.save()
        """modfac2.faculty.object.all()"""
        return render(req,'admmessage.html')
       
def deletemark(req):
    ids=req.GET.get("ids")
    delstu=studentresult.objects.get(id=ids)
    delstu.delete()
    return render(req,'admmessage.html')


def resetstupass(req):
    try:
        email=req.POST.get("emailid")
        encryptedpassword=make_password(req.POST['password'])
        rpass=student.objects.get(email=email)
        rpass.password=encryptedpassword
        rpass.save()
        messages.success(req,'Changed Successfully')
        return redirect('/checkrole')
    except Exception as ex:
        mes="User doesnot Exist"       
        return render(req,'resetpasstemp.html',{'mes':mes}) 


    