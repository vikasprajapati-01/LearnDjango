from django.shortcuts import render , redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from receipes.models import *

# The below two line are for the Custom User Model
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

@login_required(login_url='/loginpage/')
def receipe(request):
    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get('reciepe_image')
        receipe_name = data.get('reciepe_name')
        receipe_description = data.get('reciepe_description')

        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description,
        )

        # print(reciepe_name)
        # print(reciepe_description)
        # print(reciepe_image)

        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipe' : queryset}

    return render(request , 'recep.html', context)

@login_required(login_url='/loginpage/')
def update_receipe(request , slug):
    queryset = Receipe.objects.get(slug = slug)
    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get('reciepe_image')
        receipe_name = data.get('reciepe_name')
        receipe_description = data.get('reciepe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')

    context = {'receipe' : queryset}

    return render(request , 'update_recep.html' , context)

@login_required(login_url='/loginpage/')
def delete_receipe(request , id):

    queryset = Receipe.objects.get(id = id)
    queryset.delete()

    return redirect('/receipes/')

def logout_page(request):
    logout(request)
    return redirect('/loginpage/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Username name does not exist')
            return redirect('/loginpage/')

        user = authenticate(username = username , password = password)

        if user is None :
            messages.error(request , 'Incorrect Password')
            return redirect('/loginpage/')
        else:
            login(request , user)
            return redirect('/receipes/')

    return render(request , 'login.html')

def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/registerpage/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)

        user.save()

        messages.info(request , 'Account created successfully')

        return redirect('/loginpage/')

    return render(request , 'register.html')

from django.db.models import Q  
# This is imported to search multiple fields at a time

def get_students(request):
    queryset = Student.objects.all()

    # Searching a student
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search)
        )
    
    paginator = Paginator(queryset , 20)  # Shows 10 students per page
    page_number = request.GET.get("page" , 1)  # 1 is written as a default page number(i.e. if not varible as 'page' exists)
    page_obj = paginator.get_page(page_number)

    return render(request , 'report/students.html' , {'queryset' : page_obj})

# To print the student marks using student id
from django.db.models import Sum

def see_marks(request , student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)

    total_marks = queryset.aggregate(total_marks = Sum('marks'))

    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    # - sign is used because we need in descending order
    i = 1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank = i
            break
        i = i + 1

    return render(request , 'report/see_marks.html' , {'queryset' : queryset , 'total_marks' : total_marks , 'current_rank' : current_rank})