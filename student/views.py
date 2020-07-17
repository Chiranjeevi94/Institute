from django.shortcuts import render
from app1.models import ClassModel
from student.forms import RegisterForm
from student.models import StudentModel
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
    name = request.POST.get("name")
    cno = request.POST.get("contactno")
    email = request.POST.get("email")
    pwd =  request.POST.get("password")
    ss = StudentModel(name=name,contactno=cno,email=email,password=pwd)
    ss.save()
    return render(request,"student/studentregister.html",{"message":"Registered Successfully"})