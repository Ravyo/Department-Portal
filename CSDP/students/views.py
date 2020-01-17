from django.shortcuts import render, redirect
# Create your views here.
from datetime import date
from students.models import Student,StudentInfo,EduLevel,StudentQualification
from .forms import AddStudentForm


def index(request):
    students = Student.objects.order_by('student_id')
    context = {
        'students': students,
    }
    return render(request, 'students/student_index.html', context)


# detail view
def student_detail(request, student_id):
    pupil = Student.objects.get(pk=student_id)
    details = StudentInfo.objects.get(pk=student_id)

    def age(dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    studentAge = age(details.dateOfBirth)
    qualifications = EduLevel.objects.all()
    context = {
        'pupil': pupil,
        'details': details,
        'studentAge': studentAge,
        'qualifications': qualifications,



    }
    return render(request, 'students/studentdetail.html', context)


# create view
def addStudentView(request):
    form = AddStudentForm()
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            student_id = form.cleaned_data['student_id']
            roll = form.cleaned_data['roll']
            semester = form.cleaned_data['semester']
            section = form.cleaned_data['joined']
            phone = form.cleaned_data['phone']
            registration = form.cleaned_data['registration']
            session_start = form.cleaned_data['session_start']
            session_end = form.cleaned_data['session_end']
            instance = Student(
                name=name, student_id=student_id,
                roll=roll,
                semester=semester, section=section,
                phone=phone, registration=registration, session_start=session_start,
                session_end=session_end
            )
            instance.save()
            form = AddStudentForm()
            return redirect('/students/')

    else:
        form = AddStudentForm()
    context = {
        'form': form,
    }
    return render(request, 'students/add_student.html', context)



