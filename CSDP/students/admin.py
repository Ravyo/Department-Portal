from django.contrib import admin
from students.models import Student
from students.models import StudentInfo
from students.models import EduLevel,StudentQualification


admin.site.register(Student)
admin.site.register(StudentInfo)
admin.site.register(EduLevel)
admin.site.register(StudentQualification)