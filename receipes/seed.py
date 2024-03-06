# This is to generate fake data.

from .models import *
from faker import Faker
import random

fake = Faker()

def create_subject_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student = student ,
                    subject = subject ,
                    marks = random.randint(0 , 100)
                )
    except Exception as e:
        print(e)

def seed_db(n = 10) -> None :
    try:
        for i in range(0 , n):

            # Now we will generate random department and student id
            department_gen = Department.objects.all()
            random_index = random.randint(0 , len(department_gen)-1)
            department = department_gen[random_index]

            # Now creating unique id for student
            student_id = f'STU-{random.randint(100 , 1000)}-2024'

            # Now generating fake data for other variables
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18 , 35)
            student_address = fake.address()

            # Creating the id in new varible
            student_id_obj = StudentID.objects.create(student_id = student_id)

            # Storing all the fake data that is generated
            student_obj = Student.objects.create(
                department = department , 
                student_id = student_id_obj , 
                student_name = student_name , 
                student_email = student_email , 
                student_age = student_age , 
                student_address = student_address
            )

    except Exception as e :
        print(e)

from django.db.models import Sum

def generate_report_card():
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    i = 1
    for rank in ranks:
        print()
        ReportCard.objects.create(
            student = rank ,
            student_rank = i
        )
        i = i + 1