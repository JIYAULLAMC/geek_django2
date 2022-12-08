from django.shortcuts import render

# Create your views here.

from .models import Student

from django.views.generic.list import ListView

class StudentListView(ListView):
    model = Student
    ordering = ["course"]
    template_name = "school/students.html"

