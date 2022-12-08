from django.contrib import admin

# Register your models here.
from . models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "course"]
    # class Meta:
    #     model = Student
    #     fields = "__all__"
    