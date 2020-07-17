from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('main/', views.index, name="main"),
    path('studentindex/', views.student_index, name="studentindex"),
    path('studentregister/',views.student_register,name="studentregister"),
    path('savestudent/',views.savestudent,name="savestudent")
]
