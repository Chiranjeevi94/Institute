from django.shortcuts import render,redirect
from app1.models import ClassModel
from student.forms import RegisterForm
from student.models import StudentModel,CourseModel
import sys
# Create your views here.

def index(request):
    return render(request, "student/main.html")

def student_index(request):
    r = ClassModel.objects.all()
    return render(request, "student/studentindex.html", {"data":r})

def student_register(request):
    reg = RegisterForm()
    return render(request,"student/studentregister.html",{"reg":reg})

def savestudent(request):
    #name = request.POST.get("name")
    #cno = request.POST.get("contactno")
    #email = request.POST.get("email")
    #pwd =  request.POST.get("password")
    #ss = StudentModel(name=name,contactno=cno,email=email,password=pwd)
    ss = RegisterForm(request.POST,request.FILES)
    if ss.is_valid():
        ss.save()
        return render(request,"student/studentregister.html",{"message":"Registered Successfully"})
    else:
        return render(request,"student/studentregister.html",{"reg":ss})

def studentlogin(request):
    return render(request,"student/studentlogin.html")


def studentwelcome(request):
    email = request.POST.get("t1")
    password = request.POST.get("t2")
    try:
        sf = StudentModel.objects.get(email=email, password=password)
        usr = sf.name
        contact = sf.contactno
        if email == email and password == password:
            return render(request,"student/studenthome.html",{"usr":usr,"contact":contact})
    except StudentModel.DoesNotExist:
        return render(request,"student/studentlogin.html",{"loginerror":"Invalid Username and Password"})

def studenthome(request):
    return render(request,"student/studenthome.html")

def enrollcourse(request):
    r = ClassModel.objects.all()
    return render(request, "student/enrollcourse.html", {"data":r})

def registercourse(request,na,contact):
    name = request.GET.get("na")
    print(na)
    contactno = request.GET.get("cn")
    print(contactno)
    course = request.GET.get("cr")
    sn = CourseModel(name=name,contactno=contactno,course=course)
    sn.save()
    return render(request,"student/studenthome.html")

