from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Student

class StudentListView(ListView):
    model = Student
    # template_name_suffix = "_get"
    # ordering = ['name']
    template_name = "school/student.html"
    context_object_name = "students"

    # def get_queryset(self):
    #     return Student.objects.filter(course="python")

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['freshers'] = Student.objects.all().order_by('name')
    #     return context



class StudentDetailView(DetailView):
    model = Student
    template_name = "school/mystudent.html"
    context_object_name = 'stu'
    pk_url_kwarg = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["students"] = Student.objects.all()
        return context



from .forms import ContactForm
from django.views.generic.edit import FormView
class ContactFormView(FormView):
    template_name = "school/contact.html"
    form_class = ContactForm
    success_url = '/thankyou/'
    # http://127.0.0.1:8000/school/thankyou/
    # success_url = 'school/thankyou/'
    # http://127.0.0.1:8000/contact/school/thankyou/

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)


from django.views.generic.base import TemplateView

class ThankyouTemplateView(TemplateView):
    template_name = "school/thankyou.html"