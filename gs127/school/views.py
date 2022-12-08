from django.shortcuts import render

# Create your views here.



from django.views.generic.edit import CreateView
from .models import Student
from django import forms
class StudentCreateView(CreateView):
    model = Student
    fields = ["name", "email", "password"]
    # success_url = "/thanks/"
    template_name = "school/sform.html"

    def get_form(self):
        form = super().get_form()
        form.fields["password"].widget = forms.PasswordInput(attrs = {"class": "myclass"})
        return form

from .forms import StudentForm
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = "school/student_form.html"
    success_url = "/thanks/"


from django.views.generic.base  import TemplateView


class ThanksTemplateView(TemplateView):
    template_name = "school/thanks.html"


from django.views.generic.detail import DetailView


class StudentDetailView(DetailView):
    model = Student
