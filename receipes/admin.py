from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Receipe)

admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)

admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' , 'marks']

admin.site.register(SubjectMarks , SubjectMarkAdmin)

from django.db.models import Sum

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student' , 'student_rank'  , 'total_marks' , 'date_of_report']
    ordering = ['student_rank']

    def total_marks(self , obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        marks = subject_marks.aggregate(marks = Sum('marks'))
        print()
        return marks['marks']

admin.site.register(ReportCard , ReportCardAdmin)