from django.shortcuts import redirect, render
from main.models import Meeting, ToDo, EventGallery

from teachers.models import Teacher
from students.models import Student




def home(request):
    students= Student.objects.all()
    teachers = Teacher.objects.all()  # for teacher counter
  # for club counter

    meetings = Meeting.objects.all()  # for meetings
    todos = ToDo.objects.order_by('-todo_time')  # for todo
    events = EventGallery.objects.order_by('-date')  # for events
    context = {

        'teachers': teachers,
        'meetings': meetings,
        'todos': todos,
        'events': events,
    }
    return render(request, 'index.html', context)


def redirectView(request):
    response = redirect('/welcome/')
    return response
