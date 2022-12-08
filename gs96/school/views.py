from django.shortcuts import render

# Create your views here.


from .models import Student, Teacher
from django.db.models import Q
def home(request):
    students = Student.objects.all()
    students = Student.objects.filter(marks=98)
    students = Student.objects.exclude(marks=98)
    students = Student.objects.all().order_by("city")
    students = Student.objects.all().order_by("-city")
    students = Student.objects.all().order_by("id")
    students = Student.objects.all().order_by("id").reverse()
    students = Student.objects.all().order_by("id")[0:5]
    students = Student.objects.values()
    students = Student.objects.values('name', 'city')
    students = Student.objects.values_list()
    students = Student.objects.values_list("id", "name")
    students = Student.objects.values_list(named=True)
    students = Student.objects.values_list("id", "name", named= True)
    students = Student.objects.using('default')
    students = Student.objects.dates("pass_date", 'year')  # distinct
    students = Student.objects.dates("pass_date", 'month') 
    students = Student.objects.dates("pass_date", 'week')
    students = Student.objects.dates("pass_date", 'day')
    qs1 = Student.objects.values_list("id", "name",named=True)
    qs2 = Teacher.objects.values_list("id", "name", named=True)
    students = qs1.union(qs2)
    qs1 = Student.objects.values_list("id",named=True)
    qs2 = Teacher.objects.values_list("id", named=True)
    students = qs1.union(qs2)   
    qs1 = Student.objects.values_list('name',named=True)
    qs2 = Teacher.objects.values_list('name', named=True)
    students = qs1.intersection(qs2)
    students = qs1.union(qs2, all=True)
    students = qs1.difference(qs2)
    students = Student.objects.filter(id=6, roll=10)
    students = Student.objects.filter(id=6) & Student.objects.filter(roll= 10)
    students = Student.objects.filter(id=6) | Student.objects.filter(roll= 10)
    students = Student.objects.filter(Q(id=6) & Q(roll=6))
    students = Student.objects.filter(Q(id=6) | Q(roll=6))

    # print("+++++++++++++++++++++++++++++++++")
    # print(students)
    # print("-------------------------------")
    # print(students.query)
    # print(students.exists())

    # return render(request, "school/home.html",{"students": students})

###### method return single object 

    student = Student.objects.get(pk=1)
    student = Student.objects.first()
    student = Student.objects.order_by('name').first()
    student = Student.objects.last()
    student = Student.objects.latest('pass_date')
    student = Student.objects.earliest('pass_date')

    student = Student.objects.all()
    student = Student.objects.get(pk=1)
    student = Student.objects.filter(pk= student.id)
    print("the data is ", student.exists())
    # Student.objects.create(name="jiya", roll=15, city="haveri", marks=45, pass_date="2021-02-11")
    # student, created = Student.objects.get_or_create(name="vishwa", roll=17, city="haveri", marks=45, pass_date="2021-02-11")

    # student = Student.objects.filter(roll=15).update(name="jiya")

    # print(student)
    # print(created)
    # student, created = Student.objects.update_or_create(name="manju", roll=20, city="haveri", marks=45, pass_date="2021-02-11", defaults={"name" : "sanju"})

    # print(student)
    # print(created)


    # bulk objects creation

    # objs = [
    #     Student(name="likhit", roll=21, city="mumbai",marks=78, pass_date="2021-03-23"),
    #     Student(name="reddy", roll=22, city="tlugu",marks=87, pass_date="2021-09-23"),
    #     Student(name="prajwal", roll=23, city="mumbai",marks=99, pass_date="2021-04-13"),
    # ]
    # student = Student.objects.bulk_create(objs)

    # student = Student.objects.in_bulk([1,2,3])
    # print(student[0])
    # # print(student[1].name)

    # print(Student.objects.all().count())

    # field lookups   

    
    # return render(request, "school/home.html",{"student": student})
    
    return render(request, "school/home.html",{"students": students})