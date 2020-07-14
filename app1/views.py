from django.shortcuts import render,redirect
from app1.forms import ScheduleForm
from app1.models import ClassModel


def admin_login(request):
    return render(request,"adminlogin.html")

def adminwelcome(request):
    name = request.POST.get("usr")
    password = request.POST.get("pass")
    if name == "Admin" and password == "Admin123":
        return render(request,"adminwelcome.html")
    else:
        return render(request,"adminlogin.html",{"error": "Please check the login credentials"})

def scheduleclass(request):
    r = ScheduleForm()
    return render(request,"scheduleclass.html",{"formclass": r})

def savecourse(request):
    course = request.POST.get("course")
    faculty = request.POST.get("faculty")
    date = request.POST.get("date")
    time = request.POST.get("time")
    fee = request.POST.get("fee")
    duration = request.POST.get("duration")
    sm = ClassModel(course=course,faculty=faculty,date=date,time=time,fee=fee,duration=duration)
    sm.save()
    return render(request,"scheduleclass.html",{"message":"Details are Saved Successfully"})

def viewclasses(request):
    result = ClassModel.objects.all()
    return render(request,"viewclasses.html",{"data": result})

def deletecourse(request):
    del_course = request.GET.get("no")
    ClassModel.objects.filter(id=del_course).delete()
    return render(request,"viewclasses.html",{"msg":"Record has been deleted"})

def updatecourse(request):
    id = request.GET.get("no")
    result = ClassModel.objects.get(id=id)
    return render(request,"updatecourse.html",{"data":result})

def modifycourse(request):
    id = request.POST.get("t1")
    course = request.POST.get("t2")
    faculty = request.POST.get("t3")
    date = request.POST.get("t4")
    fee = request.POST.get("t6")
    time = request.POST.get("t5")
    duration = request.POST.get("t7")
    ClassModel.objects.filter(id=id).update(course=course,faculty=faculty,date=date,time=time,fee=fee,duration=duration)
    return redirect("viewclasses")

